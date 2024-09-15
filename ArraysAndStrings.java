import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ArraysAndStrings {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int pre[] = new int[n];
        int suff[] = new int[n];
        pre[0] = 1;
        suff[n - 1] = 1;

        for(int i = 1; i < n; i++) {
            pre[i] = pre[i - 1] * nums[i - 1];
        }
        for(int i = n - 2; i >= 0; i--) {
            suff[i] = suff[i + 1] * nums[i + 1];
        }

        int ans[] = new int[n];
        System.out.println(Arrays.toString(pre));
        System.out.println(Arrays.toString(suff));
        for(int i = 0; i < n; i++) {
            ans[i] = pre[i] * suff[i];
        }
        return ans;
    }

    public int[] productExceptSelf2(int[] nums) {
        List<Integer> answer = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            int total = 1;
            if (i != 0) {
                int[] pre = Arrays.copyOfRange(nums, 0, i);
                int[] suff = Arrays.copyOfRange(nums, i + 1, nums.length);
                for (int k : pre) {
                    total *= k;
                }
                for (int l : suff) {
                    total *= l;
                }
                answer.add(total);
            } else {
                for (int j = i + 1; j < nums.length; j++) {
                    total *= nums[j];
                }
                answer.add(total);
            }
        }

        // Convert List<Integer> to int[]
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) {
        ArraysAndStrings solution = new ArraysAndStrings();
        int[] nums = {1, 2, 3, 4};
        int[] result = solution.productExceptSelf(nums); // call the non-static method
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
