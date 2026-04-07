class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # Create frequency buckets correctly
        freq = [[] for _ in range(len(nums) + 1)]
        for num, c in count.items():
            freq[c].append(num)

        res = []
        print(freq)
        # Traverse from high frequency to low
        for i in range(len(freq) - 1, 0, -1):
            if k==0:
                break
            if len(freq[i])>0:
                res+=freq[i]
                k-=len(freq[i])
        return res
                