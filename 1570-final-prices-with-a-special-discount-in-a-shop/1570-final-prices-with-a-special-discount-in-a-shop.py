class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        final_price = []

        for i in range(len(prices)):
            # final_price.append(prices[i])

            discount_applied = False
            for j in range(i+1, len(prices)):
                if prices[j]<=prices[i]:
                    discount_applied = True
                    final_price.append(prices[i]-prices[j])
                    break
            if not discount_applied:
                final_price.append(prices[i])
        
        return final_price
        