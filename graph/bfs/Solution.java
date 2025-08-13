class Solution {
    public ArrayList<Integer> bfs(ArrayList<ArrayList<Integer>> adj) {
        ArrayList<Integer> ans =  new ArrayList<>();
        boolean[] vis =  new boolean[adj.size()];
        Queue<Integer> q  =  new LinkedList<>();
        
        q.add(0);
        vis[0]=true;
        
        while(!q.isEmpty()){
            Integer node = q.poll();
            ans.add(node);
            for(Integer it : adj.get(node)){
                if(vis[it]==false){
                    vis[it]=true;
                    q.add(it);
                }
            }
        }
        return ans;
    }
}

