from django.shortcuts import render, redirect
from .services import QuizResultService
from typing import List
from .dto import QuizDTO, AnswersDTO
from .forms import TestForm
from .create_dto_objects import quiz_object_dto, answers_object_dto

# глобальный список для записи ответов
answers_dicts: List = [
     {"option_1": False, "option_2": False, "option_3": False, "option_4": False},
     {"option_1": False, "option_2": False, "option_3": False, "option_4": False},
     {"option_1": False, "option_2": False, "option_3": False, "option_4": False},
     {"option_1": False, "option_2": False, "option_3": False, "option_4": False},
     {"option_1": False, "option_2": False, "option_3": False, "option_4": False}
]


def to_fixed(main_num: float, digits: int) -> str:
    """
    Округляет дробное число до заданного числа знаков после запятой.
    :param main_num: дробное число
    :param digits: количество знаков после запятой
    :return: str
    """
    return f"{main_num:.{digits}f}"


def view_home_page(request):
    """
    Выводит данные на главную страницу и сбрасывает все предыдущие ответы пользователя в списке "answers_dicts".
    :param request:
    :return:
    """
    for i in range(5):
        answers_dicts[i]["option_1"] = False
        answers_dicts[i]["option_2"] = False
        answers_dicts[i]["option_3"] = False
        answers_dicts[i]["option_4"] = False
    context = {
        'info': "Нажмите на кнопку, чтобы начать тестирование!",
        'title': "Главная страница",
        'heading': "Добро пожаловать"
    }
    return render(request, 'quiz/index.html', context)


def view_final_page(request):
    """
    Выводит данные на последнюю страницу. Выводит результат пользователя,
    а после сбрасывает все его предыдущие ответы в списке "answers_dicts".
    :param request:
    :return:
    """
    quiz_dto: QuizDTO = quiz_object_dto()
    answers_dto: AnswersDTO = answers_object_dto(answers_dicts)
    quiz_result_service = QuizResultService(
        quiz_dto,
        answers_dto
    )
    for i in range(5):
        answers_dicts[i]["option_1"] = False
        answers_dicts[i]["option_2"] = False
        answers_dicts[i]["option_3"] = False
        answers_dicts[i]["option_4"] = False
    context = {
        'info': "Вы завершили тест!",
        'title': "Тестирование завершено",
        'heading': "Тестирование завершено",
        'result': to_fixed(quiz_result_service.get_result(), 2)
    }
    return render(request, 'quiz/final.html', context)


def view_test1(request):
    """
    Выводит данные на страницу с тестом №1. Сохраняет ответы пользователя в глобальный список "answers_dicts".
    Если пользователь не был на этой странице раньше, то создаётся форма, в поля которой передаются
    соответствующие данные из глобального списка. Эта операция не влияет на результат, так как все значения списка
    "answers_dicts" изначально ложны. Если пользователь введёт новые данные, то соответствующие значения списка
    "answers_dicts" перезапишутся.
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            answers_dicts[0]["option_1"] = form.cleaned_data['option_1']
            answers_dicts[0]["option_2"] = form.cleaned_data['option_2']
            answers_dicts[0]["option_3"] = form.cleaned_data['option_3']
            answers_dicts[0]["option_4"] = form.cleaned_data['option_4']
            return redirect('test2')
    else:
        form = TestForm(initial={
            'option_1': answers_dicts[0]["option_1"],
            'option_2': answers_dicts[0]["option_2"],
            'option_3': answers_dicts[0]["option_3"],
            'option_4': answers_dicts[0]["option_4"]
        })
    context = {
        'form': form,
        'info': "Эталонным интерпретатором языка программирования Python является: ",
        'title': "Вопрос №1",
        'heading': "Вопрос №1",
        'question_1': "IronPython",
        'question_2': "CPython",
        'question_3': "PyPy",
        'question_4': "Jython",
        'submit_button': 'Сохранить ответ и перейти к следующему вопросу'
    }
    return render(request, 'quiz/test1.html', context)


def view_test2(request):
    """
    Выводит данные на страницу с тестом №2. Сохраняет ответы пользователя в глобальный список "answers_dicts".
    Если пользователь не был на этой странице раньше, то создаётся форма, в поля которой передаются
    соответствующие данные из глобального списка. Эта операция не влияет на результат, так как все значения списка
    "answers_dicts" изначально ложны. Если пользователь введёт новые данные, то соответствующие значения списка
    "answers_dicts" перезапишутся.
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            answers_dicts[1]["option_1"] = form.cleaned_data['option_1']
            answers_dicts[1]["option_2"] = form.cleaned_data['option_2']
            answers_dicts[1]["option_3"] = form.cleaned_data['option_3']
            answers_dicts[1]["option_4"] = form.cleaned_data['option_4']
            return redirect('test3')
    else:
        form = TestForm(initial={
            'option_1': answers_dicts[1]["option_1"],
            'option_2': answers_dicts[1]["option_2"],
            'option_3': answers_dicts[1]["option_3"],
            'option_4': answers_dicts[1]["option_4"]
        })
    context = {
        'form': form,
        'info': "Какой интерпретатор языка программирования Python использует технологию JIT-компиляции: ",
        'title': "Вопрос №2",
        'heading': "Вопрос №2",
        'question_1': "PyPy",
        'question_2': "Jython",
        'question_3': "IronPython",
        'question_4': "CPython",
        'submit_button': 'Сохранить ответ и перейти к следующему вопросу'
    }
    return render(request, 'quiz/test2.html', context)


