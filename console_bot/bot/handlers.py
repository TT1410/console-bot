from .errors import input_error
from .types import User, USERS


def hello() -> str:
    """
    Отвечает в консоль "How can I help you?"
    :return:
    """
    return "How can I help you?"


def add_user(user: User) -> None:
    """
    По этой команде бот сохраняет в памяти (в словаре например) новый контакт.
    Пользователь вводит команду add, имя и номер телефона, обязательно через пробел.
    :param user:
    :return:
    """
    USERS[user.name] = user


@input_error
def change_user(user: User) -> None:
    """
    По этой команде бот сохраняет в памяти новый номер телефона для существующего контакта.
    Пользователь вводит команду change, имя и номер телефона, обязательно через пробел.
    :param user:
    :return:
    """
    USERS.pop(user.name)

    USERS[user.name] = user


@input_error
def user_phone(user: User) -> str:
    """
    По этой команде бот выводит в консоль номер телефона для указанного контакта.
    Пользователь вводит команду phone и имя контакта, чей номер нужно показать, обязательно через пробел.
    :param user:
    :return:
    """
    return USERS[user.name].phone


def show_all_users() -> str:
    """
    По этой команде бот выводит все сохраненные контакты с номерами телефонов в консоль.
    :return:
    """
    format_users = ["{:<10}: {}".format(user.name, user.phone) for user in USERS.values()]

    return '\n'.join(format_users)


def close_bot() -> None:
    """
    По любой из команд: "good bye", "close", "exit",
    бот завершает свою роботу после того, как выведет в консоль "Good bye!".
    :return:
    """
    return "Good bye!"
