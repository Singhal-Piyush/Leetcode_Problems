class Solution:
    def isHappy(self, n: int) -> bool:

        # to store the already seen sum of squares
        hash_map = {}

        while n!=1:
            digit_n = []
            sum_of_square = 0
            while n/10 !=0:
                digit_n.append(n%10)
                n =  n//10

            for i in digit_n:
                sum_of_square += i**2
            
            # assign back sum_of_square to n
            n = sum_of_square

            # For False scenario
            if n in hash_map:
                return False
            else:
                hash_map[n] =1
        
        return True
            
                




        