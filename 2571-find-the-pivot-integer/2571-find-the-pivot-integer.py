class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n*(n+1)//2

        left_sum = 0
        right_sum = total_sum

        for i in range(1,n+1):
            left_sum = left_sum + i
            right_sum = right_sum - i +1

            if left_sum == right_sum:
                return i
                 
        return -1