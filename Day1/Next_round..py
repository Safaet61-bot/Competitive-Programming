n, k = map(int, input().split())
scores = list(map(int, input().split()))
cut_off = scores[k-1]

count = 0
for score in scores:
    if score > 0 and score >= cut_off:
        count += 1

print(count)
