

from hotel.rooms import rooms
from hotel.guest import get_guest

bookings = []

def book_room():
    aadhar = int(input("Enter guest Aadhar number: "))
    guest = get_guest(aadhar)

    if not guest:
        print("Guest not registered")
        return

    room_type = input("Enter room type (AC / Non AC): ")
    days = int(input("Enter number of days: "))

    for room in rooms:
        if room["available"] and room["type"].lower() == room_type.lower():
            room["available"] = False
            total = room["price"] * days

            bookings.append({
                "name": guest["name"],
                "aadhar": aadhar,
                "room_no": room["r_no"],
                "room_type": room["type"],
                "days": days,
                "total": total
            })

            print("Room booked successfully")
            print(f"Room No: {room['r_no']}")
            print(f"Total Bill: ₹{total}")
            return

    print(" No available rooms")

def get_all_booking():
    return bookings

def view_booking_history():
    if not bookings:
        print("No booking history")
        return

    for b in bookings:
        print("-" * 30)
        for k, v in b.items():
            print(f"{k}: {v}")

