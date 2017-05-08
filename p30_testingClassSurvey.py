# Some of the common unittest tests are
# assertEqual(a,b) , assertNotEqual(a,b)
# assertTrue(a) , assertFalse(a)
# assertIn(item, list), assertNotIn(item, list)


class AnonymousSurvey():

    def __init__(self, question):
        #store a question and prepare to store response
        self.question = question
        self.responses = []

    def show_question(self):
        #shows question
        print(self.question)

    def store_response(self, new_response):
        #stores single response
        self.responses.append(new_response)

    def show_results(self):
        #show all response given
        print("Survey results ")
        for response in self.responses:
            print('- ' + response)


