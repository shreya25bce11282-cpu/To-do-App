import tkinter as tk  #Imports the Tkinter GUI toolkit as tk for easier referencing of its classes and functions.
from tkinter import messagebox #Specifically imports the messagebox submodule for dialogue pop-ups
import os #Imports the os (Operating System) module, which allows the script to interact with the file system, specifically to check if the todo_list.txt file already exists.
import re # Imports the regular expressions module to clean up or search within task text strings

TODO_FILE = "todo_list.txt" #Sets the file name where tasks will be stored persistently on disk.

def load_tasks():
    tasks = [] #Initializes an empty list to hold the tasks.
    if os.path.exists(TODO_FILE): #Only try to load if the file exists.
        with open(TODO_FILE, 'r') as f: #Open the file and read lines, stripping whitespace/newlines.
            tasks = [line.strip() for line in f.readlines()]
    return tasks #Returns the list of loaded tasks

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f: #Opens the file for writing (overwriting).
        for task in tasks: #Loops through the task list, writing each one on a new line.
            f.write(task + '\n')


class TodoApp:
    def __init__(self, master):
        self.master = master # Stores the main window.
        master.title("📋 To-Do List") #Set the window title 
        master.geometry("500x400") # Set the initial window size
        
        # 1. Load the tasks from the file initially
        self.tasks = load_tasks()

        # 2. Setup the Main Widgets
        self.setup_widgets()
        
        # 3. Populate the Listbox
        self.refresh_task_list()

    def setup_widgets(self): #Creates and organizes all the GUI elements
        
        entry_frame = tk.Frame(self.master) #Frame to hold the entry and add button
        entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(entry_frame, width=35, font=('Arial', 12)) #Single line textbox for the user to type a new task
        self.task_entry.pack(side=tk.LEFT, padx=10)

        add_button = tk.Button(entry_frame, text="Add Task", command=self.add_task_gui, bg='#A8E6CF') #When clicked, triggers self.add_task_gui
        add_button.pack(side=tk.LEFT)
        
        # Task List Frame 
        list_frame = tk.Frame(self.master)
        list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # Scrollbar for the list
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox = tk.Listbox(
            list_frame, 
            height=15, 
            width=50, 
            font=('Arial', 11),
            yscrollcommand=scrollbar.set
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar.config(command=self.task_listbox.yview)

        #  Action Buttons Frame 
        button_frame = tk.Frame(self.master) #Holds the action buttons at the bottom.
        button_frame.pack(pady=10)

        complete_button = tk.Button(button_frame, text="Mark Complete", command=self.complete_task_gui, bg='#FFD3B5') #Marks selected task as done
        complete_button.pack(side=tk.LEFT, padx=10)

        
        clear_button = tk.Button(button_frame, text="Clear All", command=self.clear_all_tasks, bg='#C2F0FC') #Clears all tasks from the list
        clear_button.pack(side=tk.LEFT, padx=10)

        exit_button = tk.Button(button_frame, text="Exit & Save", command=self.exit_app, bg='#FF8C94') #Saves tasks and exits the app
        exit_button.pack(side=tk.LEFT, padx=10)
            
    # GUI Action Methods 
    #Clears the listbox and re-populates it with tasks from the list.
    def refresh_task_list(self):
        
        self.task_listbox.delete(0, tk.END) # Clear all current items
        
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task) # Insert each task into the listbox
            
            # Change the color of completed tasks
            if task.startswith("[DONE]"):
                task_index = self.tasks.index(task)
                self.task_listbox.itemconfig(task_index, {'fg': 'gray', 'bg': '#F0F0F0'}) # Gray out completed tasks
            else:
                # Add a light border/line to separate entries (optional, depends on platform)
                task_index = self.tasks.index(task)
                self.task_listbox.itemconfig(task_index, {'fg': 'black'})

    #Handles adding a new task from the entry field.
    def add_task_gui(self):
        
        task_desc = self.task_entry.get().strip()
        
        if task_desc:
            new_task = f"[ ] {task_desc}"
            self.tasks.append(new_task)
            self.task_entry.delete(0, tk.END) # Clear the entry field
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Task description cannot be empty.")
    #Marks the selected task as complete in the listbox.
    def complete_task_gui(self):
       
        try:
            # Get the index of the selected item in the listbox
            selected_indices = self.task_listbox.curselection()
            if not selected_indices:
                messagebox.showerror("Error", "Please select a task to complete.")
                return

            task_index = selected_indices[0]
            task = self.tasks[task_index]
            
            if task.startswith("[ ]"):
                # Use regex or simple replace to update the marker
                self.tasks[task_index] = re.sub(r"\[ \]", "[DONE]", task, 1)
                self.refresh_task_list()
            elif task.startswith("[DONE]"):
                messagebox.showinfo("Status", "Task is already complete.")
                
        except IndexError:
            # Should be caught by the selected_indices check, but good practice
            messagebox.showerror("Error", "No task selected.")

    def clear_all_tasks(self):
        confirm = messagebox.askokcancel("Clear All Tasks", "Are you sure you want to permanently delete all tasks?")
        if confirm:
            self.tasks = []
            self.refresh_task_list()
            save_tasks(self.tasks)

    #Saves the final list and closes the application.
    def exit_app(self):
        
        save_tasks(self.tasks)
        messagebox.showinfo("Save Status", "All tasks saved successfully!")
        self.master.destroy() # Close the main window

   
#Runs the app if the file is run directly.
#Makes the root Tkinter window, passes it to the TodoApp, and starts the event loop.
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()