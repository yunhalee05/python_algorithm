n = int(input())
card = list(map(int, input().split()))
card.sort(reverse=True)

answer = 0
max_gold = card[0]
for i in range(1, n):
    answer += (max_gold+card[i])
    max_gold = max(max_gold, card[i])

print(answer)

