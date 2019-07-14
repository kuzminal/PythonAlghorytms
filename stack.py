MyStack = []
StackSize = 3

def DisplayStack():
    print("Сейчас стек содержит:")
    for Item in MyStack:
        print(Item)

def Push(Value):
    if len(MyStack) < StackSize:
        MyStack.append(Value)
    else:
        print("Стек заполнен!")

def Pop():
    if len(MyStack) > 0 :
        print("Снятие со стека: ", MyStack.pop())
    else:
        print("Стек пуст")


Push(1)
Push(2)
Push(3)

DisplayStack()

Push(4)
Pop()
DisplayStack()

Pop()
Pop()
Pop()