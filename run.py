import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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

    while True:
        
        print("Please enter occupancy data from the last day.")
        print("The figures entered should be 6 numbers, seperated by comas.")
        print("Example: 10,20,30,40,50,60")

        occupancy_str = input("Enter the ocupancy data here: ")
    
        occupancy_data = occupancy_str.split(",")
        vailidate_data(occupancy_data)

        if vailidate_data(occupancy_data):
            print("Occupancy Data is valid")
            break

    return occupancy_data

def vailidate_data(values):
    """
    Converting strings to integers.
    Validating the data entered where string cannot be converted to int
    and if it cant be converted referring it back to ask to re-enter
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 5 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid occupancy data: {e}, please try again.\n")
        return False
    
    return True


def update_occupancy_worksheet(data):
    """
    Update the occupancy worksheet, adds new row with the list data provided
    """
    print("Updating occupancy sheet...\n")
    occupancy_sheet = SHEET.worksheet("occupancy")
    occupancy_sheet.append_row(data)
    print("Occupancy sheet updated succesfully!\n")

def update_linen_worksheet(data):
    """
    Update the linen used worksheet, adds new row with the list data provided
    """
    print("Updating linen sheet...\n")
    linen_sheet = SHEET.worksheet("linen_used")
    linen_sheet.append_row(data)
    print("Linen sheet updated succesfully!\n")

def calculate_single(single_row):
    """
    calculate single room linen used
    """
    single_guide = SHEET.worksheet("single").get_all_values()
    single_info = single_guide[1]
    
    linen_data_single = []
    for linen, occupancy in zip(single_info, single_row):
        linen_single = int(linen) * occupancy
        linen_data_single.append(linen_single)
    return linen_data_single

def calculate_twin(twin_row):
    """
    calculate twin room linen used
    """
    twin_guide = SHEET.worksheet("twin").get_all_values()
    twin_info = twin_guide[1]
    
    linen_data_twin = []
    for linen, occupancy in zip(twin_info, twin_row):
        linen_twin = int(linen) * occupancy
        linen_data_twin.append(linen_twin)
    return linen_data_twin

def calculate_double(double_row):
    """
    calculate double room linen used
    """
    double_guide = SHEET.worksheet("double").get_all_values()
    double_info = double_guide[1]

    linen_data_double = []
    for linen, occupancy in zip(double_info, double_row):
        linen_double = int(linen) * occupancy
        linen_data_double.append(linen_double)
    return linen_data_double

def calculate_triple(triple_row):
    """
    calculate triple room linen used
    """
    triple_guide = SHEET.worksheet("triple").get_all_values()
    triple_info = triple_guide[1]

    linen_data_triple = []
    for linen, occupancy in zip(triple_info, triple_row):
        linen_triple = int(linen) * occupancy
        linen_data_triple.append(linen_triple)
    return linen_data_triple

def calculate_family(family_row):
    """
    calculate family room linen used
    """
    family_guide = SHEET.worksheet("family").get_all_values()
    family_info = family_guide[1]

    linen_data_family = []
    for linen, occupancy in zip(family_info, family_row):
        linen_family = int(linen) * occupancy
        linen_data_family.append(linen_family)
    return linen_data_family

def calculate_suite(suite_row):
    """
    calculate family room linen used
    """
    suite_guide = SHEET.worksheet("suite").get_all_values()
    suite_info = suite_guide[1]

    linen_data_suite = []
    for linen, occupancy in zip(suite_info, suite_row):
        linen_suite = int(linen) * occupancy
        linen_data_suite.append(linen_suite)
    return linen_data_suite

def add_linen_togther(a, b):
    """
    adds linen figures together
    """
    compile_linen_figure = []
    for linenone, linentwo in zip(a, b):
        linen_figure = linenone + linentwo
        compile_linen_figure.append(linen_figure)
    return compile_linen_figure

def calculate_new_linen(new_linen):
    """
    runs the calculate new linen fucntions
    """
    print("Calculating Linen Used.\n")
    
    single_linen_used = calculate_single(new_linen)
    twin_linen_used = calculate_twin(new_linen)
    double_linen_used = calculate_double(new_linen)
    triple_linen_used = calculate_triple(new_linen)
    family_linen_used = calculate_family(new_linen)
    suite_linen_used = calculate_suite(new_linen)
    linen_figure_one = add_linen_togther(single_linen_used, twin_linen_used)
    linen_figure_two = add_linen_togther(linen_figure_one, double_linen_used)
    linen_figure_three = add_linen_togther(linen_figure_two, triple_linen_used)
    linen_figure_four = add_linen_togther(linen_figure_three, family_linen_used)
    total_linen_used = add_linen_togther(linen_figure_four, suite_linen_used)
    return total_linen_used

    

def main():
    """
    Run all program functions
    """
    data = get_occupancy_data()
    occupancy_data = [int(num) for num in data]
    update_occupancy_worksheet(occupancy_data)
    new_linen_used = calculate_new_linen(occupancy_data)
    print("New Linen Calculated\n")
    print(new_linen_used)
    update_linen_worksheet(new_linen_used)

print("Welcome to the hotel automated Linen Stock System\n")
main()
