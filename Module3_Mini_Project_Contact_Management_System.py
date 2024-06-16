# Contact Management System

# import re

contacts = {} # Empty dictionary

def main():
    while True: # Welcome screen with Menu for the user to pick
        input1 = input(''' 
Welcome to the Contact Management System

Menu:

1- Add a new contact
2- Edit an existing contact
3- Delete a contact
4- Search for a contact
5- Display all contacts
6- Import contacts from a text file
7- Quit
                       
 ''')
        if input1 == "1": # If user inputs 1 user can add contacts to the empty dictionary
            add()
        elif input1 == "2": # If user inputs 2 user can edit a contact
            edit()
        elif input1 == "3": # If user inputs 3 user can delete a contact
            delete()
        elif input1 == "4": # If user inputs 4 user can search through contacts
            search()
        elif input1 == "5": # If user inputs 5 it will print contact dictionary
            display()
        elif input1 == "6": # If user inputs 6 it will import contacts from a text file and adding them to the system
            import_contacts()
        elif input1 == "7": # If user inputs 7 it will end the Contact Management System
            break
        else:
            print("Please enter a valid input") # If user inputs any other number other than 1-8 it will print please enter a valid input
            continue

def add(): # Obtains contact information from the user
    unique_id = input("Enter unique ID (phone number or email): ")
    name = input("Enter the contacts name: ")
    phone_number = input("Enter the contacts phone number: ")
    email_address = input("Enter the contacts email address: ")
    additional_info = input("Enter additional info (e.g., address, notes): ")

# Stores the contacts information in nested dictionary
    contacts[unique_id] = {
    "name": name, 
    "phone_number": phone_number,
    "email_address": email_address,
    "additional_info": additional_info, 
    }

# Exports contacts to a new text file through user input automatically
    with open('contacts.txt', 'w') as file:
        for unique_id, info in contacts.items():
            file.write(f"{unique_id}-:-{info["name"]}-:-{info["phone_number"]}-:-{info["email_address"]}-:-{info["additional_info"]}\n")

# def valid_contacts(contacts):
#     name_val = re.compile (r'^[a-zA-Z\s]*$')
#     phone_val = re.compile (r'^\d{3}-\d{3}-\d{4}$') 
#     email_val = re.compile (r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

#     for unique_id, info in contacts.items():
#         if not name_val.match(info['name']):
#             print(f"Invalid name in contact ID {unique_id}.")
#         elif not phone_val.match(info["phone_number"]):
#             print(f"Invalid phone number in contact ID {unique_id}.")
#         elif not email_val.match(info['email_address']):
#             print(f"Invalid email address in contact ID {unique_id}.")
#         else:
#             print(f"All contact information is valid for contact ID {unique_id}.")
            
# valid_contacts(contacts)


# import re

# name_val = re.compile (r'^[a-zA-Z\s]*$')
# phone_val = re.compile (r'^\d{3}-\d{3}-\d{4}$') 
# email_val = re.compile (r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

# for unique_id, info in contacts.items():
#     if not name_val.match(info['name']):
#         print(f"Invalid name in contact ID {unique_id}.")
#     elif not phone_val.match(info["phone_number"]):
#         print(f"Invalid phone number in contact ID {unique_id}.")
#     elif not email_val.match(info['email_address']):
#         print(f"Invalid email address in contact ID {unique_id}.")
#     else:
#         print(f"All contact information is valid for contact ID {unique_id}.")


def edit():
    unique_id = input("Enter unique ID (phone number or email) of the contact you want to edit: ")
    if unique_id in contacts:
        update = input("Enter the key that needs updated (name, phone_number, email_address, additional_info): ")
        new_value = input("Enter the new value for the key: ")
        [*update] = new_value
    else:
        print("Unable to find contact")
    
    print(contacts)

def delete():
    while True: # Asks the user for the unique ID of the contact wanting to delete
        unique_id = input("Enter the unique ID (phone number or email) of the contact you want to delete: ")
        if unique_id in contacts: # If the unique ID is in the contacts dictionary
            del contacts[unique_id] # It will delete the contact and print Contact has been deleted
            print("Contact has been deleted")
            return
        else:
            print("Contact not found") #If contact is not found in the contact dictionary with unique ID entered it will print Contact not found and then gives the user the option to re-input the unique or quit to go back to the menu
            print("Please enter valid unique ID or enter quit to go back to menu")
            if unique_id.lower() == "quit": # If user inputs quit it goes back to the menu
                break
        
        
def search(): # Asks user for the unique ID of the contact that user wants to search for
    unique_id = input("Enter the unique ID (phone number or email) of the contact you want to search for: ")
    if unique_id in contacts: # If the unique ID is in the contacts it will prints Contact found
        print("Contact found") 
        print(contacts[unique_id]) # Print contacts information
    else:
        print("Contact not found") # If the contact is not found in contact dictionary it will print contact not found
        return main()

def display():
    print("Original Dictionary : " + str(contacts)) # Displays oiginal dictionary not being sorted
    remaining = sorted(contacts.items(), key = lambda item: item[1]['name']) # Sorts the dictionary by name of the contact
    print("The sorted dictionary by name is :" + str(remaining)) # Prints the sorted dictionary
   
def import_contacts():
    with open("contacts.txt", "r") as file: # Opens the contacts txt file
        for line in file: # Imports contacts from a text file and adds them to the system
            unique_id, name, phone_number, email_address, additional_info = line.strip().split('-:-')
            contacts[unique_id] = {'Name': name, "Phone_Number": phone_number, "Email_address": email_address, "Additional_info": additional_info}
        print(contacts)


main()