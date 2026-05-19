import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Patna@123",
        database="bookshare"
    )
def add_user():
    con = connect()
    cur = con.cursor()
    
    print("\n--- Register New User ---")
    name = input("Enter your name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    cur.execute("""
        INSERT INTO User(name, phone, email)
        VALUES (%s, %s, %s)
    """, (name, phone, email))

    con.commit()
    print("✅ User registered successfully!\n")

def view_users():
    con = connect()
    cur = con.cursor()
    
    cur.execute("SELECT * FROM User")
    data = cur.fetchall()

    print("\n--- Registered Users ---")
    for u in data:
        print(f"ID: {u[0]}, Name: {u[1]}, Phone: {u[2]}, Email: {u[3]}")
    print()
def search_user():
    con = connect()
    cur = con.cursor()

    uid = int(input("Enter User ID to search: "))
    cur.execute("SELECT * FROM User WHERE User_id = %s", (uid,))
    data = cur.fetchone()

    print("\n--- User Details ---")
    if data:
        print(f"ID: {data[0]}")
        print(f"Name: {data[1]}")
        print(f"Phone: {data[2]}")
        print(f"Email: {data[3]}")
    else:
        print("User not found.")
    print()

def update_user():
    con = connect()
    cur = con.cursor()

    uid = int(input("Enter User ID to update: "))
    print("\nWhat do you want to update?")
    print("1. Name\n2. Phone\n3. Email")
    ch = int(input("Enter choice: "))

    if ch == 1:
        new = input("Enter new name: ")
        cur.execute("UPDATE User SET name=%s WHERE User_id=%s", (new, uid))
    elif ch == 2:
        new = input("Enter new phone: ")
        cur.execute("UPDATE User SET phone=%s WHERE User_id=%s", (new, uid))
    elif ch == 3:
        new = input("Enter new email: ")
        cur.execute("UPDATE User SET email=%s WHERE User_id=%s", (new, uid))
    else:
        print("Invalid choice.")
        return

    con.commit()
    print("✅ User updated successfully!\n")

def delete_user():
    con = connect()
    cur = con.cursor()

    uid = int(input("Enter User ID to delete: "))

    cur.execute("DELETE FROM User WHERE User_id = %s", (uid,))
    con.commit()

    print("🗑️ User deleted successfully!\n")

def search_user():
    db = connect()
    cur = db.cursor()

    uid = input("Enter User ID to search: ")
    query = "SELECT * FROM User WHERE User_id = %s"
    cur.execute(query, (uid,))

    data = cur.fetchone()
    if data:
        print("User Found:", data)
    else:
        print("No user found with that ID.")

while True:
        print("\n====== USER MANAGEMENT MENU ======")
        print("1. Add User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Search User")
        print("6. Exit User Menu")
    

        ch = input("Enter your choice: ")

        if ch == "1":
            add_user()
        elif ch == "2":
            view_users()
        elif ch == "3":
            update_user()
        elif ch == "4":
            delete_user()
        elif ch == "5":
            search_user()
        elif ch == "6":
            print("Exiting User Menu...")
            break
        else:
            print("Invalid choice! Try again.")
            
