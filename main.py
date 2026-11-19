from calendar import TextCalendar

def show_calendar():
    choose_year = input("""Choose year:
    1. 2030      6. 2025     11. 2020     16. 2015     21. 2010
    2. 2029      7. 2024     12. 2019     17. 2014    
    3. 2028      8. 2023     13. 2018     18. 2013
    4. 2027      9. 2022     14. 2017     19. 2012
    5. 2026     10. 2021     15. 2016     20. 2011
    """)
    choose_month = input("""
    1. January    5. May      9. September
    2. February   6. June    10. October
    3. March      7. July    11. November
    4. April      8. August  12. December
    """)

    if (choose_year == "1") and (choose_month == "1"):
        print(TextCalendar(2030, 1))

    return 0

print(show_calendar())