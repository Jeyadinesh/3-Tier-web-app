def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    my_dict=dict.fromkeys(set(nums),0)
    for num in nums:
        if num in my_dict:
            my_dict[num]+=1 
             
    return sorted(my_dict,key=lambda x:my_dict[x],reverse=True)[:k]
