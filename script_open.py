# this script will take care of only if i say "open _____" itll search and open given file/program,etc

"""
import os

def search_start_menu(value):
    # Path to the Start Menu folder
    start_menu_path = os.path.join(os.environ['APPDATA'], 'Microsoft\\Windows\\Start Menu')

    # Initialize a list to store found items
    found_items = []

    # Walk through all directories and subdirectories in the Start Menu
    for root, dirs, files in os.walk(start_menu_path):
        for file in files:
            # Check if the value is in the file name
            if value.lower() in file.lower():
                found_items.append(os.path.join(root, file))

    # Return the results
    return found_items

if __name__ == "__main__":
    # Set the search term
    search_term = "example"  # You can replace "example" with any term you want to search for

    # Search the Start Menu with the provided search term
    results = search_start_menu(search_term)

    # Print the results
    if results:
        print(f"Found {len(results)} item(s) in the Start Menu matching the term '{search_term}':")
        for item in results:
            print(item)
    else:
        print(f"No items found in the Start Menu matching the term '{search_term}'.")

"""

