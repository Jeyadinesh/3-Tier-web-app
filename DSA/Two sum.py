
def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen={}
    for i,v in enumerate(nums):
        num=target-v
        if num in seen:
            return[seen[num],i]

        seen[v]=i
    return []
