#!/usr/bin/python3
"""
This script uses a REST API to retrieve information about
a given employee's TODO list progress.
"""
from requests import get
from sys import argv

if __name__ == '__main__':
    # Get the user ID as a command-line argument
    userId = argv[1]

    # Retrieve user information from the API
    user = get("https://jsonplaceholder.typicode.com/users/{}".format(userId))
    
    # Extract the user's name from the response
    name = user.json().get('name')

    # Retrieve TODO list data from the API
    todos = get('https://jsonplaceholder.typicode.com/todos')
    
    # Initialize variables to keep track of completed and total tasks
    totalTasks = 0
    completed = 0

    # Iterate through the TODO list to count completed tasks
    for task in todos.json():
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    # Print the progress information
    print('Employee {} has completed tasks ({}/{}) :'.format(name, completed, totalTasks))

    # Print the titles of completed tasks
    print('\n'.join(["\t " + task.get('title') for task in todos.json()
                     if task.get('userId') == int(userId) and task.get('completed')]))
