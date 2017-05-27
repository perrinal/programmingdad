from random import randint

class SockPair: 
    def __init__(self, sock1, sock2):
        self.sock1 = sock1
        self.sock2 = sock2

    def __str__(self):
        return str(self.sock1)


class Sock:
    def __init__(self, color, pattern,size):
        self.color = color
        self.size = size
        self.pattern = pattern

    def equals(self, othersock):
        if self.color == othersock.color and\
           self.size == othersock.size and\
           self.pattern == othersock.pattern:
            return True
        else:
            return False
        
    def __str__(self):
        return self.color+" "+self.pattern+" "+self.size

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
               self.PairBucket.append(SockPair(Sock1, Sock2))
               self.Stack.remove(Sock2)
               return True
        return False

    def __str__(self):
        
        return "Stack\n" + str([str(Sock) for Sock in self.Stack])+\
               "\nPairs\n"+str([str(Pair) for Pair in self.PairBucket])+\
               "\nOrphans\n"+str([str(Sock) for Sock in self.Orphans])+"\n"


# Main
SockStk = SockStack(20)
print(SockStk)
SockStk.pairTheStack()
print(SockStk)                             
                             
            
#In the somewhat ideal world of computer my stack of unpaired socks would take 30 min to write the program and then a few milisecond to execute.
#Unfortunately in real life; I am leaft with a mountain of socks that need to be manually paired and while my brain is able to make sense of scrunched sock pattern and pair then it still take me 30 min everytime during which I would rather write silly pythion programms. 
