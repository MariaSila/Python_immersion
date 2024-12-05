from datetime import datetime, timedelta


def manager_tasks(days: int) -> datetime.date:
    cur_date = datetime.now()
    new_date = cur_date + timedelta(days)
    return new_date.strftime('%Y-%m-%d')


if __name__ == '__main__':
    print(manager_tasks(25))
