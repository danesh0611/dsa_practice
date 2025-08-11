class Solution {
  public:
    int minMeetingRooms(vector<int> &start, vector<int> &end) {
        // code here
        int count=0;
        int maxroom=0;
        sort(start.begin(),start.end());
        sort(end.begin(),end.end());
        int n=start.size();
        int i=0,j=0;
        while(i<n && j<n){
            if (start[i]<end[j]){
                count++;
                maxroom=max(maxroom,count);
                i++;
                
                
            }
            else{
                count--;
                j++;
            }
        }
        return maxroom;
    }};
