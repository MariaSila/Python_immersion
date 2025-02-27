import main
from exceptions import UserException

if __name__ == '__main__':
    try:
        main.main()
    except UserException as e:
        print(e)