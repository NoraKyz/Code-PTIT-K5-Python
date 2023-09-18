t = int(input())

def solve(s1, s2):
    for i in range(1, len(s1)):
        dist1 = abs(ord(s1[i]) - ord(s1[i-1]))
        dist2 = abs(ord(s2[i]) - ord(s2[i-1]))
        if dist1 != dist2:
            return "NO"
    return "YES"

for _ in range(t):
    s1 = input()
    s2 = s1[::-1]

    print(solve(s1, s2))
