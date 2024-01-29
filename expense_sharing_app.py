class User:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def add_balance(self, amount):
        self.balance += amount


class Expense:
    def __init__(self, description, amount, users):
        self.description = description
        self.amount = amount
        self.users = users

    def split_bill(self):
        num_users = len(self.users)
        split_amount = self.amount / num_users
        for user in self.users:
            user.add_expense(split_amount)


class ExpenseSharingApp:
    def __init__(self):
        self.users = {}

    def add_user(self):
        name = input("Enter user's name: ")
        if name not in self.users:
            initial_balance = float(input("Enter initial balance for the user in ₹: "))
            self.users[name] = User(name, initial_balance)
        else:
            print("User already exists.")

    def add_expense(self):
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount in ₹: "))
        users_input = input("Enter names of users involved (comma-separated): ")
        users = [self.users[name] for name in users_input.split(",") if name in self.users]
        if not users:
            print("No valid users found.")
            return
        expense = Expense(description, amount, users)
        for user in users:
            user.add_expense(expense)

    def show_balance(self):
        for name, user in self.users.items():
            total_expense = sum(expense.amount for expense in user.expenses)
            balance = user.balance - total_expense
            print(f"{name}'s total expense: ₹{total_expense:.2f}, Balance: ₹{balance:.2f}")


# Example usage
app = ExpenseSharingApp()

while True:
    print("\n1. Add user")
    print("2. Add expense")
    print("3. Show balance")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        app.add_user()
    elif choice == "2":
        app.add_expense()
    elif choice == "3":
        app.show_balance()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
