import json
with open("user.txt", "r") as f:
    credentials = json.load(f)

email = input("Enter your email: ")
password = input("Enter your password: ")

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
            print("\n Your parcel's status: ",parcels["status"])
        else:
            print("Invalid Tracking ID")    
else:
    print("Invalid Credentials")            