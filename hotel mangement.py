import pandas as pd

# Initialize an empty DataFrame for bookings
columns = ['Booking ID', 'Customer Name', 'Check-in Date', 'Check-out Date', 'Room Type', 'Amount']
bookings_df = pd.DataFrame(columns=columns)

# Function to add a new booking
def add_booking():
    global bookings_df
    booking_id = len(bookings_df) + 1
    customer_name = input("Enter Customer Name: ")
    check_in = input("Enter Check-in Date (YYYY-MM-DD): ")
    check_out = input("Enter Check-out Date (YYYY-MM-DD): ")
    room_type = input("Enter Room Type: ")
    amount = float(input("Enter Amount: "))

    # Create a new booking record
    new_booking = {
        'Booking ID': booking_id,
        'Customer Name': customer_name,
        'Check-in Date': check_in,
        'Check-out Date': check_out,
        'Room Type': room_type,
        'Amount': amount
    }

    new_booking_df = pd.DataFrame([new_booking])
    bookings_df = pd.concat([bookings_df, new_booking_df], ignore_index=True)
    print("Booking added successfully.")

# Function to view all bookings
def view_bookings():
    print("\nCurrent Bookings:")
    print(bookings_df)

# Function to search for a booking by customer name
def search_booking():
    customer_name = input("Enter Customer Name to search: ")
    results = bookings_df[bookings_df['Customer Name'].str.contains(customer_name, case=False)]
    if results.empty:
        print("No bookings found for this customer.")
    else:
        print("\nSearch Results:")
        print(results)

# Function to export bookings to a CSV file
def export_to_csv():
    bookings_df.to_csv("C:\\Users\\abc\\onedrive\\desktop\\csv\\hotel mangement.csv", index=False)
    print("Bookings exported to hotel_bookings.csv successfully.")

# Main menu for the hotel management system
def main_menu():
    while True:
        print("\nHotel Management System")
        print("1. Add Booking")
        print("2. View Bookings")
        print("3. Search Booking")
        print("4. Export to CSV")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_booking()
        elif choice == '2':
            view_bookings()
        elif choice == '3':
            search_booking()
        elif choice == '4':
            export_to_csv()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")

# Run the main menu
if __name__ == "__main__":
    main_menu()
