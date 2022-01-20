from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from typing import List


class QuizResultService:
    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto

    def get_result(self) -> float:
        """
        Рассчитывает результаты пользователя. Возвращает дробное число с двумя знаками после запятой.
        :return: float
        """
        result_quiz_1 = int(1)
        z = 1
        if not self.answers_dto.answers[0].choices:
            result_quiz_1 = 0
        else:
            for i in range(len(self.quiz_dto.questions[0].choices)):
                if self.quiz_dto.questions[0].choices[i].is_correct:
                    if not self.quiz_dto.questions[0].choices[i].uuid in self.answers_dto.answers[0].choices:
                        result_quiz_1 = 0
                if not self.quiz_dto.questions[0].choices[i].is_correct:
                    if self.quiz_dto.questions[0].choices[i].uuid in self.answers_dto.answers[0].choices:
                        result_quiz_1 = 0

        result_quiz_2 = int(1)
        if not self.answers_dto.answers[1].choices:
            result_quiz_2 = 0
        else:
            for i in range(len(self.quiz_dto.questions[1].choices)):
                if self.quiz_dto.questions[1].choices[i].is_correct:
                    if not self.quiz_dto.questions[1].choices[i].uuid in self.answers_dto.answers[1].choices:
                        result_quiz_2 = 0
                if not self.quiz_dto.questions[1].choices[i].is_correct:
                    if self.quiz_dto.questions[1].choices[i].uuid in self.answers_dto.answers[1].choices:
                        result_quiz_2 = 0

        result_quiz_3 = int(1)
        if not self.answers_dto.answers[2].choices:
            result_quiz_3 = 0
        else:
            for i in range(len(self.quiz_dto.questions[2].choices)):
                if self.quiz_dto.questions[2].choices[i].is_correct:
                    if not self.quiz_dto.questions[2].choices[i].uuid in self.answers_dto.answers[2].choices:
                        result_quiz_3 = 0
                if not self.quiz_dto.questions[2].choices[i].is_correct:
                    if self.quiz_dto.questions[2].choices[i].uuid in self.answers_dto.answers[2].choices:
                        result_quiz_3 = 0

        result_quiz_4 = int(1)
        if not self.answers_dto.answers[3].choices:
            result_quiz_4 = 0
        else:
            for i in range(len(self.quiz_dto.questions[3].choices)):
                if self.quiz_dto.questions[3].choices[i].is_correct:
                    if not self.quiz_dto.questions[3].choices[i].uuid in self.answers_dto.answers[3].choices:
                        result_quiz_4 = 0
                if not self.quiz_dto.questions[3].choices[i].is_correct:
                    if self.quiz_dto.questions[3].choices[i].uuid in self.answers_dto.answers[3].choices:
                        result_quiz_4 = 0

        result_quiz_5 = int(1)
        if not self.answers_dto.answers[4].choices:
            result_quiz_5 = 0
        else:
            for i in range(len(self.quiz_dto.questions[4].choices)):
                if self.quiz_dto.questions[4].choices[i].is_correct:
                    if not self.quiz_dto.questions[4].choices[i].uuid in self.answers_dto.answers[4].choices:
                        result_quiz_5 = 0
                if not self.quiz_dto.questions[4].choices[i].is_correct:
                    if self.quiz_dto.questions[4].choices[i].uuid in self.answers_dto.answers[4].choices:
                        result_quiz_5 = 0

        count = len(self.quiz_dto.questions)
        result = float(result_quiz_1 + result_quiz_2 + result_quiz_3 + result_quiz_4 + result_quiz_5) / count
        return round(result, 2)
