#!/usr/bin/env python
from datetime import date
from calendar import TextCalendar

today = date.today()

text_calendar = TextCalendar()  # <1>
print(text_calendar.formatmonth(today.year, today.month))  # <2>

