📋 To-Do List Application
Overview of the Project
This project is a simple, desktop To-Do List application built using Python and the Tkinter library for the graphical user interface (GUI). It provides a straightforward way for users to manage their daily tasks. Tasks are persisted (saved) to a local file named todo_list.txt upon exit and automatically loaded when the application starts.

Features
1. Add Tasks: Users can quickly add new tasks via an input field and an "Add Task" button.

2. View Tasks: All current tasks are displayed in a scrollable listbox.

3. Persistence: Tasks are automatically loaded from todo_list.txt on startup and saved back to the file on exit.

4. Mark Complete: Users can select a task and mark it as complete, visually greying it out in the list to distinguish completed items. The task is internally prepended with [DONE].

5. Clear All: Option to permanently delete all tasks from the list and the save file.

6. Exit & Save: A dedicated button to ensure the current task list is saved before closing the application.

Technologies/Tools Used

Component,Tool/Library,Description
Programming Language,Python 3,The core language used for the application logic.
GUI Library,Tkinter,Python's standard GUI toolkit for creating the desktop interface.
File System Interaction,os module,Used for checking file existence and interacting with the local file system.
String Operations,re module,"Used for regular expressions, specifically to update the task marker from [ ] to [DONE]."

Steps to Install & Run the Project
1. Prerequisites: Ensure you have Python 3 installed on your system. Tkinter is typically included with standard Python installations.

2. Save the Code: Save the provided code as a Python file (e.g., todo_app.py).

3. Run the Application: Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the following command:
4. python todo_app.py

5. The To-Do List GUI window should open.
  
      Instructions for Testing
1. Adding a Task: Type a description (e.g., "Buy groceries") into the entry field and click "Add Task". The task should appear in the list with [ ] at the start.

2. Persistence Test:

Add a few tasks.

Click the "Exit & Save" button.

Rerun the application (python todo_app.py). The previously added tasks should load automatically.

3. Marking Complete:

Click on a task in the listbox to select it.

Click the "Mark Complete" button.

The task should change color (e.g., grey) and be prefixed with [DONE].

4. Error Handling:

Try clicking "Add Task" with an empty entry field; a warning message should appear.

Try clicking "Mark Complete" without selecting a task; an error message should appear.

5. Clearing Tasks: Click the "Clear All" button and confirm. The list should become empty, and the todo_list.txt file should be emptied upon exit.
