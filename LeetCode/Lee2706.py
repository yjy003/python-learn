from typing import List

class Lee2706:
    def buyChoco1(self, prices: List[int], money: int) -> int:
        print("排序前：" + str(prices))
        prices.sort()
        print("排序后：" + str(prices))
        cost = prices[0] + prices[1]
        return money if money < cost else money - cost

    def buyChoco2(self, prices: List[int], money: int) -> int:
        a = b = 10000
        for x in prices:
            if x < a:
                a, b = x, a
            elif x < b:
                b = x
        cost = a + b
        return money if money < cost else money - cost

print("================")
lee = Lee2706()
list = [12,345,6,7,89]
res = lee.buyChoco2(list, 138)
print(res)

print("================")



