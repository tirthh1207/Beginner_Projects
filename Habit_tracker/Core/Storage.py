import json
import os
from datetime import date

data = 'data'
habits_files = os.path.join(data,'Habit.json')
log_file = os.path.join(data, 'Logs.json')

def load_json(path):
    '''Loads data from a JSON file safely'''

    try:
        # if file dosent exist returns empty list
        if not os.path.exixts(path):
            return[]
        
        with open(path,'r') as f:
            content = f.read().strip()

            # if file is empty -> treates as empty list
            if content =='':
                return[]
            
            # try converting JSON -> Python
            return json.loads(content)
        
    except json.JSONDecodeError:
        print(f"ERROR: JSON file '{path}' is corrupted.")
        return []
    except Exception as e:
        print(f"Unexpected error while loading {path}: {e}")
        return []
    
def save_json(path, data):
    '''Saves Python data into a JSON file safely '''
    try:
        with open(path,'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
         print(f"ERROR while saving to {path}: {e}")

def initialize_files():
    '''Creates habits.json and log,json if they dont exist.'''
    os.mkdir(data, exist_ok=True)

    #if habits.json missing -> create it
    if not os.path.exists(habits_files):
        save_json(habits_files,[])

    # if logs.json missing -> create it
    if not os.path.exists(log_file):
        save_json(log_file,[])

def get_next_id(habits_list):
    '''Returns the next intiger ID based on existing habits.'''
    if not habits_list:
        return 1
    ids = [habit['id'] for habit in habits_list]
    return max(ids)+1

def add_habit(habit_obj):
    '''Appends a new habit to habit.json'''
    habits = load_json(habits_files)
    habits.append(habit_obj)
    save_json(habits_files,habits)

def add_log_entry(log_obj):
    '''Append a new log entry to logs.json'''
    logs= load_json(log_file)
    logs.append(log_obj)
    save_json(log_file,logs)

    