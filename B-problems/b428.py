N, K = map(int, input().split())
S = input()

counts = {}

for i in range(N-K+1):
    substrings = S[i : i+K]
    counts[substrings] = counts.get(substrings, 0) + 1

max_count = max(counts.values())

result_substring = []

for substrings, count in counts.items():
    if count == max_count:
        result_substring.append(substrings)

result_substring.sort()

print(max_count)
print(" ".join(result_substring))