from random import randint

class Sock:
    color = None
    size = None
    pattern = None
    pairSock = None
    
    def __init__(self, color, pattern,size, pairSock = None):
        self.color = color
        self.size = size
        self.pattern = pattern
        self.setPairSock(pairSock) 

    def setPairSock(self, otherSock):
        if (otherSock is not None):
            if (type(otherSock) is not Sock):
                raise TypeError ("You cannot pair a Sock with a " + str(type(otherSock)))  
            if (self.equals(otherSock)):
                self.pairSock = otherSock
            else:
                raise ValueError ("Socks are not the same") 

    def equals(self, othersock):
        if self.color == othersock.color and\
           self.size == othersock.size and\
           self.pattern == othersock.pattern:
            return True
        else:
            return False
        
    def __str__(self):
        return str(id(self)) +\
               " "+ self.color+\
               " "+self.pattern+\
               " "+self.size+ " " \
               +str(id(self.pairSock))

class SockStack:
    Colors = ["Blue", "Red","Black"]
    Patterns = ["None", "Diamonds", "Stripes"]
    Sizes = ["Small", "Medium", "Large"]
    Stack = []
    PairBucket = []
    Orphans = []
    
    def __init__(self, size):
       # Generate socks, some will not be paired... like in real life
       for i in range(0,size):
           self.Stack.append(Sock(self.Colors[randint(0,len(self.Colors)-1)],\
                                  self.Patterns[randint(0,len(self.Patterns)-1)],\
                                  self.Sizes[randint(0,len(self.Sizes)-1)]))
           
    def pairTheStack(self):
        while len(self.Stack) > 0:
            Sock1 = self.Stack.pop()
            if (not self.pairThisSock(Sock1)):
                self.Orphans.append(Sock1)
                          
    def pairThisSock(self, Sock1):
        for Sock2 in self.Stack:
            if Sock1.equals(Sock2):
               Sock1.setPairSock(Sock2)
               Sock2.setPairSock(Sock1)
               self.PairBucket.append(Sock1)
               self.PairBucket.append(Sock2)
               self.Stack.remove(Sock2)
               return True
        return False

    def __str__(self):
        
        return "Stack\n" + str([str(Sock) for Sock in self.Stack])+\
               "\nPairs\n"+str([str(Sock) for Sock in self.PairBucket])+\
               "\nOrphans\n"+str([str(Sock) for Sock in self.Orphans])+"\n"


# Main
# Normal
Sock1 = Sock("Blue","Stripes","Large")
Sock2 = Sock("Blue","Stripes","Large", Sock1)
Sock1.setPairSock(Sock2)                
print(Sock1);
print(Sock2);

#Execption on type
try:
    Sock1 = Sock("Blue","Stripes","Large", list())
except TypeError as err:
    print(err)

#Exception on wrong pair
try:
    Sock3 = Sock("Blue","Stripes","Small",Sock1 )
except ValueError as err:
    print(err)

SockStk = SockStack(20)
print(SockStk)
SockStk.pairTheStack()
print(SockStk)                             
                             
            
