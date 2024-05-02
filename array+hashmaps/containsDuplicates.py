class SolutionOne:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo = set()
        for num in nums:
            if(num in memo):
                return True
            memo.add(num)
        return False
    
	
	
class SolutionTwo:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
