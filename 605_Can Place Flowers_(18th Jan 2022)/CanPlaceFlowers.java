class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int len=flowerbed.length;
        int count = 0;
        for(int i = 0; i < len && count < n; i++) {
            if(flowerbed[i] == 0) {
	           int next = (i == flowerbed.length - 1) ? 0 : flowerbed[i + 1]; 
               int prev = (i == 0) ? 0 : flowerbed[i - 1];
               if(next == 0 && prev == 0) {
                   flowerbed[i] = 1;
                   count++;
               }
            }
        }
        
        return count == n;
    }
}
