class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added: {task}")

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Completed: {task}")
        else:
            print("Task not found!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks to show!")
        for index, task in enumerate(self.tasks, 1):
            print(f"{index}. {task}")

    def run(self):
        while True:
            print("\nTo-Do List CLI")
            print("1. Add task")
            print("2. Complete task")
            print("3. List tasks")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                task = input("Enter the task to add: ")
                self.add_task(task)
            elif choice == "2":
                task = input("Enter the task to mark as completed: ")
                self.complete_task(task)
            elif choice == "3":
                self.list_tasks()
            elif choice == "4":
                print("You have left the Todo app!")
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    app = ToDoList()
    app.run()
