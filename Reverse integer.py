class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, num):
        neg_flag=False
        if(num<0):
            neg_flag=True
            num=-num
        prev_rev_num=0
        rev_num=0
        while(num!=0):
            current_dig=num%10
            rev_num=(rev_num*10)+current_dig
            # checking if the reverse overflowed or not.  
            # The values of (rev_num - current_dig)/10 and  
            # prev_rev_num must be same if there was no problem
            if (rev_num >= 2147483647 or rev_num <= -2147483648):
                #Result does not fit in a 32 bit signed integer !!
                return 0
            if ((rev_num - current_dig) // 10 != prev_rev_num): 
                #Overflow!!
                return 0
            prev_rev_num=rev_num
            num=num//10
            
        if(neg_flag==True):
            return -rev_num
        else:
            return rev_num
