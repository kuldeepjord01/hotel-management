
guests = []

def add_guest(name, aadhar, gender, contact):
    guests.append({
        "name": name,
        "aadhar": aadhar,
        "gender": gender,
        "contact": contact
    })
    return " Guest registered successfully"

def get_guest(aadhar):
    for g in guests:
        if g["aadhar"] == aadhar:
            return g
    return None

def get_all_guest():
    return guests

def search_guest(name):
    found = False
    for g in guests:
        if g["name"].lower() == name.lower():
            print(g)
            found = True
    if not found:
        print(" Guest not found")

