from typing import List
from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO


def quiz_object_dto() -> QuizDTO:
    """
    Создаёт экзмпляр класса "QuizDTO".
    :return: QuizDTO
    """
    choices_1: List[ChoiceDTO] = [
        ChoiceDTO(
            "1-1-1",
            "IronPython",
            False
        ),
        ChoiceDTO(
            "1-1-2",
            "CPython",
            True
        ),
        ChoiceDTO(
            "1-1-3",
            "PyPy",
            False
        ),
        ChoiceDTO(
            "1-1-4",
            "Jython",
            False
        )
    ]
    choices_2: List[ChoiceDTO] = [
        ChoiceDTO(
            "1-2-1",
            "PyPy",
            True
        ),
        ChoiceDTO(
            "1-2-2",
            "Jython",
            False
        ),
        ChoiceDTO(
            "1-2-3",
            "IronPython",
            False
        ),
        ChoiceDTO(
            "1-2-4",
            "CPython",
            False
        )
    ]
    choices_3: List[ChoiceDTO] = [
        ChoiceDTO(
            "1-3-1",
            "a = int(15)",
            True
        ),
        ChoiceDTO(
            "1-3-2",
            "let a = 15",
            False
        ),
        ChoiceDTO(
            "1-3-3",
            "int a = 15",
            False
        ),
        ChoiceDTO(
            "1-3-4",
            "$a = 15",
            False
        )
    ]
    choices_4: List[ChoiceDTO] = [
        ChoiceDTO(
            "1-4-1",
            "var",
            False
        ),
        ChoiceDTO(
            "1-4-2",
            "real",
            False
        ),
        ChoiceDTO(
            "1-4-3",
            "int",
            True
        ),
        ChoiceDTO(
            "1-4-4",
            "float",
            True
        ),
    ]
    choices_5: List[ChoiceDTO] = [
        ChoiceDTO(
            "1-5-1",
            "Django",
            True
        ),
        ChoiceDTO(
            "1-5-2",
            "Meteor",
            False
        ),
        ChoiceDTO(
            "1-5-3",
            "CherryPy",
            True
        ),
        ChoiceDTO(
            "1-5-4",
            "Angular",
            False
        )
    ]
    questions: List[QuestionDTO] = [
        QuestionDTO(
            "1-1",
            "Эталонным интерпретатором языка программирования Python является: ",
            choices_1
        ),
        QuestionDTO(
            "1-2",
            "Эталонным интерпретатором языка программирования Python является: ",
            choices_2
        ),
        QuestionDTO(
            "1-3",
            "Где правильно создана переменная: ",
            choices_3
        ),
        QuestionDTO(
            "1-4",
            "Какие типы переменных существуют в языке програмирования Python: ",
            choices_4
        ),
        QuestionDTO(
            "1-5",
            "Выберите фреймворки для языка программирования Python: ",
            choices_5
        )
    ]

    quiz_dto = QuizDTO(
        "1",
        "Тест на знание языка программирования Python",
        questions
    )
    return quiz_dto


def answers_object_dto(answers_dicts: List) -> AnswersDTO:
    """
    Создаёт экзмепляр класса "AnswersDTO".
    :param answers_dicts: словарь, содержащий ответы пользователя
    :return:
    """
    answer_for_question_1: List = []
    if answers_dicts[0]["option_1"]:
        answer_for_question_1.append("1-1-1")
    if answers_dicts[0]["option_2"]:
        answer_for_question_1.append("1-1-2")
    if answers_dicts[0]["option_3"]:
        answer_for_question_1.append("1-1-3")
    if answers_dicts[0]["option_4"]:
        answer_for_question_1.append("1-1-4")

    answer_for_question_2: List = []
    if answers_dicts[1]["option_1"]:
        answer_for_question_2.append("1-2-1")
    if answers_dicts[1]["option_2"]:
        answer_for_question_2.append("1-2-2")
    if answers_dicts[1]["option_3"]:
        answer_for_question_2.append("1-2-3")
    if answers_dicts[1]["option_4"]:
        answer_for_question_2.append("1-2-4")

    answer_for_question_3: List = []
    if answers_dicts[2]["option_1"]:
        answer_for_question_3.append("1-3-1")
    if answers_dicts[2]["option_2"]:
        answer_for_question_3.append("1-3-2")
    if answers_dicts[2]["option_3"]:
        answer_for_question_3.append("1-3-3")
    if answers_dicts[2]["option_4"]:
        answer_for_question_3.append("1-3-4")

    answer_for_question_4: List = []
    if answers_dicts[3]["option_1"]:
        answer_for_question_4.append("1-4-1")
    if answers_dicts[3]["option_2"]:
        answer_for_question_4.append("1-4-2")
    if answers_dicts[3]["option_3"]:
        answer_for_question_4.append("1-4-3")
    if answers_dicts[3]["option_4"]:
        answer_for_question_4.append("1-4-4")

    answer_for_question_5: List = []
    if answers_dicts[4]["option_1"]:
        answer_for_question_5.append("1-5-1")
    if answers_dicts[4]["option_2"]:
        answer_for_question_5.append("1-5-2")
    if answers_dicts[4]["option_3"]:
        answer_for_question_5.append("1-5-3")
    if answers_dicts[4]["option_4"]:
        answer_for_question_5.append("1-5-4")

    answers: List[AnswerDTO] = [
        AnswerDTO(
            "1-1",
            answer_for_question_1
        ),
        AnswerDTO(
            "1-2",
            answer_for_question_2
        ),
        AnswerDTO(
            "1-3",
            answer_for_question_3
        ),
        AnswerDTO(
            "1-4",
            answer_for_question_4
        ),
        AnswerDTO(
            "1-5",
            answer_for_question_5
        )
    ]
    answers_dto = AnswersDTO(
        "1",
        answers
    )
    return answers_dto