#!/usr/bin/python3
"""Exports data in CSV format."""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    # Get the user ID from command-line arguments
    userId = sys.argv[1]

    # Fetch user data from the API
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(userId))
    
    # Extract the username from the user data
    name = user.json().get('username')
    
    # Fetch TODO list data from the API
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    # Define the filename for the CSV export
    filename = userId + '.csv'

    # Open the CSV file for writing
    with open(filename, mode='w') as f:
        # Initialize the CSV writer with specified settings
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        
        # Iterate through TODO list items and write them to the CSV file
        for task in todos.json():
            if task.get('userId') == int(userId):
                # Write a row with user ID, username, completion status, and task title
                writer.writerow([userId, name, str(task.get('completed')), task.get('title')])
