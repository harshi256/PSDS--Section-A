
T = int(input("Enter number of test cases: "))

for _ in range(T):
    S = input("Enter the string: ")

    freq = [0] * 26

    for ch in S:
        freq[ord(ch) - ord('a')] += 1

    ans = 0

    for count in freq:
        ans += count // 2

    print("Maximum palindromic subsequences:", ans)
