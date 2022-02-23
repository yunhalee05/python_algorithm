from sys import stdin

str1 = stdin.readline().strip().upper()
str2 = stdin.readline().strip().upper()

def lcs (str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return (dp[-1][-1])

print(lcs(str1, str2))


# import sys

# A = sys.stdin.readline().strip().upper()
# B = sys.stdin.readline().strip().upper()

# lcs = [[0] * (len(A)+1) for _ in range(len(B)+1)]

# for i in range(1,len(B)+1) :
#   for j in range(1,len(A)+1) :
#     if B[i-1] == A[j-1] :
#       lcs[i][j] = lcs[i-1][j-1] + 1
#     else :
#       lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

# print(lcs[-1][-1])


            




