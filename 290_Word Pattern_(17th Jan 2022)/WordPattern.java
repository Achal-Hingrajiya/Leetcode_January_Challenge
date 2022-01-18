class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] word=s.split(" ");
        if(word.length!=pattern.length())
            return false;
        HashMap<Character,String> hm=new HashMap<>();
        HashSet<String> hs=new HashSet<>();
        
        for(int i=0;i<pattern.length();i++){
            char ch=pattern.charAt(i);
            if(hm.containsKey(ch)){
                if(!word[i].equals(hm.get(ch)))
                    return false;
            }
            else{
                if(hs.contains(word[i]))
                    return false;
                else{
                hs.add(word[i]);
                hm.put(ch,word[i]);
                }
            }
        }
        return true;
    }
}
