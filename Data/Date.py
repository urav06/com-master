import copy


class Date:
    MIN_DAY = 1
    MIN_MONTH = 1
    MAX_MONTH = 12
    MONTH_TABLE = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7, "august": 8,
                   "september": 9, "october": 10, "november": 11, "december": 12}

    def get_max_days(self, month=None, year=None):
        """
        Returns the max number of days for the month

        :param month: The month (Optional)
        :param year: The year (Optional)
        :return: The number of days in the given month
        """
        if month is None:
            month = self.month

        if year is None:
            year = self.year

        non_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        isleap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
        if isleap:
            index = month - 1
            return leap[index]
        else:
            index = month - 1
            return non_leap[index]

    def __init__(self, date="01/06/2000"):

        date = date.split("/")
        try:
            day = int(date[0])
            month = int(date[1])
            year = int(date[2])
        except IndexError:
            raise Exception("Invalid date input. Follow format DD/MM/YYYY")
        except ValueError:
            raise Exception("Invalid date input. Use numbers only")

        if not (self.MIN_MONTH <= month <= self.MAX_MONTH):
            raise Exception("Month invalid. Input: {}. Expected between {} and {}".format(month, Date.MIN_MONTH,
                                                                                          Date.MAX_MONTH))

        if not (self.MIN_DAY <= day <= self.get_max_days(month, year)):
            raise Exception("Day invalid. Input: {}. Expected between {} and {}".format(day, Date.MIN_DAY,
                                                                                        self.get_max_days(month, year)))

        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{day}/{month}/{year}".format(day=self.day, month=self.month, year=self.year)

    @staticmethod
    def add_months(initial, months):
        """
        Adds the number of months to a date and returns it

        :param initial: the initial date
        :param months: the number of months to add
        :return: the date after addition is done
        """
        final = copy.deepcopy(initial)
        for i in range(months):
            if final.month < Date.MAX_MONTH:
                final.month += 1
            elif final.month == Date.MAX_MONTH:
                final.month = Date.MIN_MONTH
                final.year += 1
        return final
