import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hotel_linen_sheet_record')

def get_occupancy_data():
    """
    Get occupancy figures from the user
    """
    print("Please enter occupancy data from the last day.")
    print("The figures entered should be 5 numbers, seperated by comas.")
    print("Wxample: 10,20,30,40,50")

    occupancy_str = input("Enter the ocupancy data here: ")
    
    occupancy_data = occupancy_str.split(",")
    vailidate_data(occupancy_data)

def vailidate_data(values):
    """
    Converting strings to integers.
    Validating the data entered where string cannot be converted to int
    and if it cant be converted referring it back to ask to re-enter
    """
    try:
        if len(values) != 5:
            raise ValueError(
                f"Exactly 5 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid occupancy data: {e}, please try again.\n")

get_occupancy_data()