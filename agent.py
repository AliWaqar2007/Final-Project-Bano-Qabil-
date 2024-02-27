import json

with open("agent.txt", "r") as f:
    credentials = json.load(f)

email = input("Enter your email: ")
password = input("Enter your password: ")

if credentials["email"] == email and credentials["password"] == password:
    print("Hi", credentials["name"])
    ask = input("Type 'yes' to change a parcel's status: ")
    if ask.lower() == "yes":
        parcel_id = int(input("Enter parcel's id: "))
        
        with open("parcel.txt", "r") as f:
            parcels = json.load(f)
        
        if parcels["id"] == parcel_id:
            print("0: Order Processing")
            print("1: Pickup Request")
            print("2: In Transit")
            print("3: Arrived at Sorting Facility")
            print("4: Out for Delivery")
            print("5: Delivery Attempted")
            print("6: Delivered")
            status = input("Enter updated status: ")
            
            parcels["status"] = status
            
            with open("parcel.txt", "w") as f:
                json.dump(parcels, f, indent=4)
            
            print("Status updated successfully!")
        else:
            print("Parcel not found.")
else:
    print("Invalid credentials.")
