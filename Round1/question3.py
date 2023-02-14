import datetime

def compute_prev_date(date_list:list):

    dates_list = []

    for date in date_list:
        current_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        previous_date = current_date - datetime.timedelta(days=1)
        dates_list.append(previous_date.strftime('%d %b %Y'))
    return dates_list

if __name__ == '__main__':
    print(compute_prev_date(['2023-02-14', '2023-01-01']))



