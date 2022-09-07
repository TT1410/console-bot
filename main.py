from bot import DICT_FUNC, input_error, User


@input_error
def text_parsing(text: str) -> tuple:
    data = DICT_FUNC.get(text.lower())

    if not data:
        command, *args = text.split(maxsplit=1)
        args = args[0] if args else None

        data = DICT_FUNC.get(command.lower())

        if not data:
            raise ValueError(f"Sorry, but there is no '{command}' command")
    else:
        command, args = text.lower, None

    if isinstance(data, dict):
        if not args:
            if data['quantity_arg'] == 1:
                raise ValueError("Enter user name")
            raise ValueError("Give me name and phone please")

        args = args.rsplit(maxsplit=1)

        args = args + [''] if (len(args) < 2) and (len(args) == data['quantity_arg']) else args

        user: User = data['arguments']

        try:
            _args = user(*args)
            print(args)
        except TypeError:
            # print(command, '----', args)
            raise ValueError("Please tell me your name and phone number, separated by a space")

        return data['function'], _args

    return data, None


def main() -> None:
    while True:
        text = input()

        result = text_parsing(text)

        if not result:
            continue

        func, args = result

        if not args:
            result = func()
        else:
            result = func(args)

        if result:
            print(result)

            if result == "Good bye!":
                break


if __name__ == '__main__':
    main()
