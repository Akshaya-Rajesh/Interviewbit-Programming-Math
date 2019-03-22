class Solution:
    def findDigitsInBinary(self, A):
        b=''
        f=0
        if(A==0):
            return 0
        for i in range(A, -1, -1):  
            k = A>> i; 
            if (k & 1): 
                f=1
                b+='1'
            else:
                if(f==1):
                    b+='0'
        return b
