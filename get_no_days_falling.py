from get_recent_data_by_name import get_recent_data_by_name


def get_no_days_falling(stockname: str):
    recent_data = get_recent_data_by_name(stockname)
    number = 0
    for tuple in recent_data[::-1].itertuples(index=False):
        if tuple._5 > 0:
            break  # break here
        number += 1

    return number