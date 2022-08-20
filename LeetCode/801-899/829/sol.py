class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        sol_num = 0
        for i in range(n):
            real_i = i + 1
            mean_num = n/real_i
            mean_min = mean_num - 0.5*(real_i-1)
            if mean_min < 1:
                break
            if mean_num % 0.5 != 0 or mean_min % 1 != 0:
                continue
            sol_num += 1
        return sol_num

'''
通过强行压制的做法
- 因为当解中有2个以上的数字，表示最起码，start number 应该是 n 的 1/2 + 1，意味着，所有结果的平均数 * list 数字个数就是 n
- 
- 从上面出发，就可以做优化，增加限制条件。
- - 1个数的解是本身
- - 2个数的解是平均数 * 2，即平均数-0.5 和 平均数 + 0.5
- - 3个数的解是平均数 * 3，即平均数、平均数-1、平均数+1
- - m个数的解是平均数 * m，即平均数-0.5*(m-1)～平均数+0.5*(m-1)
- - 由此可以写出函数
- 当最小值小于1时，即平均数-0.5*(m-1)<1时，不用再计算
- 当平均数不为0.5的倍数时，不成立
- 当最小值不为整数时，不成立
'''
if __name__ == '__main__':
    test_1 = Solution()
    print(test_1.consecutiveNumbersSum(333764327))