def view_test3(request):
    """
    Выводит данные на страницу с тестом №3. Сохраняет ответы пользователя в глобальный список "answers_dicts".
    Если пользователь не был на этой странице раньше, то создаётся форма, в поля которой передаются
    соответствующие данные из глобального списка. Эта операция не влияет на результат, так как все значения списка
    "answers_dicts" изначально ложны. Если пользователь введёт новые данные, то соответствующие значения списка
    "answers_dicts" перезапишутся.
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            answers_dicts[2]["option_1"] = form.cleaned_data['option_1']
            answers_dicts[2]["option_2"] = form.cleaned_data['option_2']
            answers_dicts[2]["option_3"] = form.cleaned_data['option_3']
            answers_dicts[2]["option_4"] = form.cleaned_data['option_4']
            return redirect('test4')
    else:
        form = TestForm(initial={
            'option_1': answers_dicts[2]["option_1"],
            'option_2': answers_dicts[2]["option_2"],
            'option_3': answers_dicts[2]["option_3"],
            'option_4': answers_dicts[2]["option_4"]
        })
    context = {
        'form': form,
        'info': "Где правильно создана переменная: ",
        'title': "Вопрос №3",
        'heading': "Вопрос №3",
        'question_1': "a = int(15)",
        'question_2': "let a = 15",
        'question_3': "int a = 15",
        'question_4': "$a = 15",
        'submit_button': 'Сохранить ответ и перейти к следующему вопросу'
    }
    return render(request, 'quiz/test3.html', context)


def view_test4(request):
    """
    Выводит данные на страницу с тестом №4. Сохраняет ответы пользователя в глобальный список "answers_dicts".
    Если пользователь не был на этой странице раньше, то создаётся форма, в поля которой передаются
    соответствующие данные из глобального списка. Эта операция не влияет на результат, так как все значения списка
    "answers_dicts" изначально ложны. Если пользователь введёт новые данные, то соответствующие значения списка
    "answers_dicts" перезапишутся.
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            answers_dicts[3]["option_1"] = form.cleaned_data['option_1']
            answers_dicts[3]["option_2"] = form.cleaned_data['option_2']
            answers_dicts[3]["option_3"] = form.cleaned_data['option_3']
            answers_dicts[3]["option_4"] = form.cleaned_data['option_4']
            return redirect('test5')
    else:
        form = TestForm(initial={
            'option_1': answers_dicts[3]["option_1"],
            'option_2': answers_dicts[3]["option_2"],
            'option_3': answers_dicts[3]["option_3"],
            'option_4': answers_dicts[3]["option_4"]
        })
    context = {
        'form': form,
        'info': "Какие типы переменных существуют в языке програмирования Python: ",
        'title': "Вопрос №4",
        'heading': "Вопрос №4",
        'question_1': "var",
        'question_2': "real",
        'question_3': "int",
        'question_4': "float",
        'submit_button': 'Сохранить ответ и перейти к следующему вопросу'
    }
    return render(request, 'quiz/test4.html', context)


def view_test5(request):
    """
    Выводит данные на страницу с тестом №5. Сохраняет ответы пользователя в глобальный список "answers_dicts".
    Если пользователь не был на этой странице раньше, то создаётся форма, в поля которой передаются
    соответствующие данные из глобального списка. Эта операция не влияет на результат, так как все значения списка
    "answers_dicts" изначально ложны. Если пользователь введёт новые данные, то соответствующие значения списка
    "answers_dicts" перезапишутся.
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            answers_dicts[4]["option_1"] = form.cleaned_data['option_1']
            answers_dicts[4]["option_2"] = form.cleaned_data['option_2']
            answers_dicts[4]["option_3"] = form.cleaned_data['option_3']
            answers_dicts[4]["option_4"] = form.cleaned_data['option_4']
            return redirect('final')
    else:
        form = TestForm(initial={
            'option_1': answers_dicts[4]["option_1"],
            'option_2': answers_dicts[4]["option_2"],
            'option_3': answers_dicts[4]["option_3"],
            'option_4': answers_dicts[4]["option_4"]
        })
    context = {
        'form': form,
        'info': "Выберите фреймворки для языка программирования Python: ",
        'code area': '',
        'title': "Вопрос №5",
        'heading': "Вопрос №5",
        'question_1': "Django",
        'question_2': "Meteor",
        'question_3': "CherryPy",
        'question_4': "Angular",
        'submit_button': 'Завершить тестирование'
    }
    return render(request, 'quiz/test5.html', context)