class Solution {
    public int myAtoi(String s) {
        if(s.length()==0)
            return 0;
        long number=0;
        s=s.trim();
        if(s.length()==0)
            return 0;
        int sign=1;
        if(s.charAt(0)=='-')
            sign=-1;
        int i=(s.charAt(0)=='+' || s.charAt(0)=='-')?1:0;
        
        while(i<s.length()){
            int ascii=s.charAt(i)-'0';
            if(ascii>=0 && ascii<=9){
                    number*=10;
                    number+=ascii;
             }
            else 
                break;
            if(sign==-1 && -1*number<Integer.MIN_VALUE)
                return Integer.MIN_VALUE;
            if(sign==1 && number>Integer.MAX_VALUE)
                return Integer.MAX_VALUE;
            i++;
            
         }
        
        return (int)(number*sign); 
    }
}
