tasks = {"No Tasks here :)"}

def Task_is_Done(t):
    if t in tasks:
        tasks.remove(t)
        tasks.add(t + "   ==============    TASK IS DONE +++ :)")
    else:
        print("     THIS TASK DOESN'T EXIST")
    return 0
def Add_Task(t):
    if t not in tasks:
        tasks.add(t)
    else:
        print("     TASK IS ALREADY IN THE DESK")
    return 0
def check():
    mess = "  ---  #NEED TO COMPLETE# "
    for task in tasks:
        if (task[-2] + task[-1]) != ":)":
            print(task, mess)
        else:
            print(task)
    return 0
def Del(t):
    if t in tasks:
        tasks.remove(t)
    else:
        print("     THIS TASK DOESN'T EXIST")
    return 0
def Del_All_Compleated():
    k = 0
    targ = ""
    for T in tasks:
        if (T[-2] + T[-1]) == ":)":
            k += 1
            targ = T
    if k > 0:
        Del(targ)
    if k > 0:
        Del_All_Compleated()
    if k == 0:
        for task in tasks:
            print(task, "               **")
IsBoardEmpty = (tasks == {})
Switch = True
while ((not IsBoardEmpty) and Switch):
    print("print a task and the move (add, rem, ch, Del, Del all, Switch)")
    print()
    Task, do = input(), input()
    if do == ("add" or "Add"):
        Add_Task(Task)
        for task in tasks:
            print(task)
    elif do == ("rem" or "Rem"):
        Task_is_Done(Task)
        for task in tasks:
            print(task)
    elif do == ("ch" or "Ch"):
        check()
    elif do == ("Switch"):
        Switch = False
    elif do == ("Del"):
        Del(Task)
        for task in tasks:
            print(task)
    elif do == "Del all":
        Del_All_Compleated()
    else:
        print("pls choose a correct move")
    if IsBoardEmpty:
        print("*EMPTY*")
    print()
if not Switch:
    print("*" * 8, "  PROG IS CLOSED FR  ", "*" * 8)
