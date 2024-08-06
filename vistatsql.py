
import mysql.connector as sql  # For connecting sql database and python program
from os import close

from delete import deleteFromCustomer, deleteFromOrder, deleteFromService;
from display import displayCustomerDetails, displayOrderDetails, displayServiceDetails;
from insert import insertDetailsInCustomer, insertDetailsInOrder, insertDetailsInServices;
from search import searchRecInCustomer, searchRecInOrder, searchrecInServices;
from update import updateCustomer, updateOrder, updateService;

from utils.dbConnection import connect_to_db;


from math import e  # In built module for math functions


def submenuForCustomer():
    print("SUBMENU:")
    print("1. Insert customer details")
    print("2. Display customer details")
    print("3. Delete any record")
    print("4. Update any record")
    print("5. Search any record")

    choice = input("Enter your choice: ").lower()

    if choice in ["1", "insert customer details"]:
        insertDetailsInCustomer()
    elif choice in ["2", "display customer details"]:
        displayCustomerDetails()
    elif choice in ["3", "delete any record"]:
        deleteFromCustomer()
    elif choice in ["4", "update any record"]:
        updateCustomer()
    elif choice in ["5", "search any record"]:
        searchRecInCustomer()
    else:
        print("Wrong choice")

def submenuForOrder():
    print("SUBMENU:")
    print("1. Insert order details")
    print("2. Display order details")
    print("3. Delete any record")
    print("4. Update any record")
    print("5. Search any record")

    choice = input("Enter your choice: ").lower()

    if choice in ["1", "insert order details"]:
        insertDetailsInOrder()
    elif choice in ["2", "display order details"]:
        displayOrderDetails()
    elif choice in ["3", "delete any record"]:
        deleteFromOrder()
    elif choice in ["4", "update any record"]:
        updateOrder()
    elif choice in ["5", "search any record"]:
        searchRecInOrder()
    else:
        print("Wrong choice")

def submenuForService():
    print("SUBMENU:")
    print("1. Insert services details")
    print("2. Display services details")
    print("3. Delete any record")
    print("4. Update any record")
    print("5. Search any record")

    choice = input("Enter your choice: ").lower()

    if choice in ["1", "insert services details"]:
        insertDetailsInServices()
    elif choice in ["2", "display service details"]:
        displayServiceDetails()
    elif choice in ["3", "delete any record"]:
        deleteFromService()
    elif choice in ["4", "update any record"]:
        updateService()
    elif choice in ["5", "search any record"]:
        searchrecInServices()
    else:
        print("Wrong choice")

def menu():
    while True:
        print("MENU:")
        print("1. Customer Details")
        print("2. Order Details")
        print("3. Services")

        choice = input("Enter your choice: ").lower()

        if choice in ["1", "customer details"]:
            submenuForCustomer()
        elif choice in ["2", "order details"]:
            submenuForOrder()
        elif choice in ["3", "services"]:
            submenuForService()
        else:
            print("Wrong choice")

        con = input("Do you want to continue (y/n): ").lower()
        if con != "y":
            print("Thank you")
            break

if __name__ == "__main__":
    while True:
        query = input("Enter a command: ").lower()
        if "open menu" in query:
            menu()
        else:
            print("Unknown command.")