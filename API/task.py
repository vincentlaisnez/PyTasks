import os
from pathlib import Path
import logging
import json

logging.basicConfig(level=logging.DEBUG)
TASKS_DIR = os.path.join(Path.home(), ".todo")
TASKS_FILEPATH = os.path.join(TASKS_DIR, "tasks.json")


def get_tasks():
    if os.path.exists(TASKS_FILEPATH):
        with open(TASKS_FILEPATH, "r") as f:
            return json.load(f)
    return {}


def add_task(name):
    tasks = get_tasks()
    if name in tasks.keys():
        logging.error("une tâche avec le même nom existe déjà")
        return False

    tasks[name] = False
    _write_tasks_to_disk(tasks=tasks)
    return True


def remove_task(name):
    tasks = get_tasks()
    if name not in tasks:
        logging.error("La tâche n'existe pas dans le dictionnaire.")
        return False

    del tasks[name]
    _write_tasks_to_disk(tasks=tasks)
    return True


def _write_tasks_to_disk(tasks):
    if not os.path.exists(TASKS_DIR):
        os.makedirs(TASKS_DIR)
    with open(TASKS_FILEPATH, "w") as f:
        json.dump(tasks, f, indent=4)
        logging.info("Les tâches ont bien été mises à jour.")


if __name__ == '__main__':
    t = remove_task("Apprendre le python")
    print(t)