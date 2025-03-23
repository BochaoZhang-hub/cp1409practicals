import datetime
from projects import Project
FILENAME = "projects.txt"

def main():

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
            projects = load_projects(FILENAME)
        elif choice.upper() == "S":
            save_project(projects)
        elif choice.upper() == "D":
            display_porject()
        elif choice.upper() == "F":
            pass
        elif choice.upper() == "A":
            new_project = add_new_project()
            projects.append(new_project)
        elif choice.upper() == "U":
            pass
        else:
            print("invalid")
        print(menu)
        choice = input("another choice: ")

def add_new_project():
    """This function will ask the user to prompt in a new project"""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    percentage_of_completion = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost, percentage_of_completion)


def save_project(projects):
    """This function will save the project to the txt"""
    with open(FILENAME, "w") as out_file:
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                           f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_porject(projects):
    """This function will display the project"""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]
    complete.sort()
    incomplete.sort()
    print("complete projects:")
    for project in complete:
        print(f"{project}")
    for project in incomplete:
        print(f"{incomplete}")

def load_projects(FILENAME):
    """This function will load the txt file and save it into list"""
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