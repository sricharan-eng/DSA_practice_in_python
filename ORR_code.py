print("this is ORR code")
class ORR_list:
    def __init__(self,extno,tolname,kms):
        self.exit_no = extno
        self.toll_name = tolname
        self.prev = None
        self.next = None
        self.kms = kms


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,extno,tolname,kilo_metre):     
            temp = ORR_list(extno,tolname,kilo_metre)
            if self.head is None and self.tail is None:
                self.head = self.tail = temp           
            else :
                self.tail.next = temp
                temp.prev = self.tail
                self.tail = temp
                self.tail.next = None

    def display_DLL(self):
        current = self.head
      
        if current is None:
            return
        else:     
            while current != None:
                current = current.next
            
class Vehicle(DLL):
    def __init__(self,veh,en_point,ex_point,ORR_head):
        self.Vehicle_type = veh
        self.entry_point = en_point
        self.exit_point = ex_point
        self.cost = None
        self.distance = None
        self.this_head = ORR_head
        self.ent_node = None
        self.ext_node = None

    def cost_and_distance(self):
        self.distance = self.exit_point - self.entry_point

        
        ent_toll_name= 0
        ext_toll_name =0
        tp = self.this_head
        count = 0
        lt= 0
        self.ent_node = None
        self.ext_node = None
        if tp is None:
            return 
        else:     
            while tp != None:
                count += 1
                lt += tp.kms
                if self.entry_point == count:
                    ent_toll_name  = tp.toll_name
                    self.ent_node = tp
                if self.exit_point == count:
                    ext_toll_name = tp.toll_name
                    self.ext_node = tp
                    break
                tp = tp.next

        tolls_count_with_kms = 0
        while self.ent_node != None:
            self.ent_node = self.ent_node.next
            tolls_count_with_kms += self.ent_node.kms
            if self.ent_node == self.ext_node:
                break


        if self.Vehicle_type == 4:
            self.cost = tolls_count_with_kms * 0.35
        elif self.Vehicle_type  == 6:
            self.cost = tolls_count_with_kms * 0.45
        elif self.Vehicle_type == 8:
            self.cost =  tolls_count_with_kms * 0.50
        else:
            print("nothing")

        value ={
            "distance":tolls_count_with_kms,
            "cost":self.cost,
            "toll name exit":ext_toll_name,
            "toll name entered": ent_toll_name
            }
        return value

    
d =DLL()
file1 = open('orr_names.txt', 'r')
Lines = file1.readlines()

count = 0

import random
for line in Lines:
    count += 1
    kms  = random.randint(5, 20)

    d.insert(count,line.strip(),kms)
    
m = Vehicle(4,1,4,d.head)
this_is_val = m.cost_and_distance()

print("........................")
print("Vehicle type ::", m.Vehicle_type)
print("Total cost ::",round(this_is_val["cost"],2))
print("Distance covered ::",this_is_val["distance"])
print("Vehicle Entry toll plaza name and toll_exit_no ::",this_is_val["toll name entered"],m.entry_point)
print("Vehicle exit toll plaza name and toll_exit_no ::",this_is_val["toll name exit"],m.exit_point)


n = Vehicle(8,2,7,d.head)

this_is_val_n = n.cost_and_distance()


print("........................")
print("Vehicle type ::", n.Vehicle_type)
print("Total cost ::",this_is_val_n["cost"])
print("Distance covered ::",this_is_val_n["distance"])
print("Vehicle Entry toll plaza name and toll_exit_no ::",this_is_val_n["toll name entered"],n.entry_point)
print("Vehicle exit toll plaza name and toll_exit_no ::",this_is_val_n["toll name exit"],n.exit_point)
