import json
import sys

def choise_one():
    try:
        
        print(" enter 1 to show all data ")
    except Exception as err:
        print(err)
    print(" enter 2 to show one user ")
    print(" enter 3 to edit one user ")
    print(" enter 4 to delete one user ")
    print(" enter 5 to add one user ")
    print(" enter 6 to close app ")
    my_choise: int = int(input("plz enter number from 1 to 6 "))
    return my_choise


def search_one(my_id: object) -> int:
    with open("data.json", "r") as myfile:
        my_ls = json.load(myfile)
    place = -1
    for i, u in enumerate(my_ls):
        if u["ID"] == my_id:
            place = i
            break
    return place

def add_dat(x):
    try:
        ID = int(input("enter your ID "))


        for user in x:
            if user['ID'] == ID:
                print("Error: ID already exists. Please use a different ID.")
                return

    except ValueError:
        print("Invalid ID, please enter a valid ID.")
        return

    name = input("enter your name ")
    age = float(input("enter your age "))

    salary = input("enter your salary ")

    my_dict = {
        'name': name,
        'age': age,
        'ID': ID,
        'salary': salary,
    }
    x.append(my_dict)


    with open('data_with_duplicates.json', 'r') as file:
        data = json.load(file)


    unique_items = {}
    for item in data["items"]:
        unique_items[item["id"]] = item  # This will overwrite duplicates, keeping the last occurrence


    unique_items_list = list(unique_items.values())


    data["items"] = unique_items_list


    with open('cleaned_data.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("Duplicates removed and saved to cleaned_data.json")

    try:

        with open("data.json", 'w') as out_file:
            json.dump(x, out_file, indent=4)
        print("Data added successfully!")
    except Exception as err:
        print(f"An error occurred while writing to the file: ")

def edit_one():
    with open("data.json", "r") as myfile:
        my_ls = json.load(myfile)
    try:
        your_id = int(input("please enter Your Id :"))
    except ValueError:
        print("Invalid ID, please enter a valid number.")
        return
    place = search_one(your_id)
    if place == -1:
        print("Sorry, user not found.")
    else:
        name = input(f"Current name is {my_ls[place]['name']}, enter new name: ")
        age = input(f"Current age is {my_ls[place]['age']}, enter new age: ")
        salary = input(f"Current salary is {my_ls[place]['salary']}, enter new salary: ")
        my_ls[place]['name'] = name
        my_ls[place]['age'] = age
        my_ls[place]['salary'] = salary
        with open("data.json", 'w') as out_file:
            json.dump(my_ls, out_file, indent=4)
        print("User updated successfully.")


def delete_one():
    with open('data.json', "r") as myfile:
        my_ls = json.load(myfile)
    try:
        your_id = int(input('please enter Your Id :'))
    except ValueError:
        print("Invalid ID, please enter a valid number.")
        return
    place = search_one(your_id)
    if place == -1:
        print("Sorry, user not found.")
    else:
        my_ls.pop(place)
        with open("data.json", 'w') as out_file:
            json.dump(my_ls, out_file, indent=4)
        print("User deleted successfully.")


def show_all():
    with open("data.json", "r") as myfile:
        my_ls = json.load(myfile)
    for u in my_ls:
        print(u)


def show_one():
    with open("data.json", "r") as myfile:
        my_ls = json.load(myfile)
    try:
        your_id = int(input("please enter Your Id :"))
    except ValueError:
        print("Invalid ID, please enter a valid number.")
        return
    place = search_one(your_id)
    if place == -1:
        print("Sorry, user not found.")
    else:
        print(my_ls[place])


def close_file():
    sys.exit(0)



def start():
    my_ls = []
    while True:
        try:
            my_choise = choise_one()
        except Exception as err:
            print(err)
            continue

        if my_choise == 1:
            show_all()
        elif my_choise == 2:
            show_one()
        elif my_choise == 3:
            edit_one()
        elif my_choise == 4:
            delete_one()
        elif my_choise == 5:
            with open("data.json", "r") as myfile:
                my_ls = json.load(myfile)
            add_dat(my_ls)
        elif my_choise == 6:
            close_file()
            break


start()