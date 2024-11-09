def find_item_in_list(item_list, target_item):
    # Traverse the list
    for item in item_list:
        if item == target_item:
            return True  # Item found
    return False  # Item not found

# Sample list and target item
item_list = [10, 20, 30, 40, 50]
target_item = int(input("Enter the item to search for: "))

# Check if the item is in the list
if find_item_in_list(item_list, target_item):
    print(f"{target_item} is present in the list.")
else:
    print(f"{target_item} is not present in the list.")
