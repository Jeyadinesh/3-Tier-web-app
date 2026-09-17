def longestConsecutive(self, nums: list[int]) -> int:
    snums=set(nums)
    longest=0
    for num in snums:
        if num-1 not in snums:
            length=0
            while (num+length) in snums:
                length+=1
            longest=max(length,longest)
    return longest
