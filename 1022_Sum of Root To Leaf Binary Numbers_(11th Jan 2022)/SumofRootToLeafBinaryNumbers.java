class Solution {
    int ans=0;
        
    public int sumRootToLeaf(TreeNode root) {
        sumIndividual(root,0);
        return ans;
    }
    
    public void sumIndividual(TreeNode node,int sum){
        if(node==null)
            return;
        sum<<=1;
        sum+=node.val;
        
        if(node.left==null && node.right==null){
            ans+=sum;
            return;
        }
      
        sumIndividual(node.left, sum);
        sumIndividual(node.right, sum);
           
    }
}
