from datetime import date, datetime, timedelta


def get_birthdays_per_week(all_users):

    WEEK_DAYS = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday',
    }

    users = {"Monday": [], "Tuesday": [], "Wednesday": [],
             "Thursday": [], "Friday": []}

    current_date = date.today()
    next_week_date = current_date + timedelta(days=7)

    for user in all_users:

        date_ = user['birthday']

        user_month = date_.month

        user_day = date_.day
        user_birthday = date(
            current_date.year, user_month, user_day)
        print('30', current_date, user_birthday, next_week_date)
        delta = user_birthday - current_date
        if delta.days < 0:
            user_birthday = date(
                current_date.year + 1, user_month, user_day)
            print("32")
        delta = user_birthday - current_date
        if delta.days < 7:
            weekday_user = user_birthday.weekday()

            if weekday_user in ('Sunday', 'Saturday'):
                pass

            else:
                users[WEEK_DAYS[weekday_user]].append(
                    user['name'].split(' ')[0])

    for weekday, user in list(users.items()):
        if not user:
            del users[weekday]
    print(users)
    return users


if __name__ == '__main__':

    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 11, 25).date()},
        {"name": "Al Pach", "birthday": datetime(1956, 12, 26).date()},
        {"name": "Foma Kiniaev", "birthday": datetime(1969, 12, 29).date()},
        {"name": "not Bill Gates", "birthday": datetime(1955, 12, 28).date()},
        {"name": "not Al Pach", "birthday": datetime(1956, 12, 29).date()},
        {"name": "not Foma Kiniaev", "birthday": datetime(1969, 1, 2).date()},
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)

    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
