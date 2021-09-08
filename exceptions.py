from fastapi import HTTPException


class InvalidDimensionException(Exception):
    pass


class EmptyArrayException(Exception):
    pass


def handle_server_exceptions(func):
    def wrapper():
        try:
            func()
        except (HTTPException, ) as e:
            print(e)

    return wrapper
