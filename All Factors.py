class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, n):
        result = set()
        for i in range(1, int(n ** 0.5) + 1):
            div, mod = divmod(n, i)
            if mod == 0:
                result |= {i, div}
        return sorted(result)
