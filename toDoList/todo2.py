class ToDo:
    def __init__(self):
        self.work = []
        
    def add_work(self, work):
        self.work.append(work)
        print(f"Added: {work}")
        
    def complete_work(self, work):
        if work in self.work:
            self.work.remove(work)
            print(f"You have completed: {work}")
        else:
            print("Please add a task or work to be done")
    
    def list_work(self):
        if not self.work:
            print("No task to show here")
        for index, work in enumerate(self.work, 1):
            print(f"{index}. {work}")
            
    def run(self):
        while True:
            print("\nTO-DO List")
            print("1. Add task")
            print("2. Complete one of your task")
            print("3. List task")
            print("4. Exit app")
            choice = input("Enter your choice from(1-4) ")
        
            if choice =="1":
                work = input("Enter the task to be added ")
                self.add_work(work)
            elif choice =="2":
                work = input("Enter the task to be marked as completed ")
                self.complete_work(work)
            elif choice == "3":
                self.list_work()
            elif choice == "4":
                print("You have left the app")
                break
            else:
                print("Invalid choice!!")
                
if __name__ == "__main__":
    app = ToDo()
    app.run()