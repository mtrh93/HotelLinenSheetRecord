import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

# connection between python and google sheet
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hotel_linen_sheet_record')

# retrieve occupacy data request

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

#validates if data entered is valid
#code used is from the love_sandwiches project

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

#code updates the occupancy worksheet of the google sheet

#def update_occupancy_worksheet(data):
#    """
#    Update the occupancy worksheet, adds new row with the list data provided
#    """
#    print("Updating occupancy sheet...\n")
#    occupancy_sheet = SHEET.worksheet("occupancy")
#    occupancy_sheet.append_row(data)
#    print("Occupancy sheet updated succesfully!\n")

#def update_linen_worksheet(data):
#    """
#    Update the linen used worksheet, adds new row with the list data provided
#    """
#    print("Updating linen sheet...\n")
#    linen_sheet = SHEET.worksheet("linen_used")
#    linen_sheet.append_row(data)
#    print("Linen sheet updated succesfully!\n")

#refactored code updates the passed worksheet on the google sheet
#code used is from the love sandwiches walkthrough

def update_worksheet(data, worksheet):
    """
    Update the worksheet passed through the function, adds new row with the list data provided
    """
    print(f"Updating {worksheet} sheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} sheet updated succesfully!\n")

#code that overall takes the occupancy data and calculates how much linen has been used

#refactored code that calculates linen
def calculate_linen(linen_row, room_type):
    """
    calculate room linen used
    """
    linen_guide = SHEET.worksheet(room_type).get_all_values()
    linen_info = linen_guide[1]
    print(f"calculating {room_type} linen used")
    linen_data = []
    for linen, occupancy in zip(linen_info, linen_row):
        linen_type = int(linen) * occupancy
        linen_data.append(linen_type)
    return linen_data

#def calculate_single(single_row):
#    """
#    calculate single room linen used
#    """
#    single_guide = SHEET.worksheet("single").get_all_values()
#    single_info = single_guide[1]
#    
#    linen_data_single = []
#    for linen, occupancy in zip(single_info, single_row):
#        linen_single = int(linen) * occupancy
#        linen_data_single.append(linen_single)
#    return linen_data_single

#def calculate_twin(twin_row):
#    """
#    calculate twin room linen used
#    """
#    twin_guide = SHEET.worksheet("twin").get_all_values()
#    twin_info = twin_guide[1]
#    
#    linen_data_twin = []
#    for linen, occupancy in zip(twin_info, twin_row):
#        linen_twin = int(linen) * occupancy
#        linen_data_twin.append(linen_twin)
#    return linen_data_twin

#def calculate_double(double_row):
#    """
#    calculate double room linen used
#    """
#    double_guide = SHEET.worksheet("double").get_all_values()
#    double_info = double_guide[1]
#
#    linen_data_double = []
#    for linen, occupancy in zip(double_info, double_row):
#        linen_double = int(linen) * occupancy
#        linen_data_double.append(linen_double)
#    return linen_data_double

#def calculate_triple(triple_row):
#    """
#    calculate triple room linen used
#    """
#    triple_guide = SHEET.worksheet("triple").get_all_values()
#    triple_info = triple_guide[1]
#
#    linen_data_triple = []
#    for linen, occupancy in zip(triple_info, triple_row):
#        linen_triple = int(linen) * occupancy
#        linen_data_triple.append(linen_triple)
#    return linen_data_triple

#def calculate_family(family_row):
#    """
#    calculate family room linen used
#    """
#    family_guide = SHEET.worksheet("family").get_all_values()
#    family_info = family_guide[1]
#
#    linen_data_family = []
#    for linen, occupancy in zip(family_info, family_row):
#       linen_family = int(linen) * occupancy
#        linen_data_family.append(linen_family)
#    return linen_data_family

#def calculate_suite(suite_row):
#    """
#    calculate family room linen used
#    """
#    suite_guide = SHEET.worksheet("suite").get_all_values()
#    suite_info = suite_guide[1]
#
#    linen_data_suite = []
#    for linen, occupancy in zip(suite_info, suite_row):
#        linen_suite = int(linen) * occupancy
#        linen_data_suite.append(linen_suite)
#    return linen_data_suite

def add_linen_togther(a, b):
    """
    adds linen figures together
    """
    compile_linen_figure = []
    for linenone, linentwo in zip(a, b):
        linen_figure = linenone + linentwo
        compile_linen_figure.append(linen_figure)
    return compile_linen_figure

#code that runs all the calculate linen functions
#each rom type is pulled seperately from sheet so that linen numbers can be adjusted

def calculate_new_linen(new_linen):
    """
    runs the calculate new linen fucntions
    """
    print("Calculating Linen Used.\n")
    
    single_linen_used = calculate_linen(new_linen, "single")
    twin_linen_used = calculate_linen(new_linen, "twin")
    double_linen_used = calculate_linen(new_linen, "double")
    triple_linen_used = calculate_linen(new_linen, "triple")
    family_linen_used = calculate_linen(new_linen, "family")
    suite_linen_used = calculate_linen(new_linen, "suite")
    linen_figure_one = add_linen_togther(single_linen_used, twin_linen_used)
    linen_figure_two = add_linen_togther(linen_figure_one, double_linen_used)
    linen_figure_three = add_linen_togther(linen_figure_two, triple_linen_used)
    linen_figure_four = add_linen_togther(linen_figure_three, family_linen_used)
    total_linen_used = add_linen_togther(linen_figure_four, suite_linen_used)
    return total_linen_used

    return order_data


def order_day():
    """
    Get answer to question yes or no for is it a day to order
    """
    while True: 
        print("Is today a day where you order linen?")
        print("Please enter yes or no")

        answer = input("Enter yes or no here")
    
        vailidate_answer(answer)

        if vailidate_answer(answer):
            print("Answer is valid")
            break
    return answer


def validate_answer(answered):
    try:
        if answered != 'yes' or 'no':
            raise ValueError(
                f"Exactly 5 values required, you provided {(answered)}"
            )
    except ValueError as e:
        print(f"Invalid occupancy data: {e}, please try again.\n")
        return False
    return True

#main core that runs all functions

def main():
    """
    Run all program functions
    """
    data = get_occupancy_data()
    occupancy_data = [int(num) for num in data]
    update_worksheet(occupancy_data, "occupancy")
    new_linen_used = calculate_new_linen(occupancy_data)
    print("New Linen Calculated\n")
    print(new_linen_used)
    update_worksheet(new_linen_used, "linen_used")
    order_day_answer = order_day()

print("Welcome to the hotel automated Linen Stock System\n")
main()
