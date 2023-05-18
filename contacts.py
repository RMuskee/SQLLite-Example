import sqlite3

def create_database():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (name TEXT, phone TEXT)''')

    conn.commit()
    conn.close()

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")

    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()

    c.execute("INSERT INTO contacts VALUES (?, ?)", (name, phone))

    conn.commit()
    conn.close()

def display_contacts():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()

    c.execute("SELECT * FROM contacts")
    contacts = c.fetchall()

    if contacts:
        print("Contacts:")
        for contact in contacts:
            print("Name:", contact[0])
            print("Phone:", contact[1])
            print("-----")
    else:
        print("No contacts found.")

    conn.close()

create_database()
add_contact()
display_contacts()