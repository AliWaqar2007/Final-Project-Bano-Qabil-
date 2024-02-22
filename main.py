import json

class User:
    def __init__(self, id, name, email, password, rtype, branch=None, address=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.rtype = rtype
        self.branch = branch
        self.address = address

        self.user_dict = {
            
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "rtype": self.rtype
            
        }
        if self.rtype == "agent":
            self.user_dict["branch"] = self.branch
        elif self.rtype == "customer":
            self.user_dict["address"] = self.address

    def to_dict(self):
        return self.user_dict

class Parcel:
    def __init__(self, id, name, weight, tracking_id, for_user, to_user, type):
        self.id = id
        self.name = name
        self.weight = weight
        self.tracking_id = tracking_id
        self.for_user = for_user
        self.to_user = to_user
        self.type = type

        self.parcel_dict = {
            "id": self.id,
            "name": self.name,
            "weight": self.weight,
            "tracking_id": self.tracking_id,
            "for_user": self.for_user,
            "to_user": self.to_user,
            "type": self.type
        }

    def to_dict(self):
        return self.parcel_dict
    
class branch:
    def __init__(self, id, name, address, state, country):
        self.id = id
        self.name = name
        self.address = address
        self.state = state
        self.country = country

        self.branch_dict = {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "state": self.state,
            "country": self.country,
        }

    def to_dict(self):
        return self.branch_dict 
    
print("1: Add a user")
print("2: Add a parcel")
print("3: Add a branch")

print("11: Update a user")
print("12: Update a parcel")
print("13: Update a branch")

action = int(input("Enter your action: "))

if action == 1:
    id = int(input("Enter user ID: "))
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    password = input("Enter user password: ")
    rtype = input("Enter user type (customer/agent): ")
    if rtype == "agent":
        branch_ = input("Enter agent branch: ")
        User_data = User(id, name, email, password, rtype, branch_)
    elif rtype == "customer":
        address = input("Enter user address: ")
        User_data = User(id, name, email, password, rtype, address)

    user_dict = User_data.to_dict()

    json_user = json.dumps(user_dict, indent=4)

    f = open("user.txt","a")
    f.write(json_user)
    f.close()

elif action == 2:
    id = int(input("Enter parcel ID: "))
    name = input("Enter parcel name: ")
    weight = int(input("Enter parcel weight (in kg): "))
    tracking_id = int(input("Enter parcel tracking_id: "))
    from_user = int(input("Enter user's id from whom parcel has to be delivered: "))
    to_user = int(input("Enter user's id for whom parcel will be delivered: "))
    type = input("Enter parcel type (delivery/pickup): ")

    parcel_data = Parcel(id, name, weight, tracking_id, from_user, to_user, type)

    parcel_dict = parcel_data.to_dict()

    json_parcel = json.dumps(parcel_dict, indent=4)

    f = open("parcel.txt","a")
    f.write(json_parcel)
    f.close()

elif action == 3:
    id = int(input("Enter branch id: "))
    name = input("Enter branch id: ")
    address = input("Enter branch address: ")
    state = input("Enter State: ")
    country = input("Enter country where branch is situated: ")

    branch_data = branch(id, name, address, state, country)

    branch_dict = branch_data.to_dict()

    json_branch = json.dumps(branch_dict, indent=4)

    f = open("branch.txt","a")
    f.write(json_branch)
    f.close()

elif action == 11:
    id = int(input("Enter user id you want to update: "))
    field = input("Which field you want to update: ")

    with open("user.txt", "r") as file:
        users = json.load(file)

    user_update_index = None

    for i in users:
        if i["id"] == id:
            user_update_index = i
            break

    if user_update_index != None:
        update_data = input(f"Enter the new value for {field}: ")
        users[user_update_index][field] = update_data

        with open("user.txt", "w") as file:
            json.dump(users, file, indent=4)

    else:  
        print("User not found")
