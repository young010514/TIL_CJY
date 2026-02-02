N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        A.append(int(line[1]))
    else:
        A.append(0)


# Please write your code here.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head != None:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
        self.node_num += 1

    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail
        # 하나도 없을때
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        # 하나라도 있을 때
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        self.node_num += 1

    def pop_front(self):
        # 빈 리스트일때:
        if self.node_num == 0:
            print("empty list")
        elif self.node_num == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        else:
            temp = self.head
            self.head = temp.next
            self.node_num -= 1
            return temp.data
    def pop_back(self):
        # 빈 리스트일때:
        if self.node_num == 0:
            print("empty list")
        elif self.node_num == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        else:
            temp = self.tail
            self.tail = temp.prev
            self.node_num -= 1
            return temp.data
    def size(self):
        return self.node_num

    def empty(self):
        if self.node_num == 0 :
            return 1
        else:
            return 0

    def front(self):
        if self.head :
            return self.head.data
        else:
            print("empty list")
    def back(self):
        if self.tail :
            return self.tail.data
        else:
            print("empty list")

lst = DoublyLinkedList()

for com, data in zip(command, A):
    if com.strip() == 'push_back':
        lst.push_back(data)
    elif com.strip() == 'push_front':
        lst.push_front(data)
    elif com.strip() == 'pop_front':
        print(lst.pop_front())
    elif com.strip() == 'pop_back':
        print(lst.pop_back())
    elif com.strip() == 'size':
        print(lst.size())
    elif com.strip() == 'empty':
        print(lst.empty())
    elif com.strip() == 'front':
        print(lst.front())
    elif com.strip() == 'back':
        print(lst.back())