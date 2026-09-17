
from datetime import datetime, timedelta


def get_dates(date_str, amount, skip):
    start_date = datetime.strptime(date_str, "%d/%m/%Y")

    return list(
        map(
            lambda i: (
                start_date + timedelta(days=i * skip)
            ).strftime("%d/%m/%Y"),
            range(amount)
        )
    )



