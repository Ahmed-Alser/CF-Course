print(f"----------------------- >> Welcome to Gaza bus station << -----------------------")
booking_A = []
booking_B = []
user_info = {"buses": [], "seats": []}
name = input("Enter you full name: ")
Id = input("Enter your Id: ")
while True:
    bus = int(input("Choose a destination from the following available trips :\n1. Bus A: From KhanYounis To Gaza "
                    "\n2. Bus B: From Gaza to Jerusalem\n>> "))
    seat = int(input("Choose a seat number (In range 1-25):\n>> "))
    if bus == 1:

        if seat in booking_A:
            print("Sorry! this seat Already Booked")
        else:
            print(f"Ticket Booked Successfully\nConfirmation message: Seat number {seat} has been reserved on Bus-A"
                  f" (KhanYounis ----> Gaza) ")
            booking_A.append(seat)
            user_info["buses"] += ["Bus A - KhanYounis ----> Gaza"]
            user_info["seats"] += [seat]
    else:

        if seat in booking_B:
            print("Sorry! this seat Already Booked")
        else:
            print("Ticket Booked Successfully\nConfirmation message: Seat number {seat} has been reserved on Bus-B("
                  "Gaza ----> Jerusalem) ")
            booking_B.append(seat)
            user_info["buses"] += ["Bus B - Gaza ----> Jerusalem"]
            user_info["seats"] += [seat]

    another_booking = input("Do you want another booking? ")
    if another_booking.lower() == "yes":
        continue
    else:
        print("------------------------------------------------------------------------------")
        print("                 Thank you for using Gaza bus station                         ")
        print("------------------------------------------------------------------------------")
        print(f"Passenger name : {name}          Passenger Id: {Id}")
        # for i in range(len(user_info["buses"])):
        for key, list in user_info.items():
            print(f"{name}'s booked {key}>> ")
            for item in list:
                print(f" {item}")
        print("------------------------------------------------------------------------------")

        break
