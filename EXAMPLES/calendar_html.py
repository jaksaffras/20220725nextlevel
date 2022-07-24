#!/usr/bin/env python
import os
from datetime import date
from calendar import HTMLCalendar
import webbrowser


current_year = date.today().year

html_calendar = HTMLCalendar()  # <1>
formatted_month = html_calendar.formatyear(current_year)  # <2>

html_file_name = 'calendar_{}.html'.format(current_year)

with open(html_file_name, 'w') as calendar_out:
    calendar_out.write(formatted_month)  # <3>
    webbrowser.open("file://" + os.path.realpath(html_file_name))  # <4>
