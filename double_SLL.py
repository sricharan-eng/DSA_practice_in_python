# print("this is Double Linked list")

class Node:
    def __init__(self,data=None)->None:
        self.prev = None
        self.data = data
        self.next = None

    


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None


    def insert(self,data):
        temp = Node(data)
        if self.head is None and self.tail is None:
            self.head = self.tail = temp
         
        else :
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp
            self.tail.next = None

            

    def delete(self,ddata =None):
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
            print("only head is present")
        if self.tail.next is None and ddata is None:
            # print("this is self.tail.prev",self.tail.prev.data,self.tail.prev,self.tail)     
            self.tail = self.tail.prev
            self.tail.next = None
            return ddata
        if ddata is not None:

            temp1 = self.head
            if temp1.data == ddata:
                print("This is head data")
                self.head = self.tail = temp1.next
                self.head.prev = self.tail.prev = None
            else:
               temp1 = self.head
               while temp1.next is not None:
                temp1 = temp1.next
                if temp1.data == ddata:
                    print("this is prev value",temp1.prev.data,temp1.data,temp1.next.data)
                    temp1.prev.next = temp1.next
                    temp1.next.prev = temp1.prev
                   
                    temp1 = None
                    break
            return ddata
        return data
      
        
    
    def display_DLL(self):
        current = self.head
      
        if current is None:
            print("this list is empty")
        else:
           
            while current != None:
                print(current.data ,end=" ")
                print("this is data",
                      current.prev,
                      current.data,
                      current.next,
                     )
                current = current.next
            
            



d=DLL()

for i in range(0,100,5):
    d.insert(i)
d.display_DLL()
print("\n")
print("deleting last value",d.delete())
d.display_DLL()
print("\n")
print("deleting 20 value ", d.delete(20))
d.display_DLL()
print("\n")
print("deleting head value",d.delete(0))
d.display_DLL()
# print("deleting 50 value",d.delete(50))
# d.display_DLL()
# print("deleting 25 value",d.delete(25))
# d.display_DLL()
# print("deleting 85 value",d.delete(85))
# d.display_DLL()