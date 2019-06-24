# 15. 3Sum
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:
# The solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l_ans = []
        d_pos = dict()
        d_neg = dict()
        for num in nums:
            if num >= 0:
                if num in d_pos:
                    d_pos[num] += 1
                else:
                    d_pos[num] = 1
            else:
                if num in d_neg:
                    d_neg[num] += 1
                else:
                    d_neg[num] = 1
        for x in d_pos:
            for y in d_neg:
                t = x + y
                if  -1*t in d_pos and x < -1*t:
                    l_ans.append([y, x, -1*t])
                elif -1*(x + y) in d_neg and y < -1*t:
                    l_ans.append([y, x, -1*t])
                elif -1*t == x and d_pos[x] > 1:
                    l_ans.append([y, x, x])
                elif -1*t == y and d_neg[y] > 1:
                    l_ans.append([y, y, x])
        if 0 in d_pos and d_pos.get(0) >= 3:
            l_ans.append([0,0,0])
        return l_an