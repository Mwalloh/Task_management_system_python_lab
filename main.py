# Import functions from task_manager.task_utils package
from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

# Define the main function
def main():
    while True:
        print("⏰ --------------------------- ⏳")
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            title = input("Input task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date (YYYY, MM, DD): ")
            
            add_task(title, description, due_date)
            
        elif choice == "2" :
            try :
                index = int(input("Enter the position of the task to be marked as complete in the list, where the first item's position is 0 (zero): "))
            except IndexError:
                print("Invalid input. Enter a valid number.")
            else :
                mark_task_as_complete(index)
        
        elif choice == "3" :
            view_pending_tasks()
        
        elif choice == "4" :
            progress = calculate_progress()
            print(progress)
            
        elif choice == "5":
            print("Exiting the program...")
            break
        
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
