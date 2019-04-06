#Given a set of digits (A) in sorted order, find how many numbers of length B are possible whose value is less than number C.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def count(self, A, B, b, i):
        if i >= len(b) or B==0:
            return 1
        c_max = int(b[i])
        rt = 0
        for x in A:
            if i == 0 and x ==0 and B!=1:
                continue
            if x > c_max:
                continue
            if x == c_max:
                if i >= len(b) -1:
                    continue
                rt = rt + self.count(A, B-1, b, i+1)
            else:
                rt = rt + len(A)**(B-1)
        return rt
                
    
    def solve(self, A, B, C):
        c = str(C)
        if len(c) < B:
            return 0
        
        ind = 0
        if len(c) == B:
            return self.count(A, B, c, 0)
        rt = 0
        for x in A:
            if x == 0 and B!=1:
                continue
            if x==0 and x < C:
                rt +=1
            else:
                rt = rt + len(A)**(B-1)
        return rt
            
