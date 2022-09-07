from .handlers import User

DICT_FUNC = {}


def register_message_handler(func, commands: str | list, arguments: User = None):
    if isinstance(commands, str):
        commands = [commands]

    for cmd in commands:
        if arguments:
            DICT_FUNC.update({cmd: {'function': func, "arguments": arguments}})
        else:
            DICT_FUNC[cmd] = func

    return func
