import math

class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, value):
        self.next_node = value
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
class Stack:
    def __init__(self, name):
        self.top_item = None
        self.size  = 0
        self.limit = 1000
        self.name = name

    def has_space(self):
        return self.size < self.limit
    
    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
    
    def get_name(self):
        return self.name
    
    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item

            self.size += 1
        else:
            print("No more space!")

    def pop(self):
        if not self.is_empty():
            item = self.top_item
            self.top_item = item.get_next_node()

            self.size -= 1
        else:
            print("Nothing to remove!")
        
    def peek(self):
        if not self.is_empty():
            print(self.top_item.get_value())
            return self.top_item.get_value()
        else:
            print("Nothing to see here!")

    def print_stack(self):
        print_list = []
        current_stack = self.top_item
        while current_stack:
            print_list.append(current_stack.get_value())
            current_stack = current_stack.get_next_node()
        print_list.reverse()
        print(f"{self.get_name()}: {print_list}")

num_disks = int(input("Number of disks you want to play!: "))

Left = Stack("Left Stack")
Mid = Stack("Middle Stack")
Right = Stack("Right Stack")
stacks = [Left, Mid, Right]
for i in range(num_disks, 0, -1):
    Left.push(i)

choices = ["l", "m", "r"]
stack_name = {
    "r": "Right Stacks",
    "m": "Middle",
    "l": "Left"
}

stack_value = {
    "r": Right,
    "m": Mid,
    "l": Left
}

def get_input():
    while True:
        for i in range(len(stacks)):
            print(f"{choices[i]} for {stack_name[choices[i]]}")

        user_input = input()
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]

if num_disks < 3:
    while num_disks < 3:
        num_disks = int(input("Input a number > 3: "))

while Right.get_size() < num_disks:
    print("\nCurrent Status...\n")
    for stack in stacks:
        stack.print_stack()

    print("\n")
    
    while True:
        print("\nWhich stack do you want to go from?\n")
        from_stack = get_input()

        if not from_stack.is_empty():
            print("\nWhich stack do you want to go to\n")
            to_stack = get_input()

            if to_stack.is_empty() or (to_stack.peek() > from_stack.peek()):
                disk = from_stack.top_item.get_value()
                to_stack.push(disk)
                from_stack.pop()

                break
            else:
                print("\n_____________Invalid Move_____________\n")
                break
        else:
            print("\n_____________From Stack has no disk_____________\n")
            break

print("__GAME ENDS__")