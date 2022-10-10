from get_recent_data_by_name import get_recent_data_by_name


def get_performance_streak(stockname: str):
    recent_data = get_recent_data_by_name(stockname)
    number = 0
    trend = "?"
    for item in recent_data[::-1].itertuples(index=False):
        if item._5 > 0:
            break  # break here
        number += 1
        trend = "falling"

    for item in recent_data[::-1].itertuples(index=False):
        if item._5 < 0:
            break  # break here
        number += 1
        trend = "rising"

    data = {"trend": trend, "streak": number}

    return data
