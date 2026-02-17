from datetime import datetime

def validate_task_title(title):
    # Trim whitespace
    new_title = title.strip()
    
    if not new_title :
        print("❌ Title cannot be empty.")
    
    if len(new_title) < 3  :
        print("❌ Task title cannot be less than 3 characters.")
        
    if len(new_title) > 100 :
        print("❌ Task title cannot be more than 100 characters.")
    
    return new_title
    
def validate_task_description(description):
    # Trim whitespace
    new_description = description.strip()
    
    if not new_description :
        print("❌ Description cannot be empty.")
    
    if len(new_description) > 500 :
        print("❌ Description cannot be more than 500 characters.")
    
    return new_description
    
def validate_due_date(due_date):
    # Trim whitespace
    new_due_date = due_date.strip()
    
    if not new_due_date :
        print("❌ Date cannot be empty.")
    
    return new_due_date