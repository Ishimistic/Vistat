from vistatsql import menu;

def thankyou():
    while True:
        cont = input("Do you wanna continue(y/n) ")
        if cont == "y":
            menu()
        else:
            break

