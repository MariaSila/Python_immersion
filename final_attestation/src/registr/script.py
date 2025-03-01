from exceptions import UserException
from menu import Menu

if __name__ == '__main__':
    try:
        Menu()
    except UserException as e:
        print(e)