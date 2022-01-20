class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left=1,right=1;
        
        //range 1 to maxElement
        for(int pile:piles){
            right=Math.max(right,pile);
        }
        while(left<right){
            int mid=left+(right-left)/2;
            reqHours(piles,h,mid);
            if(reqHours(piles,h,mid)){
                right=mid;//equal to because sometimes there will be no optimised ans
            }
            else
                left=mid+1;
        }
        return left;
    }
    
    boolean reqHours(int[] piles, int h, int mid){
        for(int pile:piles){
            h-=(1+(pile-1)/mid);
        }     
        return h>=0;
    }
}
