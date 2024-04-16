# node
# class Node:
#     def __init__(self,item=None,nextnode=None):
#         self.item = item
#         self.nextnode = id(nextnode)

#     def __str__(self):
#         return f'Item : {self.item},Nextnode : {self.nextnode}'



# item = Node(5)
# item2 = Node(10,item)

# print(item2)

# def sum(x):
#     total =  0
#     for num in range(x + 1):
#         total += num
#     return total
    

# print(sum(5))

# singly linked list code

class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
    
class SLL:
    def __init__(self,start=None):
        self.start = start

    def is_empty(self):
        return self.start == None
          
    def insert_at_start(self,data):
        node = Node(data,self.start)
        self.start = node
    
    def insert_at_last(self,data):
        node = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                 temp = temp.next
            temp.next = node
        else:
            self.start = node
    
    def search_item(self,item):
        if not self.is_empty():
            find_index = self.start
            while find_index is not None:
                if find_index.item == item:
                    return find_index
                find_index = find_index.next
            return 'Item not found'
        
    def insert_after(self,data):
        node = Node(data)
        if not self.is_empty():
            find_index = self.start
            while find_index is not None:
                if find_index.item == item:
                    return find_index
                find_index = find_index.next
            return 'Item not found'
