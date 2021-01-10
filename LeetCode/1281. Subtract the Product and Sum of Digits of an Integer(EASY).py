class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        arr = [int(element) for element in str(n)]
        
        product_digit = 1
        sum_digit = 0
        
        for digit in arr:
            product_digit*=digit
            sum_digit+=digit
        return product_digit-sum_digit
