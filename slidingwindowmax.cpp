#include<deque>
class Solution {
public:
vector<int> maxSlidingWindow(vector<int>& nums, int k) {
deque<int>maa;
vector<int>ans;
for(int i=0;i<nums.size();++i){
    if(!maa.empty() && maa.front()<=i-k){
        maa.pop_front();
    }
    while(!maa.empty() && nums[maa.back()]<nums[i]){
        maa.pop_back();
    }
    maa.push_back(i);
    if(i>=k-1){
        ans.push_back(nums[maa.front()]);
    }
}
return ans;
}


};
