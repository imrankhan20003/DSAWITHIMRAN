q=[]
def Enqueue():
    if len(q)==size:
        print("Queue is full!!!!")
    else:
        element = input("Enter the element:")
        q.append(element)
        print(element,"is addad to the Queue!")
def dequeue():
    if not q:
        print("Queue is empty !!!")
    else:
        e=q.pop(0)
        print("element removed!!!",e)
def display():
        print(q)
size=int(input("Enter the size if Queue:"))
while True:
    print("Select the Operational: 1. Add 2. Delete 3. Display 4. Quet")
    choice=int(input())
    if choice==1:
        Enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Invalid Option!!!")