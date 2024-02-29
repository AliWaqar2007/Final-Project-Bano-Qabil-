import json
import os

print("1: Login")
print("2: Register")
choice = int(input("Enter your action: "))

if choice == 1:
    if os.path.exists("user.txt") and os.path.getsize("user.txt") > 0:
        with open("user.txt", "r") as f:
            credentials = json.load(f)
    else:
        credentials = {}

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if "email" in credentials and "password" in credentials:
        if credentials["email"] == email and credentials["password"] == password:
            print("Hi", credentials["name"])
            ask = input("Type 'yes' to see your parcel's status: ")
            if ask.lower() == "yes":
                parcel_id = int(input("Enter parcel's tracking id: "))
                
                with open("parcel.txt", "r") as f:
                    parcels = json.load(f)
                
                if parcels["tracking_id"] == parcel_id:
                    print("0: Order Processing")
                    print("1: Pickup Request")
                    print("2: In Transit")
                    print("3: Arrived at Sorting Facility")
                    print("4: Out for Delivery")
                    print("5: Delivery Attempted")
                    print("6: Delivered")
                    print("\nYour parcel's status: ", parcels["status"])
                    if parcels["status"] == 6:
                        obj_ask = input("You have received the parcel. Is there any objection from your side. (Type 'yes' if there is): ")
                        if obj_ask.lower() == "yes":
                            objection = input("Describe: ")
                            with open("obj.txt", "w") as f:
                                json.dump(objection, f, indent=4)

                        elif obj_ask.lower() == "no" or obj_ask == "":
                            print("Thank you for trusting us!")
                else:
                    print("Invalid Tracking ID")

        else:
            print("Invalid Credentials")
    else:
        print("User credentials not found. Please register.")

elif choice == 2:
    id = 10
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    password = input("Enter user password: ")
    address = input("Enter user address: ")

    user = {
        "id" : id,
        "name" : name,
        "email" : email,
        "password" : password,
        "address" : address
    }

    with open("user.txt", "w") as f:
        json.dump(user, f, indent=4)

else:
    print("Invalid action: ")
