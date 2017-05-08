import unittest
from p30_testingClassSurvey import AnonymousSurvey





class TestAnonymousSurvey (unittest.TestCase):
    #testing the class AnonymousSurvey


    # unittest has a setUp() method that allows you to create these objects once 
    # then use them in each of your test methods
    def setUp(self):
        #create a survey and a set of responses for use in all methods
        question = "What is your favorite programming language?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Python', 'C', 'Java']

    #If this test fails then it shows there was a problem when
    #storing in user response
    def test_store_single_response(self):
        #test that single response is stored successfully
        # question = "What is your favorite programming language?"
        # my_survey = AnonymousSurvey(question)
        # my_survey.store_response('Python')
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        # self.assertIn('Python', my_survey.responses)

    def test_storeThreeResponses(self):
        # we're now checking multiple responses
        # question = "What is your favorite programming language?"
        # my_survey = AnonymousSurvey(question)
        # responses = ['Python', 'C', 'Java']
        # for response in responses:
        #     my_survey.store_response('Python')

        # for response in responses:
        #     self.assertIn('Python', my_survey.responses)
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()