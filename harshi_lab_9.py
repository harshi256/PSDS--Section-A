# ques1
def digit_sum(num):
    total = 0

    while num > 0:
        total += num % 10
        num //= 10

    return total


def solve():
    N = int(input("Enter:"))
    nums = list(map(int, input().split()))

    count = {}

    for num in nums:
        s = digit_sum(num)

        if s in count:
            count[s] += 1
        else:
            count[s] = 1

    ans = 0

    for freq in count.values():
        ans += freq * (freq - 1) // 2

    print(ans)


solve()