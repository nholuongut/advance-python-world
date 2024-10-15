from typing import Any , Dict

class MyList:
    
    def __init__(self) -> None:
        self.length = 0
        self.data : Dict[int, Any] = {}

    def push(self, data:Any):
        # push data
        self.data[self.length] = data
        self.length +=1

    def insert(self, index:int , data:Any):
        # shift data to right
        self.rshift(index=index)
        # repalce data
        self.data[index] = data 
        # update the lenght
        self.length +=1
        
    def rshift(self, index:int):
        tmp_array =  self.data.copy()
        for i in range(index, self.length):
            self.data[i+1] = tmp_array[i]     
        del tmp_array

    def reverse(self):
        # in memeory item change
        L_p , H_p = 0 , self.length-1

        while ( L_p < H_p ):
            L_val  = self.data[L_p]
            self.data[L_p] = self.data[H_p]
            self.data[H_p] = L_val

            # iterate the L_P and H_P
            L_p += 1
            H_p = self.length-1 - L_p
        



if __name__ == '__main__':
    mylist =  MyList()
    mylist.push(data="Hi")
    mylist.push(data="My")
    mylist.push(data="Name")
    print(mylist.data)
    mylist.insert(index=1,data="Himasha")
    mylist.push(data="Thamali")
    mylist.push(data="Uni")
    mylist.push(data="Kalada")
    mylist.push(data="manika")
    print(mylist.data)
    mylist.reverse()
    print(mylist.data)