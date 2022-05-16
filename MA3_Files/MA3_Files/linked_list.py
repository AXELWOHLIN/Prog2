""" linked_list.py

Student: Axel Wohlin
Mail: axelwohlin@gmail.com
Reviewed by: Gustav Fredrikson
Date reviewed: 11/5
"""

class LinkedList:
    
    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ      
        
            
    def __init__(self):
        self.first = None

    
    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ
            
    def __in__(self, x):           # Discussed in the section on operator overloading 
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False 
        return False
        
    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')         

    def length(self):
        i = 0
        f = self.first
        while f.succ:
            i+=1
            f = f.succ   
        return i
    
    # To be implemented
    

    def length(self):
        if not self.first:
            return 0
        i = 1
        f = self.first
        while f.succ:
            i+=1
            f = f.succ   
        return i
  

    def mean(self):               # Optional
        summa = 0
        i = 1
        f = self.first
        while f.succ:
            summa += f.data
            i += 1
            f = f.succ
        summa += f.data
        return summa/i
    
    
    def remove_last(self):        # Optional
        if not self.first:
            return None
        elif not self.first.succ:
            return self.first.data
        else:
            f1 = self.first
            f2 = f1.succ
            while f2.succ:
                f1 = f2
                f2 = f2.succ
            f1.succ = None
            return f2.data
    

    def remove(self, x):          # Compulsory
        if not self.first:
            return False
        else:
            f1 = self.first
            f2 = f1.succ
            if f1.data == x:
                self.first = f2
                return True
            if not f2:
                return False
            while f2.data != x and f2.succ:
                f1 = f2
                f2 = f2.succ
            if f2.data == x:
                f1.succ = f2.succ
                return True
            else:
                return False

    
    def count(self, x):           # Optional
        i = 0
        for val in self:
            if val == x:
                i += 1
        return i
        
    def to_list(self):            # Compulsory
        if not self.first:
            return []
        else:
            return self._to_list(self.first)

    def _to_list(self,f):
        if f.succ == None:
            return [f.data]
        else:
            return [f.data] + self._to_list(f.succ)

    
    def remove_all(self, x):      # Compulsory
        if not self.first:
            return False
        else:
            self = self._remove_all(self.first,x)
           
    def _remove_all(self,f,x): #TODO

        """def remove(self, x):          # Compulsory
            if not self.first:
                return False
            else:
                f1 = self.first
                f2 = f1.succ
                if f1.data == x:
                    self.first = f2
                while f2.data != x and f2.succ:
                    f1 = f2
                    f2 = f2.succ
                if f2.data == x:
                    f1.succ = f2.succ
                    return True
                else:
                    return False 
                    """
        if not f: 
            return self
        elif self.first.data == x:
            self.first = f.succ
            self._remove_all(f.succ,x)
        elif f.data == x: 
            self.remove(x)
            self._remove_all(f.succ,x)
        else:
            self._remove_all(f.succ,x)
            

    def __str__(self):            # Compulsary
        if not self.first:
            return "()"
        ans = '('
        for x in self:
            ans += (str(x) + ', ')
        ans = ans[:len(ans)-2] + ')'
        return ans
    
    def merge(self, lst):         # Compulsory 
        """
        Since list concatenation has O(n**2) and python's built in sort function
        has O(n*log(n)), the O(n**2) term dominates and my merge function will be O(n**2).
        """
        """
        def insert(self, x):
            if self.first is None or x <= self.first.data:
                self.first = self.Node(x, self.first)
            else:
                f = self.first
                while f.succ and x > f.succ.data:
                    f = f.succ
                f.succ = self.Node(x, f.succ)
        """
        for val in lst:
            self.insert(val)
        
    
    
    def __getitem__(self, ind):   # Compulsory
        f = self.first
        i = 0
        while i < ind:
            f = f.succ
            i += 1
        return f.data



class Person:                     # Compulsory to complete
    def __init__(self,name, pnr):
        self.name = name
        self.pnr = pnr
        
    def __str__(self):
        return f"{self.name}:{self.pnr}"

    def __lt__(self,x):
        if self.pnr < x:
            return True
        else:
            return False

    def __le__(self,x):
        if self.pnr <= x:
            return True
        else:
            return False

    def __gt__(self,x):
        return self.pnr > x

    def __ge__(self,x):
        if self.pnr >= x:
            return True
        else:
            return False

    def __eq__(self,x):
        if self.pnr == x:
            return True
        else:
            return False
    def __ne__(self,x):
        if self.pnr != x:
            return True
        else:
            return False
    

def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()
    
    # Test code:
    'print( lst.length() )'
    'print( lst.mean() )'
    """
    print( lst.remove_last() )
    print( lst.length() )
    """
    
    i = 0
    while i < 4:
        print( lst.remove(1) ) 
        lst.print()
        i += 1
    print(lst.remove(10))

    """
    print( lst.to_list() )
    """
    """
    lst.remove_all(1) #TODO FIX
    lst.print()
    """
    """
    lst.remove_all(3) #TODO FIX
    lst.print()
    """
    """
    lst.remove_all(2)
    lst.print()
    """
    """
    lst.remove_all(9)
    lst.print()
    """
    '''
    print(lst.__str__())
    a = lst.merge([-1,0,12])
    print(a)
    '''
    """
    lst.print()
    for i in range(10):
        print( lst.__getitem__(i) )
        print(lst[i])
    """
    
 
if __name__ == '__main__':
    main()
    


    

