from datetime import date, datetime, timedelta


def get_birthdays_per_week(all_users):

    if not all_users:
        return {}

    WEEK_DAYS = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday',
    }
    result = {"Monday": [], "Tuesday": [], "Wednesday": [],
              "Thursday": [], "Friday": [], "Saturday": [], "Sunday": []}

    current_day = date.today()
    next_week_day = current_day + timedelta(days=7)

    for user in all_users:
        user_birthday = user['birthday'].replace(year=current_day.year)

        if user_birthday < current_day:
            user_birthday += timedelta(days=365)

        if user_birthday.weekday() == 5:
            user_birthday += timedelta(days=2)
        elif user_birthday.weekday() == 6:
            user_birthday += timedelta(days=1)

        week_day = WEEK_DAYS[user_birthday.weekday()]

        if current_day <= user_birthday < nex_weed_day:

            result[week_day].append(user['name'].split()[0])

    result_final = {}

    for weekday, user in result.items():
        if user != []:
            result_final[weekday] = user

    return result_final


if __name__ == '__main__':

    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 2, 5).date()},
        {"name": "Al Pach", "birthday": datetime(1956, 2, 7).date()},
        {"name": "Foma Kiniaev", "birthday": datetime(1969, 2, 4).date()},
        {"name": "not Bill Gates", "birthday": datetime(1955, 2, 3).date()},
        {"name": "not Al Pach", "birthday": datetime(1956, 2, 2).date()},
        {"name": "not Foma Kiniaev", "birthday": datetime(1969, 1, 2).date()},
        {"name": "Jan Koum", "birthday": datetime(1976, 2, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
