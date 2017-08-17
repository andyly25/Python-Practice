'''
From: http://interactivepython.org/runestone/static/pythonds/BasicDS/SimulationPrintingTasks.html

On any average day about 10 students are working in the lab at any given hour. 
These students typically print up to twice during that time, and the length of 
these tasks ranges from 1 to 20 pages. The printer in the lab is older, 
capable of processing 10 pages per minute of draft quality. The printer could 
be switched to give better quality, but then it would produce only five pages 
per minute. The slower printing speed could make students wait too long. 
What page rate should be used?

Looking at the rates, 10 students so at most there can be 20 print tasks per hr
20tasks/1hr x 1hr/60min x 1min/60s = 1task/180s

so we can simulate from 1-180 randomly per second for our print task

Goal:
1. With queue empty at start, create queue of print tasks with timestamp
2. We look at what happens each second if:
    - new print task gets created -> add to queue for the printer
    - printer not busy and there are tasks ready
        - remove next task from print queue and assign to printer
        - currentSecond - timestamp to compute waiting time for task
        - push waiting time to a list for later processing
        - based on num of pages, figure how much time is needed
    - does 1 sec of printing while subtracts 1 from task's time
    - if task done with its time reaching zero, printer no longer busy
3. after done simulating, compute avg waiting time from list of waiting times

EXTRA:
How would I modify to reflect larger num of students?
The equation we use above to calculate 180, I would make it into a function.
The user provides how many students for simulation we plug into the function
and spit out the number to be used.

What happens if length of avg print task cut in half?
so instead of 1-20 in the Tasks class we would have for 1-10
I'll assume this makes tasks finished twice as fast.


How would you paramaterize num of students?
we can have a count of total tasks performed and we know that each students 
can do up to 2 tasks. So we can make an average from total tasks/2 = avg students

'''

# importing Queue that I made previously
from a007_Queue import Queue
# this is so we can use the random number generator
import random


# Let's create the class Printer
class Printer:
    def __init__(self, pageRates):
        self.pagerate = pageRates
        self.currentTask = None
        self.timeRemain = 0

    # ticks decrements the time of current task until printer is idle
    def tick(self):
        if self.currentTask !=None:
            self.timeRemain -= 1
            if self.timeRemain <=0:
                self.currentTask = None

    # returns a boolean if printer is busy or not
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    # starting a new task and also setting the time until done with task
    def startNext(self, newTask):
        self.currentTask = newTask
        self.timeRemain = newTask.getPages() * 60/self.pagerate



# task will represent a single printing task
class Task:
    def __init__(self, time):
        # timestamp necessary to compute waiting time,
        # represents time task was created and placed in printer queue
        self.timestamp = time
        # randomly picked from 1-20
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    # used to retrieve amt of time spent in the queue before printing begins
    def waitTime(self, currentTime):
        return currentTime - self.timestamp

# Helper function decides wheter a new print task has been created
# This will be new print task using the calculated results from earlier
# from 1-180 we simulate a random event.
def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

# allows to set total time and pages per minutes for testing
def simulation(numSec, ppm):
    # create a labPrinter for simulation
    labPrinter = Printer(ppm)
    # create a printQueue
    printQueue = Queue()
    # prepare an array for wait time
    waitTime = []

    # starts loop until currSec reaches numSec we specified
    for currSec in range(numSec):

        # if we got a 180 (print task) we then add into our printQueue
        if newPrintTask():
            task = Task(currSec)
            printQueue.enqueue(task)

        # if printQueue is not empty and labPrinter is not busy
        # we start going to the next task and we cross it off our queue
        if (not printQueue.isEmpty()) and (not labPrinter.busy()):
            nextTask = printQueue.dequeue()
            waitTime.append(nextTask.waitTime(currSec))
            labPrinter.startNext(nextTask)

        # then we begin ticking down 
        labPrinter.tick()

    # calculate avg wait time
    avgWaitTime = sum(waitTime)/len(waitTime)
    # forgot about print formatting and quick googling showed:
    # usually in format of %[flags][width][.precision]type
    # so %6.2f means the floating number should have a width of 6 and goes up 
    # to 2 decimal places  e.g. if number was 3.2 -> _ _ _ _ _ 3 . 2 0
    print("Avg wait %6.2f secs %3d tasks remaining." % (avgWaitTime, printQueue.size()))

# we're doing 10 runs
# for i in range(10):
#     simulation(3600, 5)

def simulate(runs, time, ppm):
    print("\nBeginning Simulation with " + str(ppm) + " page per minute")
    for i in range(runs):
        simulation(time, ppm)

# There's a huge difference in results between 5 ppm and 10 ppm
simulate(10, 3600, 5)
simulate(10, 3600, 10)