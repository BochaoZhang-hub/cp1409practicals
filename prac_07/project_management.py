import datetime
from projects import Project
FILENAME = "projects.txt"

def main():
    projects = load_projects(FILENAME)
    menu = """
    Welcome to Pythonic Project Management
    Loaded 5 projects from projects.txt
    - (L)oad projects  
    - (S)ave projects  
    - (D)isplay projects  
    - (F)ilter projects by date
    - (A)dd new project  
    - (U)pdate project
    - (Q)uit
    """
    print(menu)
    choice = input("Give your choice:")
    while choice.upper() != "Q":
        if choice.upper() == "L":
            pass
        elif choice.upper() == "S":
            save_project(projects)
        elif choice.upper() == "D":
            display_porject()
        elif choice.upper() == "F":
            pass
        elif choice.upper() == "A":
            pass
        elif choice.upper() == "U":
            pass
        else:
            print("invalid")
        print(menu)
        choice = input("another choice: ")


def save_project(projects):
    with open(FILENAME, "w") as out_file:
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                           f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_porject(projects):
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]
    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(f"{project}")
    print("Completed projects:")
    for project in sorted(complete):
        print(f"{project}")

def load_projects(FILENAME):
    projects = []
    with open(FILENAME, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            if len(parts) >= 5:
                name = parts[0]
                start_date = parts[1]
                priority = parts[2]
                cost_estimate = parts[3]
                completion = parts[4]
                project = Project(name, start_date, priority, cost_estimate, completion)
                projects.append(project)
    return projects