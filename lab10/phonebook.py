import psycopg2
import csv
import json

# Connect to PostgreSQL
def connect():
    return psycopg2.connect(
        host="localhost",
        database="phones",  
        user="ansstsvv",          
        password="12345678"  
    )

conn = connect()
cur = conn.cursor()
#cur.execute("""
  #          CREATE PROCEDURE inserting(name1 VARCHAR(100), phone1 VARCHAR(15))
   #         LANGUAGE plpgsql
    #        AS $$
     #       BEGIN
      #          INSERT INTO PhoneBook (name, phone) VALUES (name1, phone1);
       #         COMMIT;
        #    END;
         #   $$;
#""")
#cur.execute("""
          #  CREATE PROCEDURE updating(phone1 VARCHAR(15))
           # LANGUAGE plpgsql
            #AS $$
          #  BEGIN
           #     UPDATE PhoneBook SET phone = phone1 WHERE name = name1;
            #    COMMIT;
         #   END;
          #  $$;
#""")
conn.commit()
cur.close()
conn.close()


def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(15) NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_user_new():
    name1 = input("Enter name: ")
    phone1 = str(input("Enter phone: "))
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM PhoneBook WHERE name = %s", (name1,))
    user_exists = cur.fetchone()
    if user_exists:
        cur.execute("CALL updating(%s, %s)", (name1, phone1))
        print("donennne")
    else:
        cur.execute("CALL inserting(%s, %s)", (name1, phone1))
        print("disdfjsdf")
    cur.close()
    conn.close()



def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = connect()
    cur = conn.cursor()

    # Check if the user already exists
    cur.execute("SELECT * FROM PhoneBook WHERE name = %s", (name,))
    user = cur.fetchone()

    if user:
        # Update the phone number if the user exists
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE name = %s", (phone, name))
        print(f"Phone number for '{name}' updated successfully!")
    else:
        # Insert a new user if they don't exist
        cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
        print(f"User '{name}' inserted successfully!")

    conn.commit()
    cur.close()
    conn.close()


def insert_from_csv(file_path):
    conn = connect()
    cur = conn.cursor()
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader) #propuskayem header row
        for row in reader:
            cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("Data uploaded from CSV successfully!")
    cur.close()
    conn.close()


def insert_or_update_user(name, phone):
    conn = connect()
    cur = conn.cursor()
    query = """
        INSERT INTO PhoneBook (name, phone)
        VALUES (%s, %s)
        ON CONFLICT (name) DO UPDATE
        SET phone = EXCLUDED.phone
    """
    cur.execute(query, (name, phone))
    conn.commit()
    print(f"User '{name}' inserted or updated successfully!")
    cur.close()
    conn.close()

def insert_many_users(users):
    conn = connect()
    cur = conn.cursor()
    invalid_users = []

    for user in users:
        name = user.get("name")
        phone = user.get("phone")

        # checking phone number
        if phone.isdigit():
            query = """
                INSERT INTO PhoneBook (name, phone)
                VALUES (%s, %s)
                ON CONFLICT (name) DO UPDATE
                SET phone = EXCLUDED.phone
            """
            cur.execute(query, (name, phone))
        else:
            invalid_users.append(user)

    conn.commit()
    print("Users processed successfully!")
    if invalid_users:
        print("Invalid users:", invalid_users)
    cur.close()
    conn.close()


def update_data():
    conn = connect()
    cur = conn.cursor()
    user_id = input("Enter the ID of the user to update: ")
    new_name = input("Enter the new name (leave blank to skip): ")
    new_phone = input("Enter the new phone (leave blank to skip): ")

    if new_name:
        cur.execute("UPDATE PhoneBook SET name = %s WHERE id = %s", (new_name, user_id))
    if new_phone:
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE id = %s", (new_phone, user_id))

    conn.commit()
    print("Data updated successfully!")
    cur.close()
    conn.close()


def query_data():
    conn = connect()
    cur = conn.cursor()
    print("1. Query by name")
    print("2. Query by phone")
    print("3. Query by partial name match")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name to search: ")
        cur.execute("SELECT * FROM PhoneBook WHERE name = %s", (name,))
    elif choice == "2":
        phone = input("Enter the phone to search: ")
        cur.execute("SELECT * FROM PhoneBook WHERE phone = %s", (phone,))
    elif choice == "3":
        partial_name = input("Enter the partial name to search: ")
        cur.execute("SELECT * FROM PhoneBook WHERE name LIKE %s", (partial_name + '%',))
    else:
        print("Invalid choice!")
        return

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


def delete_data():
    conn = connect()
    cur = conn.cursor()
    print("1. Delete by name")
    print("2. Delete by phone")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name to delete: ")
        cur.execute("DELETE FROM PhoneBook WHERE name = %s", (name,))
    elif choice == "2":
        phone = input("Enter the phone to delete: ")
        cur.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone,))
    else:
        print("Invalid choice!")
        return

    conn.commit()
    print("Data deleted successfully!")
    cur.close()
    conn.close()


def delete_user(identifier):
    conn = connect()
    cur = conn.cursor()
    query = """
        DELETE FROM PhoneBook
        WHERE name = %s OR phone = %s
    """
    cur.execute(query, (identifier, identifier))
    conn.commit()
    if cur.rowcount > 0:
        print(f"User with identifier '{identifier}' deleted successfully!")
    else:
        print(f"No user found with identifier '{identifier}'.")
    cur.close()
    conn.close()


def view_data():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM PhoneBook")
    rows = cur.fetchall()

    if rows:
        print("\nPhoneBook Records:")
        print(f"{'ID':<5} {'Name':<20} {'Phone':<15}")
        print("-" * 40)
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<15}")
    else:
        print("\nNo records found in the PhoneBook.")

    cur.close()
    conn.close()


def get_records_by_pattern(pattern):
    conn = connect()
    cur = conn.cursor()
    query = """
        SELECT * FROM PhoneBook
        WHERE name ILIKE %s OR phone ILIKE %s
    """
    cur.execute(query, (f"%{pattern}%", f"%{pattern}%"))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


def get_records_with_pagination(limit, offset):
    conn = connect()
    cur = conn.cursor()
    query = """
        SELECT * FROM PhoneBook
        ORDER BY id
        LIMIT %s OFFSET %s
    """
    cur.execute(query, (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# menu
def main():
    create_table()
    while True:
        print("\nPhoneBook Menu:")
        print("1. Insert data from console")
        print("2. Insert data from CSV")
        print("3. Insert or update user")
        print("4. Insert many users")
        print("5. Query data by pattern")
        print("6. Query data with pagination")
        print("7. Delete user")
        print("8. View all data")  
        print("9. Exit")
        print("f  to new user")
        choice = input("Enter your choice: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            file_path = input("Enter the path to the CSV file: ")
            insert_from_csv(file_path)
        elif choice == "3":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            insert_or_update_user(name, phone)
        elif choice == "4":
            users = [
                {"name": "Alice", "phone": "12345"},
                {"name": "Bob", "phone": "67890"},
                {"name": "InvalidUser", "phone": "invalid_phone"}
            ]
            insert_many_users(users)
        elif choice == "5":
            pattern = input("Enter pattern to search: ")
            get_records_by_pattern(pattern)
        elif choice == "6":
            limit = int(input("Enter limit: "))
            offset = int(input("Enter offset: "))
            get_records_with_pagination(limit, offset)
        elif choice == "7":
            identifier = input("Enter name or phone to delete: ")
            delete_user(identifier)
        elif choice == "8":
            view_data() 
        elif choice == "9":
            print("Exiting...")
            break
        elif choice == "f":
            insert_user_new()
            print("probably done")
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()