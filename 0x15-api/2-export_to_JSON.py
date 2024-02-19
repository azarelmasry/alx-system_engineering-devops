#!/usr/bin/python3
"""Exports data in JSON format."""

if __name__ == "__main__":
    import json
    import requests
    import sys

    # Get the user ID from command-line arguments
    userId = sys.argv[1]

    # Fetch user data from the API
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(userId))

    # Fetch TODO list data from the API and parse it as JSON
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    # Initialize dictionaries and lists for organizing the data
    todoUser = {}
    taskList = []

    # Iterate through TODO list items and extract relevant information
    for task in todos:
        if task.get('userId') == int(userId):
            taskDict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user.json().get('username')
            }
            taskList.append(taskDict)
    
    # Organize the data under the user's ID
    todoUser[userId] = taskList

    # Define the filename for the JSON export
    filename = userId + '.json'
    
    # Write the JSON data to the specified file
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)
