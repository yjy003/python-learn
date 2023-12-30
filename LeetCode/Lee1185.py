
'''
我们可以使用蔡勒公式来计算星期几，蔡勒公式如下：

w=(⌊c4⌋−2c+y+⌊y4⌋+⌊13(m+1)5⌋+d−1) mod 7w = (\left \lfloor \frac{c}{4} \right \rfloor - 2c + y + \left \lfloor \frac{y}{4} \right \rfloor + \left \lfloor \frac{13(m+1)}{5} \right \rfloor + d - 1) \bmod 7
w=(⌊
4
c
​
 ⌋−2c+y+⌊
4
y
​
 ⌋+⌊
5
13(m+1)
​
 ⌋+d−1)mod7
其中：

w: 星期（从 Sunday 开始）
c: 年份前两位
y: 年份后两位
m: 月（m 的取值范围是 3 至 14，即在蔡勒公式中，某年的 1、2 月要看作上一年的 13、14 月来计算，比如 2003 年 1 月 1 日要看作 2002 年的 13 月 1 日来计算）
d: 日
⌊⌋: 向下取整
mod: 取余

作者：ylb
链接：https://leetcode.cn/problems/day-of-the-week/solutions/2584790/python3javacgotypescript-yi-ti-yi-jie-ca-faya/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


class Lee1185:
    def dayOfTheWeek(self, d: int, m: int, y: int) -> str:
        # 1,2月用13,14来计算
        if m < 3:
            m += 12
        # 年
        c = y // 100    # 年前两位
        y = y % 100     # 年后两位
        w = (c//4 - 2*c + y + y//4 + (13 * (m + 1))//5 + d - 1) % 7
        return [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"][w]

lee = Lee1185()
week = lee.dayOfTheWeek(26, 8, 1995)
print(week)
