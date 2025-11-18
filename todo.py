
import os #Imports the os (Operating System) module, which allows the script to interact with the file system, specifically to check if the todo_list.txt file already exists.
import tkinter as tk
from tkinter import messagebox
import re # Used for cleaning up the task string

TODO_FILE = "todo_list.txt" # Defines a constant variable for the name of the file used to store the tasks.



#Defines the function responsible for loading tasks.
def load_tasks():
   
    tasks = [] #Initializes an empty list to store the tasks read from the file
    
    if os.path.exists(TODO_FILE): #Checks if the file specified by TODO_FILE exists in the current directory.
        with open(TODO_FILE, 'r') as f: #Opens the file in read mode ('r'). The with statement ensures the file is automatically closed, even if errors occur. f is the file object.
            
            tasks = [line.strip() for line in f.readlines()]  #This is a list comprehension that reads every line (f.readlines()) in the file, removes the newline character (\n) and any extra spaces from both ends (line.strip()), and puts the clean task string into the tasks list.
    return tasks #Returns the list of tasks.

#Defines the function responsible for saving tasks
def save_tasks(tasks):
    
    with open(TODO_FILE, 'w') as f: #Opens the file in write mode ('w'). This mode overwrites the file every time, ensuring the file reflects the current list exactly
       
        for task in tasks: #Loops through every task string in the input tasks list.
            f.write(task + '\n') #Writes the task string to the file, followed by a newline character (\n) so the next task starts on a new line.
class TodoApp:
    def __init__(self, master):
        self.master = master
        master.title("📋 Simple GUI To-Do List")
        master.geometry("500x400") # Set the initial window size
        
        # 1. Load the tasks from the file initially
        self.tasks = load_tasks()

        # 2. Setup the Main Widgets
        self.setup_widgets()
        
        # 3. Populate the Listbox
        self.refresh_task_list()
#Defines the function to display tasks
def view_tasks(tasks):
    #Checks if the tasks list is empty and prints a message if it is, then exits the function.
    if not tasks:
        print("\n📝 Your To-Do list is empty!")
        return

    print("\n--- Current To-Do List ---")
    for i, task in enumerate(tasks): #Loops through the list, using enumerate to get both the index (i) and the value (task) of each item.
        
        print(f"[{i + 1}] {task}") #Uses an f-string to print the task number (index + 1) and the task content.
    print("--------------------------")

#Defines the function to add a new task
def add_task(tasks):
    
    task_desc = input("Enter the new task description: ").strip() #Prompts the user for input and uses .strip() to remove accidental spaces.
    if task_desc: #Ensures the user didn't enter an empty task.
       
        new_task = f"[ ] {task_desc}" #Creates the task string with the [ ] marker indicating it's incomplete.
        tasks.append(new_task) #Adds the new task string to the end of the tasks list.
        save_tasks(tasks) #Calls the save function to immediately write the updated list to the file.
        print(f"✅ Added: '{task_desc}'")
    else:
        print("❌ Task cannot be empty.")

#Defines the function to mark a task as complete
def complete_task(tasks):
    
    view_tasks(tasks)
    if not tasks:
        return

    try: #Starts a block of code that is tested for errors (like entering text instead of a number)
       
        task_num = int(input("Enter the number of the task to mark complete: ")) #Takes user input and attempts to convert it to an integer.
        
       
        task_index = task_num - 1 #Converts the user-friendly number (starting at 1) to the list's zero-based index.

        if 0 <= task_index < len(tasks): #Validation to ensure the entered index is within the valid range of the list.
            task = tasks[task_index]
            
            # Simple check/replacement logic
            if task.startswith("[ ]"): #Checks if the task is currently incomplete
                # Replace the incomplete marker with the completed marker
                tasks[task_index] = task.replace("[ ]", "[DONE]", 1) #Replaces the [ ] marker with [DONE]. The 1 ensures only the first occurrence is replaced (the one at the start).
                save_tasks(tasks)
                print(f"🎉 Task {task_num} marked as complete!")
            elif task.startswith("[DONE]"):
                print(f"Task {task_num} is already complete.")
            else:
                # Fallback for unexpected format
                tasks[task_index] = "[DONE] " + task
                save_tasks(tasks)
                print(f"🎉 Task {task_num} marked as complete!")
        else:
            print(f"❌ Invalid number. Please enter a number between 1 and {len(tasks)}.")
    except ValueError: #Handles the error if the user input cannot be converted to an integer.
        print("❌ Invalid input. Please enter a number.")
        

#Defines the primary function that controls the application flow
def main():
    
    tasks = load_tasks() #The first action: loads any existing tasks from the file into the tasks list.
    print("Welcome to the Simple Command-Line To-Do List!")
    
    while True: #Starts an infinite loop to keep the menu running until the user chooses to exit.
        print("\n--- Menu ---")
        print("1. View To-Do List")
        print("2. Add New Task")
        print("3. Mark Task as Complete")
        print("4. Exit and Save")
        
        choice = input("Enter your choice (1-4): ") #Gets the user's menu choice as a string.

        #A series of if/elif statements that call the corresponding task function based on the user's input.
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            save_tasks(tasks) # Save one last time
            print("👋 Tasks saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")

#This standard Python construct ensures that the main() function is only called when the script is run directly (not when it's imported as a module into another script).
if __name__ == "__main__":
    main()
