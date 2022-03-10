# https://practice.geeksforgeeks.org/contest/interview-series-atlassian-4644/problems/
# Input: 4 8 6 5 3
# Output: 4 0 3 4 -1

class Solution:
    def nearestSmallestTower(self,arr):
        for i in range(len(arr)):
            for j in range(len(i+1)):
                if arr[i] <= arr[j]:
                    return -1
                else:
                    return arr[j]

    arr = [4, 8, 6, 5, 3]
    nearestSmallestTower(arr)
    #no idea
