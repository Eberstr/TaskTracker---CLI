import json
import os
import argparse

def create_json_file():
    app_dir = os.path.dirname(os.path.abspath(__file__))
    json_dir = os.path.join(app_dir, "tasks.json")

    if os.path.exists(json_dir):
        with open(json_dir, "r") as j:
            data = json.load(j)
    else:
        with open(json_dir, "w") as j:
            json.dump({'tasks': ['test']}, j, indent=4)

def create_task():
    pass

def update_task():
    pass

def delete_task():
    pass

def list_tasks():
    pass

def clear_tasks():
    pass