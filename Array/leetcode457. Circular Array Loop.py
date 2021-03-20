# two pointer solution
# Same like https://leetcode.com/problems/linked-list-cycle/
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        self.N = len(nums)
        self.nums = nums
        for i in range(self.N):
            slow = i
            fast = self.moveToNext(slow)
            while nums[fast]*nums[i]>0 and nums[self.moveToNext(fast)]*nums[i]>0:
                if fast == slow:
                    if slow == self.moveToNext(slow):
                        break
                    return True
                slow = self.moveToNext(slow)
                fast = self.moveToNext(self.moveToNext(fast))
        return False
    
    def moveToNext(self, index):
        return (index + self.nums[index] + self.N) % self.N