from .handlers import User

DICT_FUNC = {}


def register_message_handler(func, commands: str | list, arguments: User = None, quantity_arg: int = 0):
    if isinstance(commands, str):
        commands = [commands]

    for cmd in commands:
        if arguments:
            DICT_FUNC.update({cmd: {'function': func, "arguments": arguments, "quantity_arg": quantity_arg}})
        else:
            DICT_FUNC[cmd] = func

    return func
