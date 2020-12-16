last_day_from_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def add_days(self, days):
        self.day += days
        while self.day > last_day_from_month[self.month]:
            self.day -= last_day_from_month[self.month]
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1

    def get_date(self):
        return f"{self.day:0>2}/{self.month:0>2}/{self.year}"


year = int(input("Ano: "))
month = int(input("Mês: "))
day = int(input("Dia: "))

d = Date(year, month, day)

print(f"Data digitada: {d.get_date()}")

days_to_sum = int(input("Dias a somar: "))
d.add_days(days_to_sum)

print(f"Nova data: {d.get_date()}")
