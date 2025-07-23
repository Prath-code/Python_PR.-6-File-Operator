import time
import random


def write_entry(filename, entry):
    with open(filename, "a") as file:
        file.write(f"{entry}\n")


def read_entries(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def search_entry(filename, keyword):
    entries = read_entries(filename)
    matching_entries = [entry for entry in entries if keyword.lower() in entry.lower()]
    return matching_entries


def delete_all_entries(filename):
    try:
        with open(filename, "w") as file:
            file.write("")
        return True
    except FileNotFoundError:
        return False


def main():
    filename = "journal.txt"
    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("0. Exit")

        choice = input("User Input: ")

        if choice == "1":
            entry = input("Enter your journal entry: ")
            write_entry(filename, entry)
            print("Entry added successfully!")

        elif choice == "2":
            entries = read_entries(filename)
            if entries:
                print("Output (If the file exists):")
                for entry in entries:
                    print(entry.strip())
            else:
                print("Output (If the file does not exist):")
                print("No journal entries found. Start by adding a new entry!")

        elif choice == "3":
            keyword = input("Enter a keyword or date to search: ")
            matching_entries = search_entry(filename, keyword)
            if matching_entries:
                print("Output (If a match is found):")
                for entry in matching_entries:
                    print(entry.strip())
            else:
                print("Output (If no match is found):")
                print(f"No entries were found for the keyword: {keyword}")

        elif choice == "4":
            confirmation = input(
                "Are you sure you want to delete all entries? (yes/no): "
            )
            if confirmation.lower() == "yes":
                if delete_all_entries(filename):
                    print("Output (If the file is deleted successfully):")
                    print("All journal entries have been deleted!")
                else:
                    print("Output (If the file does not exist):")
                    print("No journal entries to delete.")
            else:
                print("Deletion cancelled.")

        elif choice == "0":
            print("Thank you for using Personal Journal Manager. Goodbye!")
            print("Exiting the program...")
            time.sleep(random.randint(1, 6))  # Simulate a delay before exit
            break

        else:
            print("Invalid option. Please select a valid option from the menu.")


if __name__ == "__main__":
    main()
