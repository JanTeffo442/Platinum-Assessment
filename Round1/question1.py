from datetime import datetime

def is_date_format_correct(date:str) -> bool:

    date_input = input("Enter date in the format YYYY-MM-DD")

    try:
        date_format = datetime.strptime(date_input, '%Y-%m-%d')
        print(date_input, bool(format(date_input)))

    except ValueError:
        print(date_input, 'False'.format(date_input))

if __name__ == '__main__':
    is_date_format_correct('1989-12-14')


