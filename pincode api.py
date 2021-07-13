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
        print(var, "records found")

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
        print(var, "records found")

        for i in range(var):
            overall = f"{i + 1}" + ". " + data[0]["PostOffice"][i]['Name'] + ", " + data[0]["PostOffice"][i][
                'District'] + ", " + data[0]["PostOffice"][i]['State'] + ", " + data[0]["PostOffice"][i]['Pincode']
            print(overall)

    except Exception as e:
        print("No record found. Please enter the correct name OR check the spelling once")


if __name__ == '__main__':

    while(True):
        choice = str(input("\t\t\tWhat you want to search\n1. Pin-code via Branch name\n2. Branch name via Pin-code\n3. Quit\n"))

        if choice == "1":
            pincode()

        elif choice == "2":
            district_name()

        elif choice == "3":
            print("You took a exit")
            exit()

        else:
            print("Invalid user choice. Please select again")
