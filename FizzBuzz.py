class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        ans=[]
        for i in range(1,A+1):
            add=""
            if(i%3==0):
                add+="Fizz"
            if(i%5==0):
                add+="Buzz"
            if(add==""):
                ans.append(i)
            else:
                ans.append(add)
        return(ans)
