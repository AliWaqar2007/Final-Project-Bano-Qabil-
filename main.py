import json

class User:
    def __init__(self, id, name, email, password, address):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.address = address

        self.user_dict = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "address" : self.address

        }

    def to_dict(self):
        return self.user_dict

class Agent:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

        self.agent_dict = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
        }
        
    def to_dict(self):
        return self.agent_dict    

class Parcel:
    def __init__(self, id, name, weight, tracking_id, status, for_user, to_user):
        self.id = id
        self.name = name
        self.weight = weight
        self.tracking_id = tracking_id
        self.status = status
        self.for_user = for_user
        self.to_user = to_user

        self.parcel_dict = {
            "id": self.id,
            "name": self.name,
            "weight": self.weight,
            "tracking_id": self.tracking_id,
            "status": self.status,
            "for_user": self.for_user,
            "to_user": self.to_user
        }

    def to_dict(self):
        return self.parcel_dict

class Branch:
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

print("\n1: Add a user")
print("2: Add a agent")
print("3: Add a parcel")
print("4: Add a branch")

print("\n11: Update a user")
print("12: Update a agent")
print("13: Update a parcel")
print("14: Update a branch\n")

action = int(input("Enter your action: "))

if action == 1:
    id = int(input("Enter user ID: "))
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    password = input("Enter user password: ")
    address = input("Enter user address: ")
    User_data = User(id, name, email, password, address)

    user_dict = User_data.to_dict()

    with open("user.txt", "w") as f:
        json.dump(user_dict, f, indent=4)

elif action == 3:
    id = int(input("Enter parcel ID: "))
    name = input("Enter parcel name: ")
    weight = float(input("Enter parcel weight (in kg): "))
    tracking_id = int(input("Enter parcel tracking_id: "))
    status = int(input("Enter the parcel's status (in digit): "))
    from_user = input("Enter customer's name from whom parcel has to be delivered: ")
    to_user = input("Enter customer's name for whom parcel will be delivered: ")

    parcel_data = Parcel(id, name, weight, tracking_id, status, from_user, to_user)

    parcel_dict = parcel_data.to_dict()

    with open("parcel.txt", "w") as f:
        json.dump(parcel_dict, f, indent=4)

elif action == 4:
    id = int(input("Enter branch id: "))
    name = input("Enter branch name: ")
    address = input("Enter branch address: ")
    state = input("Enter State: ")
    country = input("Enter country where branch is situated: ")

    branch_data = Branch(id, name, address, state, country)

    branch_dict = branch_data.to_dict()

    with open("branch.txt", "w") as f:
        json.dump(branch_dict, f, indent=4)

elif action == 2:
    id = int(input("Enter agent ID: "))
    name = input("Enter agent name: ")
    email = input("Enter agent email: ")
    password = input("Enter agent password: ")
    agent_data = Agent(id, name, email, password)

    agent_dict = agent_data.to_dict()

    with open("agent.txt", "w") as f:
        json.dump(agent_dict, f, indent=4)

elif action == 11:
    id = int(input("Enter user id you want to update: "))
    field = input("Which field you want to update: ")
    update_data = input(f"Enter the new value for {field}: ")

    with open("user.txt", "r+") as file:
        users = json.load(file)

        for user in users:
            if user["id"] == id:
                user[field] = update_data

        json.dump(users, file, indent=4)

elif action == 12:
    id = int(input("Enter agent id you want to update: "))
    field = input("Which field you want to update: ")
    update_data = input(f"Enter the new value for {field}: ")

    with open("agent.txt", "r+") as file:
        agent = json.load(file)

        for agents in agent:
            if agents["id"] == id:
                agents[field] = update_data

        json.dump(agent, file, indent=4)

elif action == 13:
    id = int(input("Enter parcel id you want to update: "))
    field = input("Which field you want to update: ")
    update_data = input(f"Enter the new value for {field}: ")

    with open("parcel.txt", "r+") as file:
        parcel = json.load(file)

        for parcels in parcel:
            if parcels["id"] == id:
                parcels[field] = update_data

        json.dump(parcel, file, indent=4)

elif action == 14:
    id = int(input("Enter branch id you want to update: "))
    field = input("Which field you want to update: ")
    update_data = input(f"Enter the new value for {field}: ")

    with open("branch.txt", "r+") as file:
        branch = json.load(file)

        for branches in branch:
            if branches["id"] == id:
                branches[field] = update_data

        json.dump(branch, file, indent=4)
else:
    print("Invalid Action")
