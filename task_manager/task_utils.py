from datetime import datetime

# Import validation functions
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = [{'title':'Task 1', 'description':'testing','due_date':'2024_05_26','completed': True},{'title':'Task 2', 'description':'testing','due_date':'2024_05_26','completed': False}]

# Implement add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title) :
        print("Invalid title.")
        return 
    
    if not validate_task_description(description) :
        print("Invalid description.")
        return
    
    if not validate_due_date(due_date) :
        print("Invalid date format.")
        return
    
    tasks.append({'title': title, 'description': description, 'due_date': due_date})
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):    
    if len(tasks) == 0 :
        print("You have no tasks. Add tasks to proceed.")
        return
    elif index >= len(tasks) :
        print("Task with the index does not exist.")
        return
    else :
        tasks[index]['completed'] = True
        print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    for task in tasks :
        if 'isComplete' not in task.keys() :
            print(task)

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    completed_tasks = []
    
    for task in tasks :
        if task['completed'] == True :
            completed_tasks.append(task)
            
    progress = (len(completed_tasks)/ len(tasks)) * 100
    return progress
