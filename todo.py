def display_list():
  if not todo_list:
    print("Your ToDo list is empty.")
  else:
    print("Current ToDo list: ")
    for task in todo_list:
      print(f"- {task}")

todo_list = []

while True:

  print("Options:")
  print("1) Add Task")
  print("2) Remove Task")
  print("3) Display List")
  print("4) Quit")

  choice = input("Choose option (1, 2, 3, or 4): ")

  if choice == "1":
    print("Adding task")
    new_task = input("Enter the task you want to add: ")
    todo_list.append(new_task)
    print("Task is added to list")
    display_list()
  elif choice == "2":
    if todo_list == []:
      print("Your ToDo list is empty.")
    else:
      removed_task = todo_list.pop()
      print(f"Removed task: {removed_task}")
      display_list()
  elif choice == "3":
    display_list()    
  elif choice == "4":
    print("Quitting")
    break
