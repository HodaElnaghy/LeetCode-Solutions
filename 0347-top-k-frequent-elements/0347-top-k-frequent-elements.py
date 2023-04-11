class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        array=[]
        for num in nums :
            hash_table[num]= 1 + hash_table.get(num,0)
            
        sorted_hash = dict(sorted(hash_table.items(), key=lambda item: item[1], reverse=True))
        
        for i, key in enumerate(sorted_hash.keys()):
            if i == k:
                break
            array.append(key)
            
        return array
