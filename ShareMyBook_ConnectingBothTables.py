import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Patna@123",
        database="bookshare"
    )

def view_all_books_with_seller():
    con = connect()
    cur = con.cursor()

    query = """
        SELECT b.book_id, b.title, b.author, b.category, b.book_condition,
               b.type, b.price,
               u.user_id, u.name, u.phone, u.email
        FROM books b
        JOIN User u ON b.user_id = u.User_id
    """
    cur.execute(query)
    data = cur.fetchall()

    print("\n--- Books With Seller Details ---")
    for row in data:
        print(f"\nBook ID: {row[0]}")
        print(f"Title: {row[1]}")
        print(f"Author: {row[2]}")
        print(f"Category: {row[3]}")
        print(f"Condition: {row[4]}")
        print(f"Type: {row[5]}")
        print(f"Price: {row[6]}")
        print("----- Seller Info -----")
        print(f"Seller ID: {row[7]}")
        print(f"Name: {row[8]}")
        print(f"Phone: {row[9]}")
        print(f"Email: {row[10]}")
    print()

def view_books_by_user():
    con = connect()
    cur = con.cursor()

    uid = int(input("Enter User ID: "))

    query = """
        SELECT b.book_id, b.title, b.author, b.category, b.type, b.price
        FROM books b
        WHERE b.user_id = %s
    """
    cur.execute(query, (uid,))
    data = cur.fetchall()

    print(f"\n--- Books Added by User {uid} ---")
    for row in data:
        print(f"\nBook ID: {row[0]}")
        print(f"Title: {row[1]}")
        print(f"Author: {row[2]}")
        print(f"Category: {row[3]}")
        print(f"Type: {row[4]}")
        print(f"Price: {row[5]}")
    print()

def search_book_with_seller():
    con = connect()
    cur = con.cursor()

    title = input("Enter title to search: ")

    query = """
        SELECT b.book_id, b.title, b.author, b.category, b.type, b.price,
               u.name, u.phone, u.email
        FROM books b
        JOIN User u ON b.user_id = u.User_id
        WHERE b.title LIKE %s
    """
    cur.execute(query, ("%" + title + "%",))
    data = cur.fetchall()

    print("\n--- Search Results ---")
    for row in data:
        print(f"\nBook ID: {row[0]}")
        print(f"Title: {row[1]}")
        print(f"Author: {row[2]}")
        print(f"Category: {row[3]}")
        print(f"Type: {row[4]}")
        print(f"Price: {row[5]}")
        print("----- Seller Info -----")
        print(f"Name: {row[6]}")
        print(f"Phone: {row[7]}")
        print(f"Email: {row[8]}")
    print()

def view_donation_books():
    con = connect()
    cur = con.cursor()

    query = """
        SELECT b.book_id, b.title, b.author,
               u.name, u.phone, u.email
        FROM books b
        JOIN User u ON b.user_id = u.User_id
        WHERE b.type = 'Donate'
    """
    cur.execute(query)
    data = cur.fetchall()

    print("\n--- Donation Books ---")
    for row in data:
        print(f"\nBook ID: {row[0]}")
        print(f"Title: {row[1]}")
        print(f"Author: {row[2]}")
        print("Seller:", row[3])
        print("Phone:", row[4])
        print("Email:", row[5])
    print()

def view_rental_books():
    con = connect()
    cur = con.cursor()

    query = """
        SELECT b.book_id, b.title, b.author, b.price,
               u.name, u.phone, u.email
        FROM books b
        JOIN User u ON b.user_id = u.User_id
        WHERE b.type = 'Rent'
    """
    cur.execute(query)
    data = cur.fetchall()

    print("\n--- Rental Books ---")
    for row in data:
        print(f"\nBook ID: {row[0]}")
        print(f"Title: {row[1]}")
        print(f"Author: {row[2]}")
        print(f"Rent Price: {row[3]}")
        print("Seller:", row[4])
        print("Phone:", row[5])
        print("Email:", row[6])
    print()

while True:
    print("""
    1. View Books with seller info
    2. View Books by User
    3. Search Books along with Sellers
    4. View Book + Seller Info
    5. View Donation books
    6. View Rental books
    7. Exit
    """)
    ch = int(input("Enter choice: "))

    if ch == 1:
        view_all_books_with_seller()
    elif ch == 2:
        view_books_by_user()
    elif ch == 3:
        search_book_with_seller()
    elif ch == 4:
        view_book_with_seller()
    elif ch == 5:
        view_donation_books()
    elif ch == 6:
        view_rental_books()
    else:
        break
