"""*****************************************************************************
Name:    Chanchatri Chaichanathong
course:  CMPT 200 X03L
purpose: Review Class
ID:      3056450
a*****************************************************************************"""

'''
this is Package class that is used by Container class to to create a package obj that containe
name, destination, weight, and id. the class have a function that set id to the package when being added.

the class contain a linked class - _Node in order to used node fuction of python'''
class Package:
    # Purpose: this method initialize package obj
    # Parameters:  name, dest, weight, pId
    # Return: none      
    def __init__(self, name, dest, weight, pId=None):
        self._dest = dest
        self._weight = weight
        self._name = name
        self._id = pId
        
    # Purpose: this method show package
    # Parameters: none
    # Return: none  
    def __repr__(self): 
        return str([self._name, self._dest,self._weight, self._id])
    
    # Purpose: this method show weight of the package
    # Parameters: none
    # Return: none      
    def weight(self):
        return int(self._weight)
    # Purpose: this method set id
    # Parameters:  pId
    # Return: none      
    def set_id(self, pId):
        self._id = pId

'''
this is Container class that is used by Shipyard class to to create a container node that containe
package obj. the class have a functions that set id, find total weight of the container,
search package, remove package, add package.

the class contain a linked class - _Node in order to used node fuction of python'''   
class Container:
    class _Node:    
        def __init__(self, element, next):
            self._element = element
            self._next = next
            
    # Purpose: this method initialize container
    # Parameters:  name, dest, weight, pId
    # Return: none      
    def __init__(self, name=None, dest=None, weight=None, pId=None):
        self._dest = dest
        self._weight = weight
        self._name = name
        self._id = pId
        self._head = None
        self._size = 0 
        self.insert(self._name, self._dest, self._weight)
        
    # Purpose: this method check if the package is empty
    # Parameters: none
    # Return: none          
    def is_empty(self) :
        return self._size == 0 
    
    # Purpose: this method show container's contents
    # Parameters: none
    # Return: none      
    def __repr__(self):
        p = self._head 
        s = ''
        while p != None:
            #element = package = [dest, weight]
            s += '\t\t'+ str(p._element) + '\n'
            p = p._next
        return s   
    
    # Purpose: this method add package to containers
    # Parameters: name, dest, weight
    # Return: none      
    def insert(self, name, dest, weight):
        #attemp to add at first if the weight is lighter
        #self.head.element.weight = package's weight
        if self.is_empty() or weight < self._head._element._weight:
            self._head = self._Node(Package(name, dest, weight, self._id), self._head)
            self._size +=1
            #[new / lighter] -> [old node] -> [next old node]
            return
        temp = self._head
        #if weight is not lighter than search where to put the package
        while temp._next != None and weight > temp._next._element._weight:
            count+=1
            temp = temp._next              
        self._size += 1
        temp._next = self._Node(Package(name, dest, weight, self._id), temp._next)
        return
    
    # Purpose: this method find total weight of the containers
    # Parameters: none
    # Return: none      
    def total_weight(self):
        t = self._head
        total = 0
        while t !=None:
            total += int(t._element._weight)
            t = t._next
        return total
    
    # Purpose: this method set id of the package
    # Parameters: pId
    # Return: none      
    def set_id(self,pId):
        t = self._head
        listDest = []
        newId = pId.split()
        newId.append(0)
        #set destination for counting as part of the id
        while t!=None:
            if t._element._dest not in listDest:
                listDest.append(t._element._dest)
            t = t._next  
        #set id: count will reflected the package's position in the contaienr
        for i in listDest:
            count = 1
            p = self._head
            while p!=None:
                newId[-1] = str(count)
                pId = ''.join(newId)
                if p._element._dest == i: 
                    p._element.set_id(pId)
                    self._id = pId
                    count+=1
                p = p._next
                
    # Purpose: this method remove package
    # Parameters: pId
    # Return: none                  
    def remove(self, pId):
        if self.is_empty():
            return print('Empty')
        #check if the id is the same as the first package
        if self._head._element._id == pId:
            if self._head._next != None:
                self._head = self._head._next
            else: 
                self._head= None
            self._size -= 1
            return
        #search until find the package otherwise nothing happen
        t = self._head
        while t._next !=None and pId != t._next._element._id :
                t = t._next
        if t._element._id == pId:
            if t._next != None:
                t._next = t._next._next
            else:
                t._next = None
            self._size -= 1
        return
    
    # Purpose: this method search for package
    # Parameters: pId
    # Return: none      
    def search(self, pId):
        if self.is_empty():
            return
        #search the first package
        if self._head._element._id == pId:
            print(self._head._element)
            return
        #otherwise search until find
        t = self._head
        while t._next !=None and pId != t._next._element._id :
                t = t._next
        if t._element._id == pId:
            print(self._head._element)
            return        
        else: print('\nno package associated with this ID: '+ pId)
