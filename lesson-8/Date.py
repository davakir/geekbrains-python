import time
import datetime


class Date:
    """
    Date should be in the following format: 'yyyy-mm-dd'
    """
    def __init__(self, date: str):
        self.__date = date

    @property
    def date(self):
        try:
            Date.validate_date(self.__date)
        except ValueError as error:
            print(error)
            exit(1)
        else:
            return self.__date

    @classmethod
    def date_to_timestamp(cls, date: str):
        date = Date(date).date
        return int(time.mktime(datetime.datetime.strptime(date, '%Y-%m-%d').timetuple()))

    @staticmethod
    def validate_date(date):
        splitted_date = date.split('-')
        if len(splitted_date[0]) != 4 \
                or len(splitted_date[1]) != 2 or int(splitted_date[1]) < 1 or int(splitted_date[1]) > 12 \
                or len(splitted_date[2]) != 2 or int(splitted_date[2]) < 1 or int(splitted_date[2]) > 31:
            raise ValueError('Given date is incorrect')


print(Date.date_to_timestamp('2020-02-28'))
