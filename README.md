# A Hotel Linen Sheet Record

An automated linen update sheet that will calculate and do math on behalf of the user to save time.
The hotel user can print the daily occupancy and enter it into the automated system for it to calculate the 
amount of linen used and then produce an order to be sent off based on the last 7 day average.

[Here is the live version of my project]()

[image]

## How to Use

The automated linen sheet completes a task that can be done by the user but is designed; to reduce the time 
needed to complete the task.
The user on clicking run is prompted to enter in the occupancy figures it needs to run the calculations.
It then updates the external google sheet, and then performs the main calculation.
It pulls the linen per room type numbers from the sheet then works out the linen used agaisnt the occupancy entered.
It then asks the user if it is an order day, which if answered yes will also work out the 7 day average.

## Features

 * ### Existing Features
    * Occupancy data entry
        * Accepts input from user that accepts 6 numbers correlating to hotel room types.
        * This data is validated to make sure it is entered in the correct format
        * This data is then updated to the external Google Sheet

    [image]

    * Linen Useage calculation
        * The occupancy data is then used to calculate how much linen has been used. 
        * It takes the room type information from the google sheet and uses this to calculate.
        * It takes the input given and the room type data to work out linen used.

    [image]

    * Linen order request
        * The user is then prompted to decalre via input if it is an order day.
        * Based on the user answer it will then end the automation or generate an order
        * This order is then uploaded to the external google sheet.

    [image]
    
 * ### Future Features
    * Further connecting sheets to allow for linen order to be sent straight to linen company
    * Further option to have input for any additional linen used

## Data
The data used is taken from user or drawn from google sheets using API. The sheet is set up with permisison for the app to
access and update the sheets with editor permission using credentials generated.

The sheets store the data the user inputs, the linen used and the order.
The sheet also draws information to perform its calculation from the room type worksheets.

## Testing


### Bugs

### Remaining Bugs


### Validator Testing

* PEP8
    * 11 errors thrown up to do with blank lines and lines being too long.
        * 18: E302 expected 2 blank lines, found 1
        * 40: E302 expected 2 blank lines, found 1
        * 80: E302 expected 2 blank lines, found 1
        * 94: E302 expected 2 blank lines, found 1
        * 183: E302 expected 2 blank lines, found 1
        * 197: E302 expected 2 blank lines, found 1
        * 211: E501 line too long (80 > 79 characters)
        * 215: E302 expected 2 blank lines, found 1
        * 230: E302 expected 2 blank lines, found 1
        * 245: E302 expected 2 blank lines, found 1
        * 266: E302 expected 2 blank lines, found 1
    * None of the errors show or seem to have an impact on the code running.



## Deployment
This project was deployed using Code Institute's mock terminal for Heroku

* Steps for deployment
    * Create google sheet and set up API for google drive and google sheet in that order
    * Download Credentials
    * Fork or clone this repository 
    * Add credentials to repository and add creds to the ignore file
    * take email from creds file and using google sheet share it and give editor permission
    * Create a new Heroku app
    * Set the buildbacks to python and NodeJS in that order
    * Link the heroku app to the repository
    * Click on Deploy

## Credits

* Code Institute for the deployment terminal
* The love sandwiches project for the following code
    * def vailidate_data
    * def update_worksheet