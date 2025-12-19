


rooms = [
    {
        "r_no": 1,
        "type": "AC",
        "price": 500,
        "available": True
    },
    {
        "r_no": 2,
        "type": "Non AC",
        "price": 300,
        "available": True
    }
]

def get_all_rooms():
    return rooms

def add_room(r_no, r_type, price):
    rooms.append({
        "r_no": r_no,
        "type": r_type,
        "price": price,
        "available": True
    })
    return "✅ Room added successfully"

