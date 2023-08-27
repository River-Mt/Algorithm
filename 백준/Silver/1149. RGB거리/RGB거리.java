import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));
        int n = Integer.parseInt(br.readLine());
        int[][] homes = new int[n][n];
        int[][] dp = new int[n + 1][n + 1];
        
        for (int i = 0; i < n; ++i) {
            String[] tokens = br.readLine().split(" ");
            for (int j = 0; j < tokens.length; ++j) {
                homes[i][j] = Integer.parseInt(tokens[j]);
            }
        }

        for (int i = 1; i <= n; ++i) {
            dp[i][0] = homes[i - 1][0] + Math.min(dp[i - 1][1], dp[i - 1][2]);
            dp[i][1] = homes[i - 1][1] + Math.min(dp[i - 1][0], dp[i - 1][2]);
            dp[i][2] = homes[i - 1][2] + Math.min(dp[i - 1][0], dp[i - 1][1]);
        }

        int ans = Math.min(dp[n][0], Math.min(dp[n][1], dp[n][2]));

        System.out.println(ans);
    }

}
