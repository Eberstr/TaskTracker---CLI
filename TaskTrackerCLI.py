import json
import os
import argparse
from datetime import datetime


APP_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_DIR = os.path.join(APP_DIR, 'tasks.json')

def read_json():
    if os.path.exists(JSON_DIR):
        with open(JSON_DIR, 'r') as j:
            return json.load(j)
    else:
        print("JSON file does not exist")
        create_json_file()
        with open(JSON_DIR, 'r') as j:
            return json.load(j)

def write_json(data):
    with open(JSON_DIR, "w") as f:
        json.dump(data, f, indent=4)

def create_json_file():
        with open(JSON_DIR, "w") as j:
            json.dump({'tasks': []}, j, indent=4)
        print("Json file Created")

def create_task(task):
    data = read_json()
    
    tasks_id = [task['id'] for task in data['tasks']]
    new_task = {'id': len(tasks_id)+1, \
                'description': task, \
                'status': 'new', \
                'createdAt': datetime.now().strftime('%d-%m-%Y, %H:%M:%S.%f'), \
                'updatedAt': datetime.now().strftime('%d-%m-%Y, %H:%M:%S.%f')
                }
    
    data['tasks'].append(new_task)

    write_json(data)

    print(f'Task {task} has been created')    

def update_task(id, task):
    data = read_json()

    json_task = next((task for task in data['tasks'] if task['id'] == id), None)

    if json_task:
        json_task['description'] = task
        json_task['updatedAt'] = datetime.now().strftime('%d-%m-%Y, %H:%M:%S.%f')

        write_json(data)
        print('Task updated:', task)
    else:
        print(f'ID {id} doesn´t exist')

def delete_task(id):
    data = read_json()

    if any(task['id'] == id for task in data['tasks']):
        data['tasks'].pop(id - 1)
        print(f'Task {id} deleted')
    else:
        print(f'Task {id} doesn´t exist')
    write_json(data)

def list_tasks():
    pass

def clear_tasks():
    pass

def main():    
    while True:
        command = input('task-cli ').strip().lower()
        command = command.split()

        match command:
            case ['add', *task]:
                create_task(' '.join(task))
            case ['update', id, *task]:
                update_task(int(id), ' '.join(task))
            case ['delete', id]:
                delete_task(int(id))
            case ['exit']:
                print('Closing program...')
                break
            case _:
                print("Unkown command")   
    
if __name__ == '__main__':
    main()