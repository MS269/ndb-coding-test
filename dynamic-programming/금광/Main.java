import java.util.*;

public class Main {

    static int testCase, n, m;
    static int[][] dp = new int[20][20];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        testCase = sc.nextInt();
        for (int tc = 0; tc < testCase; tc++) {
            n = sc.nextInt();
            m = sc.nextInt();
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    dp[i][j] = sc.nextInt();
                }
            }

            for (int j = 1; j < m; j++) {
                for (int i = 0; i < n; i++) {
                    int leftUp = 0, leftDown = 0, left = 0;

                    if (i != 0) {
                        leftUp = dp[i - 1][j - 1];
                    }

                    if (i != n - 1) {
                        leftDown = dp[i + 1][j - 1];
                    }

                    left = dp[i][j - 1];

                    dp[i][j] = dp[i][j] + Math.max(leftUp, Math.max(leftDown, left));
                }
            }

            int result = 0;
            for (int i = 0; i < n; i++) {
                result = Math.max(result, dp[i][m - 1]);
            }
            System.out.println(result);
        }
    }

}
