import csv
import os

FILE = r"C:\Users\karth\OneDrive\csvproject.csv"

def init_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Dept", "Marks"])

def read_data():
    data = []
    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def write_data(data):
    with open(FILE, "w", newline="") as f:
        fieldnames = ["ID", "Name", "Dept", "Marks"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def add_student():
    data = read_data()

    new = {
        "ID": input("Enter ID: "),
        "Name": input("Enter Name: "),
        "Dept": input("Enter Dept: "),
        "Marks": input("Enter Marks: ")
    }

    data.append(new)
    write_data(data)
    print("Added Successfully !!!")

def view_students():
    data = read_data()
    print("\n--- Students ---")
    for d in data:
        print(d)

def update_student():
    data = read_data()
    sid = input("Enter ID to update: ")

    for d in data:
        if d["ID"] == sid:
            print("Found:", d)
            d["ID"] = input("New ID: ")
            d["Name"] = input("New Name: ")
            d["Dept"] = input("New Dept: ")
            d["Marks"] = input("New Marks: ")
    write_data(data)
    print(" Updated Sucessfully !!!")

def delete_student():
    data = read_data()
    sid = input("Enter ID to delete: ")

    data = [d for d in data if d["ID"] != sid]

    write_data(data)
    print(" Deleted Sucessfully")

def menu():
    init_file()

    while True:
        print("\n1.Add")
        print("2.View")
        print("3.Update")
        print("4.Delete")
        print("5.Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            add_student()
        elif ch == "2":
            view_students()
        elif ch == "3":
            update_student()
        elif ch == "4":
            delete_student()
        elif ch == "5":
            print("Exit ")
            print("Good Bye")
            break
        else:
            print(" Invalid choice .Try Again !!")

menu()