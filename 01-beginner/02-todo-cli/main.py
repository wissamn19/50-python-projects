"""
Command-line To-Do List
File I/O | Difficulty: Beginner

Concepts: functions, file I/O, JSON, CLI argument handling
"""
import sys
import json
from datetime import datetime



def usage():
  print("Your To-Do list is here!!, Choose the following Commands: ")
  print(''' ADD: To add a new task. 
        REMOVE: To remove any task. 
        LIST: To display all the tasks list. 
        DONE: To change the status of the task.
        ''')

usage()


def add_task():
  try:
     with open("data.json" , "r") as f:
      data = json.load(f)
  except (FileNotFoundError, json.JSONDecodeError):
    data = {}
  
  if len(data) == 0:
    new_id = "1"
  else:
     max_id = max(int(key) for key in data.keys())
     new_id = str(max_id + 1)

  
  data[new_id] = {
   'name': sys.argv[2] ,
   'status': 'Pending' , 
   'date': datetime.now().isoformat()
     }
  
  
  
  with open("data.json" , "w") as fp:
   json.dump(data , fp , indent=4)

  print(f"Task added with ID {new_id}: {sys.argv[2]}")



def remove_task():
 try:
   with open("data.json" , "r") as f:
    data = json.load(f)
 except(FileNotFoundError, json.JSONDecodeError):
   data = {}
  
 target_id = sys.argv[2]

 if target_id in data:
    deleted_name = data[target_id]['name'] 
    del data[target_id]
    print(f"Task removed: {deleted_name}")
 else:
   print(f"Error: Task ID {target_id} does not exist.")
     
 with open("data.json" , "w") as fp:
    json.dump(data , fp , indent=4)



def tasks_list():
  try:
   with open("data.json" , "r") as f:
    data = json.load(f)
  except (FileNotFoundError, json.JSONDecodeError):
    data = {}

  if not data:
    print("No tasks currently exist.")
    return

  print("To-do list:")
 
  for task_id, task_details in data.items():
    print(f"[{task_id}] - {task_details['name']} - Status: {task_details['status']} (Created: {task_details['date']})")



def done_tasks():
  try:
   with open("data.json" , "r") as f:
    data = json.load(f)
  except (FileNotFoundError, json.JSONDecodeError):
    data = {}

  tasks_id = sys.argv[2]

  if tasks_id in data:
    data[tasks_id]['status'] = 'Done'
    print(f"Task {tasks_id} marked as Done!")
  else:
    print(f"Error: Task ID {tasks_id} not found.")

  with open("data.json" , "w") as fp:
    json.dump(data , fp , indent=4)


    

if sys.argv[1] == 'add':
  add_task()
elif sys.argv[1] == 'remove':
  remove_task()
elif sys.argv[1] == 'list':
  tasks_list()
elif sys.argv[1] == 'done':
  done_tasks()
else:
  print('There is no command like that. Only ADD, REMOVE, LIST and DONE')