class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums= sorted(nums)
        freq = [[] for i in range(len(nums) + 1)]
        i=0
        for num in nums:
            if (freq[i] and num == freq[i][-1]):
                continue
            elif (freq[i] and (num - 1) == freq[i][-1]):
                freq[i].append(num)
            else:
                freq[i+1].append(num)
                i+=1

        return max(len(sublist) for sublist in freq)
