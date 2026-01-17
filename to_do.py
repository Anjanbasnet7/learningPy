#to do list 
task = [
  
]
def show():
    if not task:
        print("To do list is empty now.")
    else:
        for i, tasks in enumerate(task, start=1):
            statu = "✅" if tasks["status"] else "❌"
            print(i, tasks["task"], statu)

while True:
    print("""1.ADD\n2.MARK DONW TASK\n3.SHOW TASK\n4.EXIT""")
    
    chose = input("what you want(1/2/3):")
    if chose == "1":
        user_task = input("Enter task name:")
        task.append({"task": user_task, "status": False})
        print(f"Task {user_task} is added!")
    
    elif chose == "2":
        choseToMark = int(input("Chose to mark down:"))
        if 1<=choseToMark<=len(task):
            task[choseToMark - 1]["status"]= True
            print(f"Task {task[choseToMark -1]['task']}")

        else:
            print("Invalid choice")
            break

    elif chose == "3":
        show()
        print("\n")
        print("\n")
        print("\n")

    elif chose == "4":
        print("Good bye")
        break

    else:
        print("Invalid input!")





