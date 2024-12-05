from datetime import time, date, datetime


def current_date():
    cur_date = datetime.now()
    print(cur_date.strftime('%Y-%m-%d %H:%M:%S %A, %W неделя'))


if __name__ == '__main__':
    current_date()
