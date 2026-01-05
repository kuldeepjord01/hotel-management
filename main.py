
from hotel.rooms import add_room, get_all_rooms, rooms
from hotel.guest import add_guest, get_all_guest, search_guest
from hotel.booking import book_room, get_all_booking, view_booking_history

def main():
    while True:
        print("""
        ===== ROYAL HOTEL =====
         1. Add Room
         2. View Rooms
         3. Register Guest
         4. Book Room
         5. Checkout Guest
         6. View All Guests
         7. View Bookings
         8. Search Guest
         9. Booking History
         10. Exit
        """)

        choice = int(input("Enter choice: "))

        if choice == 1:
            r_no = int(input("Room number: "))
            r_type = input("Room type (AC/Non AC): ")
            price = int(input("Price per day: "))
            print(add_room(r_no, r_type, price))

        elif choice == 2:
            for r in get_all_rooms():
                print(r)

        elif choice == 3:
            name = input("Name: ")
            aadhar = int(input("Aadhar: "))
            gender = input("Gender: ")
            contact = input("Contact: ")
            print(add_guest(name, aadhar, gender, contact))

        elif choice == 4:
            book_room()

        elif choice == 5:
            r_no = int(input("Room number to checkout: "))
            for r in rooms:
                if r["r_no"] == r_no:
                    r["available"] = True
                    print("Checkout successful")
                    break
            else:
                print("Room not found")

        elif choice == 6:
            for g in get_all_guest():
                print(g)

        elif choice == 7:
            for b in get_all_booking():
                print(b)

        elif choice == 8:
            name = input("Enter name: ")
            search_guest(name)

        elif choice == 9:
            view_booking_history()

        elif choice == 10:
            print("Goodbye")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()


