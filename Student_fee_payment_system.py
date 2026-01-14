payments = []

def add_payment():
    name = input("Enter student name: ")
    amount = input("Enter amount paid: ")
    payments.append({"name": name, "amount": amount})
    print("Payment recorded successfully")

def view_payments():
    if not payments:
        print("No payment records found")
    else:
        for payment in payments:
            print(payment["name"], "- Amount Paid:", payment["amount"])

def main():
    while True:
        print("1. Add Payment")
        print("2. View Payments")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_payment()
        elif choice == "2":
            view_payments()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
