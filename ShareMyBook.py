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
    name = input("Enter your name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    cur.execute("INSERT INTO User(name, phone, email) VALUES (%s, %s, %s)", 
                (name, phone, email))
    con.commit()
    print("User registered successfully!\n")
def add_book():
    con = connect()
    cur = con.cursor()

    title = input("Book title: ")
    author = input("Author: ")
    category = input("Category: ")

    condition = input("Condition (New/Used): ").title()
    btype = input("Type (Donate/Rent): ").title()

    price = 0
    if btype == "Rent":
        price = int(input("Enter rent price: "))

    user_id = int(input("Enter your user ID: "))

    cur.execute("SELECT User_id FROM `User` WHERE User_id = %s", (user_id,))
    if cur.fetchone() is None:
        print("❌ Error: This user does not exist. Please register first.")
        return

    cur.execute("""
        INSERT INTO books(title, author, category, book_condition, type, price, user_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (title, author, category, condition, btype, price, user_id))

    con.commit()
    print("✔ Book added successfully!\n")


def view_books():
    con = connect()
    cur = con.cursor()
    cat = input("Enter category to search: ")

    query = "SELECT * FROM books WHERE category = %s"
    cur.execute(query, (cat,))
    rows = cur.fetchall()

    if not rows:
        print("No books found in this category.\n")
        return

    for row in rows:
        print(row)
    print()

def view_book_with_seller():
    con = connect()
    cur = con.cursor()

    book_id = int(input("Enter Book ID: "))

    cur.execute("""
        SELECT b.title, b.author, b.type, b.price, u.name, u.phone, u.email 
        FROM books b
        JOIN `User` u ON b.user_id = u.User_id
        WHERE b.book_id = %s
    """, (book_id,))

    data = cur.fetchone()

    if data:
        print("\nBook Details")
        print("Title:", data[0])
        print("Author:", data[1])
        print("Type:", data[2])
        print("Price:", data[3])
        print("\nSeller Information")
        print("Name:", data[4])
        print("Phone:", data[5])
        print("Email:", data[6])
    else:
        print("Book not found\n")

def update_book():
    con = connect()
    cur = con.cursor()

    book_id = int(input("Enter Book ID to update: "))
    title = input("Enter new Title: ")
    author = input("Enter new Author: ")
    category = input("Enter new Category: ")

    query = """
        UPDATE Books 
        SET title=%s, author=%s, category=%s
        WHERE book_id=%s
    """

    cur.execute(query, (title, author, category, book_id))
    con.commit()

    print("Book updated successfully!")
    con.close()

def delete_book():
    con = connect()
    cur = con.cursor()

    book_id = input("Enter Book ID to delete: ")

    cur.execute("DELETE FROM Books WHERE book_id=%s", (book_id,))
    con.commit()

    print("Book deleted successfully!")
    con.close()


while True:
    print("""
    1. Register User
    2. Add Book
    3. View Books by Category
    4. View Book + Seller Info
    5. Update book
    6. Delete book
    7. Exit
    """)
    ch = int(input("Enter choice: "))

    if ch == 1:
        add_user()
    elif ch == 2:
        add_book()
    elif ch == 3:
        view_books()
    elif ch == 4:
        view_book_with_seller()
    elif ch == 5:
        update_book()
    elif ch == 6:
        delete_book()
    else:
        break




