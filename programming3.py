import re

# function to check phone number
def check_phone(phone):

    pattern = r"\d{3}-\d{3}-\d{4}"

    if re.fullmatch(pattern, phone):
        return True
    else:
        return False


# function to check social security number
def check_ssn(ssn):

    pattern = r"\d{3}-\d{2}-\d{4}"

    if re.fullmatch(pattern, ssn):
        return True
    else:
        return False


# function to check zip code
def check_zip(zip_code):

    pattern = r"\d{5}(-\d{4})?"

    if re.fullmatch(pattern, zip_code):
        return True
    else:
        return False


def main():

    print("Validation Program\n")

    phone = input("Enter a phone number (XXX-XXX-XXXX): ")
    ssn = input("Enter a Social Security Number (XXX-XX-XXXX): ")
    zip_code = input("Enter a ZIP Code (XXXXX or XXXXX-XXXX): ")

    print("\nResults:")

    if check_phone(phone):
        print("Phone number is valid")
    else:
        print("Phone number is invalid")

    if check_ssn(ssn):
        print("SSN is valid")
    else:
        print("SSN is invalid")

    if check_zip(zip_code):
        print("ZIP code is valid")
    else:
        print("ZIP code is invalid")


# run the program
main()