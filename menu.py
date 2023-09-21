"""
A menu - you need to add the database and fill in the functions. 
"""

# TODO create database table OR set up Peewee model to create table

import sqlite3

database = 'juggling_records_db.sqlite'

def build_record_table():
    try:
        with sqlite3.connect(database) as records:
            records.execute('create table chainsaw_records (Name text, Country text, Catches int)')
    except sqlite3.Error as e:
        print(f'Error creating table: {e}')
    finally:
        records.close()


def main():

    # Create the database
    build_record_table()

    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    # print('todo display all records')
    try:
        records = sqlite3.connect(database) 
        for record in records.execute('select * from chainsaw_records'):
            print(record)
    except sqlite3.Error as e:
        print(f'Error retrieving data: {e}')
    finally:
        records.close()

def search_by_name():
    print('todo ask user for a name, and print the matching record if found. What should the program do if the name is not found?')
    
    record_holder = input('Please enter a Chainsaw Juggler\'s name to find their Record: ').strip()
    while record_holder == '':
        record_holder = input('Please enter a Chainsaw Juggler\'s name to find their Record: ').strip()

    get_records_by_name = 'SELECT * FROM chansaw_records WHERE Name = ?'

    try:
        records = sqlite3.connect(database)
        record_cursor = records.execute(get_records_by_name, (record_holder, ) )
        record = record_cursor.fetchall()
        print(record)
    except sqlite3.Error as e:
        print(f'Error retreiving Record: {e}')
    finally:
        records.close()


def add_new_record():
    # print('todo add new record. What if user wants to add a record that already exists?')

    holder_name = input('Please enter the Chainsaw Juggler\'s name: ').strip()

    while holder_name == '':
        holder_name = input('Please enter the Chainsaw Juggler\'s name: ').strip()

    holder_country = input('Please enter the Chainsaw Juggler\'s country: ').strip()

    while holder_country == '':
        holder_country = input('Please enter the Chainsaw Juggler\'s country: ').strip()

    holder_catches = input('Please enter number of the Chainsaw Juggler\'s catches: ').strip()

    while holder_catches.isnumeric is False or holder_catches == '':
        holder_catches = input('Please enter number of the Chainsaw Juggler\'s catches: ').strip()

    holder_catches = int(holder_catches)

    add_new_record = 'INSERT INTO * chansaw_records(Name, Country, Catches) VALUES(?, ?, ?)'

    try:
        with sqlite3.connect(database) as add_records:
            add_records.execute(add_new_record, (holder_name, holder_country, holder_catches ) )
            add_records.commit
            print(f'Record added: Name = {holder_name} Country = {holder_country} Catches = {holder_catches}')
    except sqlite3.Error as e:
        print(f'Error adding record: {e}')
    finally:
        add_records.close()


def edit_existing_record():
    print('todo edit existing record. What if user wants to edit record that does not exist?')

    holder_name = input('Please enter the Chainsaw Juggler\'s name to edit: ').strip()

    while holder_name == '':
        holder_name = input('Please enter the Chainsaw Juggler\'s name to edit: ').strip()

    

    holder_catches = input('Please enter the updated number of the Chainsaw Juggler\'s catches: ').strip()

    while holder_catches.isnumeric is False or holder_catches == '':
        holder_catches = input('Please enter the updated number of the Chainsaw Juggler\'s catches: ').strip()

    holder_catches = int(holder_catches)

    edit_record = ' UPDATE tasks SET priority = ? , begin_date = ? , end_date = ? WHERE id = ?'

    try:
        with sqlite3.connect(database) as edit_records:
            edit_records.execute(add_new_record, (holder_name, holder_country, holder_catches ) )
            edit_records.commit
            print(f'Record added: Name = {holder_name} Country = {holder_country} Catches = {holder_catches}')
    except sqlite3.Error as e:
        print(f'Error adding record: {e}')
    finally:
        add_records.close()


def delete_record():
    print('todo delete existing record. What if user wants to delete record that does not exist?') 


if __name__ == '__main__':
    main()

# @Mr-3rd
 