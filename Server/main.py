from models import *


def main():
    with db:
        # Indicators.insert(indicator_question='Какой-то вопрос').execute()
        # Indicators.delete().where(Indicators.indicator_question == 'Какой-то вопрос').execute()

       indicators_selection = Indicators.select()
       indicators_questions = [indicator.indicator_question for indicator in indicators_selection]
       print(indicators_questions)
       print(type(indicators_questions))


if __name__ == '__main__':
    main()
