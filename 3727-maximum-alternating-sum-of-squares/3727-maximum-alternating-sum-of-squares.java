class Solution {
    public long maxAlternatingSum(int[] nums) {
        int n = nums.length;
        long[] squares = new long[n];
        
       
        for (int i = 0; i < n; i++) {
            long x = nums[i];
            squares[i] = x * x;
        }
        
       
        Arrays.sort(squares);
        
        long score = 0;
        
        for (int i = 0; i < n; i++) {
            if (i < n / 2) {
                score -= squares[i];
            } else {
                score += squares[i];
            }
        }
        
        return score;
    }
}