class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        add = 0
        prod = 1
        while temp>0:
            r = temp%10
            temp//=10
            add+=r
            prod*=r
        return prod-add