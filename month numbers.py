def days_in_month():
    month = int(input("Enter month number (1-12): "))

    # 30 days: April(4), June(6), September(9), November(11)
    # 31 days: Jan(1), Mar(3), May(5), July(7), Aug(8), Oct(10), Dec(12)
    # 28/29 days: Feb(2)
    
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            print("31 days")
        case 4 | 6 | 9 | 11:
            print("30 days")
        case 2:
            print("28 or 29 days (depending on leap year)")
        case _:
            print("Invalid month number. Please enter a value between 1 and 12.")

days_in_month()
