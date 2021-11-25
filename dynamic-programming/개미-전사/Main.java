import java.util.*;

public class Main {

    public static int[] dp = new int[100];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] foods = new int[n];
        for (int i = 0; i < n; i++) {
            foods[i] = sc.nextInt();
        }

        dp[0] = foods[0];
        dp[1] = Math.max(foods[0], foods[1]);
        for (int i = 2; i < n; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + foods[i]);
        }

        System.out.println(dp[n - 1]);
    }

}
