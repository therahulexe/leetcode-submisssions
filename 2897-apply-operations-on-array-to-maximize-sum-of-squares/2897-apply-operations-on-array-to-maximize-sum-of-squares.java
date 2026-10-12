class Solution {
    public int maxSum(List<Integer> nums, int k) {
        int MOD = 1_000_000_007;
        int[] cnt = new int[31];

        
        for (int num : nums) {
            for (int b = 0; b < 31; b++) {
                if ((num & (1 << b)) != 0) {
                    cnt[b]++;
                }
            }
        }

        long ans = 0;

        
        for (int i = 0; i < k; i++) {
            long num = 0;

            for (int b = 0; b < 31; b++) {
                if (cnt[b] > 0) {
                    num |= (1L << b);
                    cnt[b]--;
                }
            }

            ans = (ans + num * num) % MOD;
        }

        return (int) ans;
    }
}