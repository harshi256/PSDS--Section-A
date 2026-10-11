
def digit_sum(n):
    n = abs(n)

    s = 0

    while n > 0:
        s = s + n % 10
        n //= 10

    return s


def solve(N, nums):

    count = {}
    ans = 0

    for x in nums:

        s = digit_sum(x)

        if s in count:
            ans += count[s]

        count[s] = count.get(s, 0) + 1

    return ans


N = int(input())
nums = list(map(int, input().split()))

print(solve(N, nums))