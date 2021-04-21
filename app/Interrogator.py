class Interrogator:

    def get_answer(question, answers, error_message):
        answered = False
        while answered == False:
            answer = input(question + ": ")
            if answer.upper() in (a.upper() for a in answers):
                answered = True
            else:
                print(error_message)
        return answer

    def get_text(question, error_message):
        valid = False
        while valid == False:
            text = input(question + ": ")
            if len(text.strip()) > 0:
                valid = True
            else:
                print(error_message)
        return text