def menu():
    print("Options list:")
    print("1- Scrape data.")
    print("2- Save data to CSV.")
    print("0- Exit")
    selection = int(input("Insert your desired function: "))
    while selection < 0 or selection > 2:
        selection = int(input("Invalid option. Please select again: "))
    return selection