'''
this is Shipyard class that is used by main() to to create a collection containers.
the class have a functions that set id, search package, remove package, insert package to containers,
prints various aspect of the class's info, ship the containers.

the class contain a linked class - _Node in order to used node fuction of python''' 
class Shipyard:
    class _Node:    
        def __init__(self, element, next):
            self._element = element
            self._next = next 
            
    # Purpose: this method initialize shipyard
    # Parameters: name, dest, weight
    # Return: none              
    def __init__(self, name=None, dest=None, weight=None):
        self._dest = dest
        self._weight = weight
        self._name = name
        self._head = None
        self._size = 0 
        
    # Purpose: this method check if wmpty
    # Parameters: None
    # Return: bool         
    def is_empty(self) :
        return self._size == 0 
    
    # Purpose: this method print contents
    # Parameters: none 
    # Return: none      
    def __repr__(self):
        if self.is_empty():
            return '\nEmpty Shipyard'
        t = self._head
        listDest = []
        #create a destination list
        while t!=None:
            if t._element._dest not in listDest:
                listDest.append(t._element._dest)
            t = t._next
        s = ''
        #show content as 
        #destination 
        #           -->
        #              container
        #                       -->
        #                          packages
        for i in listDest:
            count = 0
            p = self._head 
            s += str(i) + '-->'
            while p != None:
                if p._element._dest == i:
                    count += 1
                    s+= '\tContainer'+ str(count) +'-->\n'
                    s += str(p._element) + '\n'
                p = p._next
        return s 
    
    # Purpose: this method show everything work the same as __repr__
    # Parameters: none
    # Return: string     
    def printAll(self):
        if self.is_empty():
            return '\nEmpty Shipyard'
        t = self._head
        listDest = []
        #create a destination list
        while t!=None:
            if t._element._dest not in listDest:
                listDest.append(t._element._dest)
            t = t._next
        s = ''
        #show content as 
        #destination 
        #           -->
        #              container
        #                       -->
        #         
        for i in listDest:
            count = 0
            p = self._head 
            s += str(i) + ':\n'
            while p != None:
                if p._element._dest == i:
                    count += 1
                #element = container = [[dest, weight] -> [dest, weight]]
                    s+= '\tContainer'+ str(count) +':\n'
                    s += str(p._element) + '\n'
                p = p._next
        return s  
    
    # Purpose: this method show all contents in the container base on destination
    # Parameters: dest
    # Return: string   
    def printDest(self, dest):
        if self.is_empty():
            return '\nEmpty Shipyard'
        s = ''
        count = 0
        p = self._head 
        s += str(dest) + ':\n'
        while p != None:
            if p._element._dest == dest:
                count += 1
            #element = container = [[dest, weight] -> [dest, weight]]
                s+= '\tContainer'+ str(count) +':\n'
                s += str(p._element) + '\n'
            p = p._next
        return s  
    
    # Purpose: this method print containers
    # Parameters: none
    # Return: string    
    def printContainers(self):
        if self.is_empty():
            return '\nEmpty Shipyard'        
        s = ''
        count = 0
        p = self._head 
        
        while p != None:
            count += 1
            #element = container = [[dest, weight] -> [dest, weight]]
            s+= '\tContainer'+ str(count) +':\n'
            s += str(p._element) + '\n'
            p = p._next
        return s  
    
    # Purpose: this method add package
    # Parameters: name, dest, weight
    # Return: none      
    def insert(self, name, dest, weight):
        #check first element
        if self.is_empty() or dest < self._head._element._dest:
            self._head = self._Node(Container(name, dest, weight), self._head)
            self._size +=1
            #[low dest ] -> [high node] -> [next old node]
            return
        #check the rest
        temp = self._head
        while (temp._next != None and dest >= temp._element._dest):
            #if containers have the same destination, attemp to add to the container
            #if the weight doesn't exceed 2000 otherwise create new container
            if dest == temp._element._dest:
                if temp._element.total_weight() + weight <= 2000:
                    temp._element.insert(name, dest, weight)
                    return
                if dest != temp._next._element._dest:
                    break
                          
            temp = temp._next
            #create new containers 
            if temp._next == None and dest == temp._element._dest:
                if temp._element.total_weight() + weight <= 2000:
                    temp._element.insert(name, dest, weight)
                    return  
        self._size += 1
        temp._next = self._Node(Container(name, dest, weight), temp._next)
        return 
    
    # Purpose: this method set id
    # Parameters: none
    # Return: none      
    def set_id(self):
        t = self._head
        listDest = []
        #find list on destination - used as part of id
        while t!=None:
            if t._element._dest not in listDest:
                listDest.append(t._element._dest)
            t = t._next
        #set id base on 2 initial of destination, position of the container, 
        #position in the container - ca11 would be dest = ca, container position = 1, package position = 1
        for i in listDest:
            count = 1
            p = self._head
            while p!=None:
                pId = p._element._dest[0]+p._element._dest[1]+str(count)
                if p._element._dest == i: 
                    p._element.set_id(pId)
                    count+=1
                p = p._next
                
    # Purpose: this method remove package
    # Parameters: pId
    # Return: none          
    def remove(self, pId):
        if self.is_empty():
            return print("\ndoesn't exist")
        #check the first item
        if self._head._element._id[:-1] == pId[:-1]:
            #remove
            self._head._element.remove(pId)
            if self._head._next != None:
                self._head = self._head._next
            else:
                self._head = None
            self._size -= 1
            return
        #check the rest
        t = self._head
        while t._next !=None and t._next._element._id[:-1] != pId[:-1]:
                t = t._next
        t._next._element.remove(pId)
        if t._next._element._size == 0 and t._next != None:
            t._next = t._next._next

            return
        self._size -= 1
        return

    # Purpose: this method search for package
    # Parameters: pId
    # Return: none      
    def search(self, pId):
        if self.is_empty():
            return print("\ndoesn't exist")
        if self._head._element._id[:-1] == pId[:-1]:
            self._head._element.search(pId)
            return 
        t = self._head
        while t._next !=None and t._next._element._id[:-1] != pId[:-1]:
                t = t._next
        t._next._element.search(pId)
        return
    
    # Purpose: this method ship contents base on destination
    # Parameters: dest
    # Return: none      
    def ship(self, dest):
        if self.is_empty():
            return print('\nshipyard is empty')
        while self._head._next !=None and self._head._element._dest == dest:
            self._head = self._head._next
        self._size -= 1      
        return print('All containers going to "' +dest+ '" have departed')
    
