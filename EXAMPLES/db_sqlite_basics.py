#!/usr/bin/env python
import csv
import json
import sqlite3

#                    ":memory:"
with sqlite3.connect("../DATA/presidents.db") as conn:  # <1>

    cursor = conn.cursor()  # <2>

    # select first name, last name from all presidents
    cursor.execute('''
        select firstname, lastname, birthplace, birthstate, party
        from presidents
    ''')  # <3>

    print("Sqlite3 does not provide a row count\n")  # <4>

    first_potus = cursor.fetchone()
    print(f"first_potus: {first_potus}")

    next_4 = cursor.fetchmany(4)
    print(f"next_4: {next_4}")
    print()

    with open('potus.csv', 'w') as potus_out:
        wtr = csv.writer(potus_out)
        for row in cursor.fetchall():  # <5>
            print(row)
            wtr.writerow(row)

    cursor.execute('''
        select firstname, lastname, birthplace, birthstate, party
        from presidents
    ''')  # <3>

    with open('potus.json', 'w') as potus_out:
        json.dump(cursor.fetchall(), potus_out, indent=4)


