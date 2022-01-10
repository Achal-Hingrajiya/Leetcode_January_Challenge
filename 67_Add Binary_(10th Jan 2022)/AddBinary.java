class Solution {
    public String addBinary(String a, String b) {
        StringBuilder ans=new StringBuilder();
        int a_pointer=a.length()-1;
        int b_pointer=b.length()-1;
        int carry=0;
        
        while(a_pointer>=0 || b_pointer>=0){
            int sum=carry;
            if(a_pointer>=0)
                sum+=a.charAt(a_pointer)-'0';
            if(b_pointer>=0)
                sum+=b.charAt(b_pointer)-'0';
            ans.append(sum%2);
            carry=sum/2;
            
            a_pointer--;
            b_pointer--;
        }
        
        if(carry==1)
            ans.append(1);
        
        return ans.reverse().toString();
    }
}