# Purpose: this method main
# Parameters: none
# Return: none      
def main():
    s = Shipyard()
    print('welcome to Shipping Container Management System')
    while True:
        print('\na) Add new package (owner, destination, weight(kg))'+
              '\nb) Show all Containers'+
              '\nc) Show manifest of a destination'+
              "\nd) Show Container's Content"+
              '\ne) Remove by id'+
              '\nf) search by id' +
              '\ng) ship'+
              '\nh) exit') 
        userInput = input("\nPlease choose one of the option: ")
        if userInput.lower() == 'a':
            while True:
                infoName = input('Please enter your name: ')
                infoDest = input('Please enter your destination: ')
                infoWeight = input("Please enter your package's weight: ")
                if infoName != '' and infoDest != '' and infoWeight != '':                    
                    while not infoWeight.isdigit():
                        infoWeight = input('Weight must be numbers, Please enter weight: ')
                    break
                
            s.insert(infoName, infoDest, infoWeight)
            s.set_id()
        if userInput.lower() == 'b':
            print(s)
        if userInput.lower() == 'c':
            while True:
                infoInput = input('Please enter your infomation (destination): ')
                if infoInput == '':
                    infoInput = input('Invalid entry, Please enter your infomation (destination): ')
                else:
                    break
            print(s.printDest(infoInput))
        if userInput.lower() == 'd':
            print(s.printContainers())
        if userInput.lower() == 'e':
            while True:
                infoInput = input('Please enter your infomation (id): ')
                if infoInput == '':
                    infoInput = input('Invalid entry, Please enter your infomation (id): ')
                else:
                    break            
            s.remove(infoInput)
        if userInput.lower() == 'f':
            while True:
                infoInput = input('Please enter your infomation (id): ')
                if infoInput == '':
                    infoInput = input('Invalid entry, Please enter your infomation (id): ')
                else:
                    break  
            s.search(infoInput)
        if userInput.lower() == 'g':
            while True:
                infoInput = input('Please enter your infomation (dest): ')
                if infoInput == '':
                    infoInput = input('Invalid entry, Please enter your infomation (dest): ')
                else:
                    break              
            s.ship(infoInput)
        if userInput.lower() == 'h':
            break                          
main()