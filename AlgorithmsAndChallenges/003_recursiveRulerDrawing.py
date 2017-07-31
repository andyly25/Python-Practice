'''
Hmm recursion sure is hard to wrap head around sometimes.
'''

def draw_line(tick_length, tick_label=''):
    # draw a line with given tick length + label
    line = '-'*tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line + "\t\t (ticklen " + str(tick_length) + ")")

def draw_interval(center_length):
    # draw tick interval based on central tick length

    # stops when length reaches 0
    if center_length>0: 
        # recursively draw top ticks
        draw_interval(center_length-1)
        # draw center ticks
        draw_line(center_length)
        # recursively draw bottom ticks
        draw_interval(center_length-1)

def draw_ruler(num_inches, major_length):
    # draw english ruler with given # inches, and major tick length

    # draw the 0 inch line
    draw_line(major_length, '0') 
    for j in range(1, 1+ num_inches):
        # draw interior ticks for inch
        draw_interval((major_length - 1))
        # draw inch line and label
        draw_line(major_length, str(j))

draw_ruler(3, 4)

'''
Results are:

---- 0       (ticklen 4)
-        (ticklen 1)            # 1
--       (ticklen 2)            # 2
-        (ticklen 1)            # 3
---      (ticklen 3)            # 4
-        (ticklen 1)
--       (ticklen 2)
-        (ticklen 1)
---- 1       (ticklen 4)
-        (ticklen 1)
--       (ticklen 2)
-        (ticklen 1)
---      (ticklen 3)
-        (ticklen 1)
--       (ticklen 2)
-        (ticklen 1)
---- 2       (ticklen 4)
-        (ticklen 1)
--       (ticklen 2)
-        (ticklen 1)
---      (ticklen 3)
-        (ticklen 1)
--       (ticklen 2)
-        (ticklen 1)
---- 3       (ticklen 4)

How it recursively works is that we feed in a 4-1=3 to the drawinterval
from there for the top tick it recursively goes 3-1 until it gets to tick size
of just 1. Then it will print out the first tick (#1). Center length at that 
time is at 2 so the center of that section will contain 2 ticks (#2). Then the 
end ticks of section will be similar to #1 with 1 ticks (#3). Now from the 
recursion we made it back to when ticklen is at 3 which is the very center of 
the inch so there will be 3 ticks (#4). The bottom half of that inch is same as
#1 - #3. And this keeps repeating until the ruler is 3 inches 
'''
