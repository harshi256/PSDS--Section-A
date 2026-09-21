# Q1
# N, K = map(int, input("Enter N and K: ").split())

# arr = list(map(int, input("Enter array elements: ").split()))

# current_sum = sum(arr[:K])

# max_sum = current_sum

# for i in range(K, N):
#     current_sum = current_sum + arr[i] - arr[i - K]

#     max_sum = max(max_sum, current_sum)

# print("Maximum Sum:", max_sum)


# Q2: Longest Substring Without Repeating Characters
s = input("Enter string: ")
left = 0
max_length = 0

seen = set()

for right in range(len(s)):

    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    length = right - left + 1

    max_length = max(max_length, length)

print("Longest substring length:", max_length)

# Q3: Shortest Path from 1 to N using at most K edges

N, M, K = map(int, input("Enter N, M and K: ").split())

edges = []

for i in range(M):
    u, v, weight = map(int, input("Enter u, v and weight: ").split())
    edges.append((u, v, weight))

INF = float('inf')

dp = [INF] * (N + 1)

dp[1] = 0

for i in range(K):

    new_dp = dp.copy()

    for u, v, weight in edges:

        if dp[u] != INF:
            new_dp[v] = min(new_dp[v], dp[u] + weight)

        if dp[v] != INF:
            new_dp[u] = min(new_dp[u], dp[v] + weight)

    dp = new_dp

if dp[N] == INF:
    print(-1)
else:
    print("Minimum Path Weight:", dp[N])