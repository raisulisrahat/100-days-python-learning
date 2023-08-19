# Here is am showing Practising Day 24 in python

# RegEx Built-In Modules

import re

def extract_dates(text):
    date_pattern = r'\d{2}-\d{2}-\d{4}'
    dates = re.findall(date_pattern, text)
    return dates

def main():
    print("Welcome to the Date Extractor!")

    text = input("Enter some text containing dates: ")

    dates = extract_dates(text)

    if dates:
        print("Dates found:")
        for date in dates:
            print(date)
    else:
        print("No dates found in the input.")

if __name__ == "__main__":
    main()
