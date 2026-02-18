from datetime import datetime

def validate_task_title(title):
    # Trim whitespace
    title = title.strip()
    
    if not title :
        raise ValueError ("❌ Title cannot be empty.")
    
    if len(title) < 3  :
        raise ValueError("❌ Task title cannot be less than 3 characters.")
        
    if len(title) > 100 :
        raise ValueError("❌ Task title cannot be more than 100 characters.")
    
    return title
    
def validate_task_description(description):
    # Trim whitespace
    description = description.strip()
    
    if not description :
        raise ValueError("❌ Description cannot be empty.")
    
    if len(description) > 500 :
        raise ValueError("❌ Description cannot be more than 500 characters.")
    
    return description
    
def validate_due_date(due_date):
    # Trim whitespace
    due_date = due_date.strip()
    
    if not due_date :
        raise ValueError("❌ Date cannot be empty.")
    
    return due_date