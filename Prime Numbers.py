class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        ans=[2]
        for num in range(3,A,2):
            if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
                ans.append(num)
        return ans
