# https://leetcode.com/problems/first-bad-version/
def isBadVersion(n):
    return True
# def firstBadVersion(self, n: int) -> int:
#     for i in range(n):
#         if isBadVersion(i) == True:                
#             return i
#     return i+1

# cant be solved here

#other's solution from leetcode
def firstBadVersion(self, n: int) -> int:
    start=1
    end=n
    while start<=end:
        mid=start+(end-start)//2
        if isBadVersion(mid):
            if not isBadVersion(mid-1):
                return mid
            else:
                end=mid-1
        else:
            start=mid+1
    return -1

n=6
print(firstBadVersion(5, n))
#not understood


