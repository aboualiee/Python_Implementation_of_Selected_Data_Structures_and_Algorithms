import argparse
from datetime import datetime
from Complain import Dlinkedlist

# Initialize the doubly linked list
dlist = Dlinkedlist()
dlist.dataset()

def add_to_end(data, priority, timestamp):
    dlist.add_to_end(data, priority, datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S'))
    print("Node added.")
    print_list()

def delete_by_index(index):
    dlist.delete_by_index(index)
    print(f"Node at index {index} deleted.")
    print_list()

def update_by_index(index, data, priority, timestamp):
    dlist.update_by_index(index, data, priority, datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S'))
    print(f"Node at index {index} updated.")
    print_list()

def sort_list(attribute):
    dlist.sort(attribute)
    print(f"List sorted by {attribute}.")
    print_list()

def print_list():
    print("Current list:")
    dlist.printlist()

def filter_by_attribute(attribute, value):
    print(f"Filtering list by {attribute} = {value}:")
    dlist.filter_by_attribute(attribute, value)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage your doubly linked list.")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new node to the end of the list")
    add_parser.add_argument("data", type=str, help="Data for the new node")
    add_parser.add_argument("priority", type=int, help="Priority for the new node")
    add_parser.add_argument("timestamp", type=str, help="Timestamp for the new node (format: 'YYYY-MM-DD HH:MM:SS')")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a node by index")
    delete_parser.add_argument("index", type=int, help="Index of the node to delete")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update a node by index")
    update_parser.add_argument("index", type=int, help="Index of the node to update")
    update_parser.add_argument("data", type=str, help="New data for the node")
    update_parser.add_argument("priority", type=int, help="New priority for the node")
    update_parser.add_argument("timestamp", type=str, help="New timestamp for the node (format: 'YYYY-MM-DD HH:MM:SS')")

    # Sort command
    sort_parser = subparsers.add_parser("sort", help="Sort the list by an attribute")
    sort_parser.add_argument("attribute", type=str, choices=["priority", "timestamp"], help="Attribute to sort by")

    # Print command
    print_parser = subparsers.add_parser("print", help="Print the list")

    # Filter command
    filter_parser = subparsers.add_parser("filter", help="Filter the list by an attribute")
    filter_parser.add_argument("attribute", type=str, choices=["priority", "timestamp"], help="Attribute to filter by")
    filter_parser.add_argument("value", type=str, help="Value to filter by")

    args = parser.parse_args()

    if args.command == "add":
        add_to_end(args.data, args.priority, args.timestamp)
    elif args.command == "delete":
        delete_by_index(args.index)
    elif args.command == "update":
        update_by_index(args.index, args.data, args.priority, args.timestamp)
    elif args.command == "sort":
        sort_list(args.attribute)
    elif args.command == "print":
        print_list()
    elif args.command == "filter":
        filter_by_attribute(args.attribute, args.value)