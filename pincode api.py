import json
import requests

def district_name():
    pin = input("Enter your Postal Pin-code\n")

    try:
        pin_api = f"https://api.postalpincode.in/pincode/{pin}"

        res = requests.get(pin_api)
        data = json.loads(res.content)
        no_of_district = data[0]["Message"].split(":")
        var = int(no_of_district[1])
        print(var, "District found")

        for i in range(var):
            overall = f"{i + 1}" + ". " + data[0]["PostOffice"][i]['Name'] + ", " + data[0]["PostOffice"][i][
                'District'] + ", " + data[0]["PostOffice"][i]['State']
            print(overall)

    except Exception as e:
        print("No record found. Please enter a valid Pin-code")


def pincode():
    dis_name = str(input("Enter Branch Name or Postal Office Name\n"))

    try:
        dis_api = f"https://api.postalpincode.in/postoffice/{dis_name}"

        res = requests.get(dis_api)
        data = json.loads(res.content)
        no_of_district = data[0]["Message"].split(":")
        var = int(no_of_district[1])
        print(var, "Pin-codes found")

        for i in range(var):
            overall = f"{i + 1}" + ". " + data[0]["PostOffice"][i]['Name'] + ", " + data[0]["PostOffice"][i][
                'District'] + ", " + data[0]["PostOffice"][i]['State'] + ", " + data[0]["PostOffice"][i]['Pincode']
            print(overall)

    except Exception as e:
        print("No record found. Please enter the correct name OR check the spelling once")


# if __name__ == '__main__':
#
#     while(True):
#         choice = str(input("\t\t\tWhat you want to search\n1. Pin-code via Branch name\n2. Branch name via Pin-code\n3. Quit\n"))
#
#         if choice == "1":
#             pincode()
#
#         elif choice == "2":
#             district_name()
#
#         elif choice == "3":
#             print("You took a exit")
#             exit()
#
#         else:
#             print("Invalid user choice. Please select again")

from tkinter import *

def search():
    global pin_value, branch_value
    pin_value = pin_code.get()
    branch_value = branch_name.get()
    print(f"Pin-Code:- {pin_value}\nBranch Name:- {branch_value}")
    new_window = Toplevel()
    new_window.geometry("456x456")
    Label(new_window, text="This is a search window").pack()

    new_window.mainloop()

def clear():

    pin_code.set(" ")
    branch_name.set(" ")


def pin():
    new_window = Toplevel()
    new_window.geometry("456x456")
    Label(new_window, text="This is a Pincode window").grid(row=1, column=3)
    global pin_code
    pin_code = StringVar()
    pin_code.set(" ")
    screen1 = Entry(root, textvariable=pin_code, font="Stylus 25", width=10).grid(row=2, column=3, ipady=10, ipadx=10, pady=10)
    Label(root, text="Postal Pin-code", font="Arial 18", padx=100).grid(row=2, column=2)

    new_window.mainloop()


def branch():
    new_window = Toplevel()
    new_window.geometry("456x456")
    Label(new_window, text="This is a Branch window").pack()

    global branch_name
    branch_name = StringVar()
    branch_name.set(" ")
    screen2 = Entry(root, textvariable=branch_name , font="Stylus 25", width=15).grid(row=3, column=3, ipady=10, ipadx=10, pady=10)
    Label(root, text="Branch Name ", font="Arial 18", padx=100).grid(row=3, column=2)


root = Tk()
root.geometry("1100x356")
root.title("Pin-code Finder")
Label(root, text="Welcome to know the Pin-code or Branch Name Finder", font="ChristmasStory 22 italic").grid(row=1, column=2)


search_pincode = Button(root, text="Know Pin-Code", command=pin, font="Stylus 15", borderwidth=4).grid(row=2, column=3)
search_branch = Button(root, text="Know Branch Name", command=branch, font="Stylus 15", borderwidth=4).grid(row=3, column=3)

root.mainloop()
