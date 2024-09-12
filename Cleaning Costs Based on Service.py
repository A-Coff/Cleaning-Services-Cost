# Alex Coffman 29/JUN/23
# CMIS 102/6980 Week 3 Assignment
# This program is designed to take in user inputs for number of rooms and type of cleaning
# it will then calculate total cost to clean based off the fixed cleaning costs and size of house(certain home sizes will be upcharged)

def main():
    print("\nWelcome to Alex's house cleaning service; we provide cleaning services for small, medium, and large homes.")
    print("When prompted, please enter the amount of rooms that require cleaning and the types of cleaning needed.")
    print("\nOur list of services:\nfloors: $10\nwindows: $5\nbathrooms: $25")
    
    numberofRooms = int(input("\nHow many rooms need to be cleaned: "))
    if numberofRooms > 3:
        print("There is a cleaning fee upcharge for medium and large homes.") # up front notice there is an upcharge for medium and large homes
    print("\nCleaning Menu:\nfloors and windows\nfloors and bathrooms\nwindows and bathrooms")
    typeofCleaning = input("\nEnter the type of cleaning from the menu: ")
    
    menu1 = 'floors and windows' # I chose to group the cleaning offerings into menu options becuase I could not get the formula to work when entering typeofCleaning separated by a comma (e.g., floors, windows)
    menu2 = 'floors and bathrooms' # this method got the job done, but I know there should be a more efficient way to get the same results
    menu3 = 'windows and bathrooms'
    floors_price = 10.00    # fixed pricing variables for the individual type of cleaning available
    windows_price = 5.00
    bathrooms_price = 25.00
    total_cost = 0          # total cost starts at 0
    
    if 1 <= numberofRooms <= 3:                 # this is the small sized home(1-3 rooms) cleaning pricing with no additional charges
        if typeofCleaning == menu1:
            total_cost += floors_price * numberofRooms
            total_cost += windows_price * numberofRooms
        elif typeofCleaning == menu2:
            total_cost += floors_price * numberofRooms
            total_cost += bathrooms_price * numberofRooms # I used the plus-equals operator here because I was struggling with having the formula together with parenthesis, this method just does the calculation separately then adds to the total_cost
        elif typeofCleaning == menu3:                       # this was the most time consuming part of the program after figuring all my user input needs and variables. I really struggled with making sure the inputs calculated correclty.
            total_cost += windows_price * numberofRooms
            total_cost += bathrooms_price * numberofRooms
        else:   
            print("We don't provide that service option")
            return
        print("\nYou are being charged the small home pricing") # Informs user that they are being chared for a small home size
    elif 3 < numberofRooms <= 7:                # this is the medium sized home(4-7 rooms) cleaning pricing includes a 1.5x multiplier to the cost
        if typeofCleaning == menu1:
            total_cost += floors_price * numberofRooms
            total_cost += windows_price * numberofRooms
            total_cost *= 1.5
        elif typeofCleaning == menu2:
            total_cost += floors_price * numberofRooms
            total_cost += bathrooms_price * numberofRooms
            total_cost *= 1.5
        elif typeofCleaning == menu3:
            total_cost += windows_price * numberofRooms
            total_cost += bathrooms_price * numberofRooms
            total_cost *= 1.5  # medium sized home cleaning upcharge
        else:   
            print("We don't provide that service option")
            return
        print("\nYou are being charged the medium home pricing") # Informs the user that they will be receiving the medium sized home upcharge
    elif numberofRooms > 7:                     # this is the large sized home(over 7 rooms) cleaning pricing includes a 2x multiplier to the cost
        if typeofCleaning == menu1:
            total_cost += floors_price * numberofRooms
            total_cost += windows_price * numberofRooms
        elif typeofCleaning == menu2:
            total_cost += floors_price * numberofRooms
            total_cost += bathrooms_price * numberofRooms
        elif typeofCleaning == menu3:
            total_cost += windows_price * numberofRooms
            total_cost += bathrooms_price * numberofRooms
            total_cost *= 2 # large sized home cleaning upcharge
        else:   
            print("We don't provide that service option")
            return
        print("\nYou are being charged the large home pricing") # Informs the user that they will be receiving the large sized home upchare
    print("\nThe cost of house cleaning is: $", total_cost) # displays the total cost the user will be charged for number of rooms, type of cleaning, and home upcharge if applicable

        
main()