import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

class Solution {
    private final int n;
    private final List<Integer> logs;

    public Solution(int n, List<Integer> logs) {
        this.n = n;
        this.logs = logs;
    }

    public int solve() {
        return get_max_diff(re_order_logs());
    }

    private int get_max_diff(List<Integer> new_logs) {
        int max_diff = 0;

        for (int i = 0; i < n; ++i) {
            int prev = i;
            int next = (i + 1) % n;
            max_diff = Math.max(Math.abs(new_logs.get(next) - new_logs.get(prev)), max_diff);
        }

        return max_diff;
    }

    private List<Integer> re_order_logs() {
        Collections.sort(logs);
        Stack<Integer> st = new Stack<>();
        List<Integer> re_ordered_logs = new ArrayList<>();

        for (int i = 0; i < n; ++i) {
            if (is_Odd(i))
                st.push(logs.get(i));
            else
                re_ordered_logs.add(logs.get(i));
        }

        while (!st.empty()) {
            re_ordered_logs.add(st.pop());
        }

        return re_ordered_logs;
    }

    private boolean is_Odd(int idx) {
        return idx % 2 == 1;
    }


}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));
        int test_case = Integer.parseInt(br.readLine());

        for (int i = 0; i < test_case; ++i) {
            int n = Integer.parseInt(br.readLine());
            List<Integer> logs = Arrays.stream(br.readLine().split(" "))
                    .map(Integer::parseInt)
                    .collect(Collectors.toList());

            Solution sol = new Solution(n, logs);
            System.out.println(sol.solve());
        }
    }

}
