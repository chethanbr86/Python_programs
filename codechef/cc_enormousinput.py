# https://www.codechef.com/LP0TO101/problems/INTEST

#codechef answer
(n,k) = map(int, input().split())  #just n,k works too

ans = 0

for i in range(n):
	x = int(input())
	if x % k == 0:
		ans += 1

print(ans)	