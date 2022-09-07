from bot import DICT_FUNC, input_error


@input_error
def text_parsing(text: str) -> tuple:
    data = DICT_FUNC.get(text.lower())

    if not data:
        text = text.split(' ')
        # print(text)

        data = DICT_FUNC.get(text[0].lower())

        if not data:
            raise ValueError(f"Sorry, but there is no '{text[0]}' command")

    if isinstance(data, dict):
        if isinstance(text, str):
            raise ValueError("Give me name and phone please")

        arg = data['arguments']
        try:
            args = arg(*text[1:])
        except TypeError:
            if text[0].lower() == "phone":
                raise ValueError("Enter user name")
            raise ValueError("Please tell me your name and phone number, separated by a space")

        return data['function'], args

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
