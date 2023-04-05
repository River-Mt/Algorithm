import java.io.*;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        Stack<Integer> stack = new Stack<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++) {
            String line = br.readLine();
            String[] tokens = line.split(" ");
            String cmd = tokens[0];

            if(cmd.equals("push")) {
                int x =Integer.parseInt(tokens[1]);
                push(stack, x);
            } else if(cmd.equals(("pop"))) {
                System.out.println(pop(stack));
            } else if(cmd.equals("size")) {
                System.out.println(size(stack));
            } else if(cmd.equals("empty")) {
                System.out.println(empty(stack));
            } else {
                System.out.println(top(stack));
            }
        }
    }

    public static void push(Stack<Integer> stack, int x) {
        stack.push(x);
    }
    public static int pop(Stack<Integer> stack) {
        int ret = top(stack);
        if(ret != -1)stack.pop();
        return ret;
    }
    public static int size(Stack<Integer> stack) {
        return stack.size();
    }
    public static int empty(Stack<Integer> stack) {
        return stack.empty()
                ? 1
                : 0;
    }
    public static int top(Stack<Integer> stack) {
        return empty(stack) == 1
                ? -1
                : stack.peek();
    }
}
