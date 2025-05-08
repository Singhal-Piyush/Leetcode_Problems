class Solution:
    def pivotInteger(self, n: int) -> int:
        left_sum = 0 
        right_sum = n*(n+1)/2

        for i in range(n):
            left_sum +=i+1
            right_sum -=i
            if left_sum == right_sum:
                return i+1
        return -1