from .handlers import User, UserPhone, hello, add_user, change_user, user_phone, show_all_users, close_bot
from .register_nadlers import DICT_FUNC, register_message_handler
from .error import input_error


__all__ = [
    "DICT_FUNC",
    "User",
    "input_error"
]


register_message_handler(hello, 'hello')
register_message_handler(add_user, 'add', User)
register_message_handler(change_user, 'change', User)
register_message_handler(user_phone, 'phone', UserPhone)
register_message_handler(show_all_users, 'show all')
register_message_handler(close_bot, ["good bye", "close", "exit"])
