
def input_error(func):
    def inner(*args, **kwargs) -> None:
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(e)
        except KeyError as e:
            print(f"User {e} not found")
        except IndexError as e:
            print(e)

    return inner
