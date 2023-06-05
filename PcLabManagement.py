import json

# Initializing an empty dictionary to store all PC details
pc_details = {}

# Loading existing PC details from text file if present
try:
    with open('pc_details.txt', 'r') as file:
        pc_details = json.load(file)
except FileNotFoundError:
    pass


def add_pc():
    # Function to add a new PC
    pc_num = input("Enter PC number: ")
    if pc_num in pc_details:
        print("This PC number already exists.")
        choice = input("Do you want to modify information of this existing PC (m), remove this PC (r), or no action (n)? ")
        if choice == 'm':
            update_pc(pc_num)
        elif choice == 'r':
            remove_pc(pc_num)
    else:
        os = input("Enter operating system installed: ")
        status = input("Enter PC status: ")
        pc_details[pc_num] = {'Operating System': os, 'Status': status}
        print("PC added successfully.")


def update_pc(pc_num):
    # Function to update PC information
    os = input("Enter new operating system installed: ")
    status = input("Enter new PC status: ")
    pc_details[pc_num] = {'Operating System': os, 'Status': status}
    print("PC information updated successfully.")


def remove_pc(pc_num):
    # Function to remove a PC
    del pc_details[pc_num]
    print("PC removed successfully.")


def display_all_pc():
    # Function to display all PC information
    if not pc_details:
        print("No PC details available.")
    else:
        print("PC Number\tOperating System\tStatus")
        for pc_num, details in pc_details.items():
            print(f"{pc_num}\t\t{details['Operating System']}\t\t{details['Status']}")


def display_pc(pc_num):
    # Function to display individual PC information
    if pc_num not in pc_details:
        print("PC not found.")
    else:
        print(f"PC Number: {pc_num}")
        for key, value in pc_details[pc_num].items():
            print(f"{key}: {value}")


def search_pc():
    # Function to search for a PC
    pc_num = input("Enter PC number to search: ")
    if pc_num in pc_details:
        display_pc(pc_num)
    else:
        choice = input("PC not found. Do you want to add this PC (y/n)? ")
        if choice == 'y':
            add_pc()

"""
def store_pc_details():
    # Function to store PC details in text file
    with open('pc_details.txt', 'w') as file:
        json.dump(pc_details, file)
    print("PC details stored successfully.")
"""

def store_pc_details():
     # Function to store PC details in text file
    filepath = input("Enter the path where you want to save the file: ")
    filename = "pc_details.txt"
    fullpath = os.path.join(filepath, filename)
    with open(fullpath, 'w') as file:
        json.dump(pc_details, file)
    print("PC details stored successfully.")
    #D:\AIUB\10th\Python



while True:
    # Main program loop
    print("\nPlease select an option:")
    print("1. Add a new PC")
    print("2. Update information of an existing PC")
    print("3. Remove an existing PC from the lab")
    print("4. Display information about all the PCs")
    print("5. Display information about a particular PC")
    print("6. Search for a particular PC")
    print("7. Store all PC information to a text file")
    print("8. Quit the program")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        add_pc()
    elif choice == "2":
        pc_num = input("Enter PC number to update: ")
        update_pc(pc_num)
    elif choice == "3":
        pc_num = input("Enter PC number to remove: ")
        remove_pc(pc_num)
    elif choice == "4":
        display_all_pc()
    elif choice == "5":
        pc_num = input("Enter PC number to show: ")
        display_pc(pc_num)
    elif choice == "6":
        search_pc()
    elif choice == "7":
        store_pc_details()
    elif choice == "8":
        print("Thank you for using the lab management system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

