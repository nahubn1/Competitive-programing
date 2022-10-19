class Solution:
	def totalFruit(self, nums: List[int]) -> int:

		k = 2
		left = 0
		hashmap = {}

		for right in range(len(nums)):
			if nums[right] not in hashmap:
				k -= 1
				hashmap[nums[right]] = 1
			elif nums[right] in hashmap:
				hashmap[nums[right]] += 1

			if k < 0:
				if hashmap[nums[left]] == 1:
					del hashmap[nums[left]]
					k += 1
				else:
					hashmap[nums[left]] -= 1
				left += 1
       
		return right - left + 1
        
