from p30_testingClassSurvey import AnonymousSurvey

#define a question and make a survey
question = "What is your first programming language? "
my_survey = AnonymousSurvey(question)

#show the question and store responses to the question
my_survey.show_question()
print("Enter 'q' anytime to quit \n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results
print("\nThank you all for participating in the survey! ")
my_survey.show_results()