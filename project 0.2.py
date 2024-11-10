# Define the list of authorized vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Function to print the list of authorized vehicles
def print_vehicles():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

# Function to search for a vehicle in the allowed list
def search_vehicle():
    # Ask user for vehicle name
    vehicle_to_search = input("Please Enter the full Vehicle name: ").strip()

    # Search for the vehicle in the list
    if vehicle_to_search in AllowedVehiclesList:
        print(f"{vehicle_to_search} is an authorized vehicle")
    else:
        print(f"{vehicle_to_search} is not an authorized vehicle, if you received this in error please check the spelling and try again")

# Function to display the main menu and handle user input
def menu():
    while True:
        print("********************************")
        print("AutoCountry Vehicle Finder v0.2")
        print("********************************")
        print("Please Enter the following number below from the following menu:\n")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. Exit")
        
        # Get user input
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        
        if choice == "1":
            print_vehicles()
        elif choice == "2":
            search_vehicle()
        elif choice == "3":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid choice, please enter 1, 2, or 3.")

# Start the program
menu()
