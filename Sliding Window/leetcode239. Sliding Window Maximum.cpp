class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        vector<int> res;
        // nums = [1,3,-1,-3,5,3,6,7], k = 3
        for(int i=0;i<nums.size();i++) {
            
            while(!dq.empty() && nums[i] > nums[dq.back()])
                dq.pop_back();
            
            dq.push_back(i);
            
            if(i>=k-1){
                if(!dq.empty() && (i - dq.front() >= k))
                    dq.pop_front();
                res.push_back(nums[dq.front()]);
            }
        }
        
        return res;
    }
};