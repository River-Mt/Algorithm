import java.io.*;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Optional;
import java.util.Queue;

class CustomQueue {
    private Deque<Integer> queue;

    public CustomQueue() {
        queue = new LinkedList<>();
    }

    public void push(int value) {
        queue.addLast(value);
    }

    public int pop() {
        return empty() == 1 ? -1 : queue.pollFirst();
    }

    public int size() {
        return queue.size();
    }

    public int empty() {
        return queue.isEmpty() ? 1 : 0;
    }

    public int front() {
        return empty() == 1 ? -1 : queue.getFirst();
    }

    public int back() {
        return empty() == 1 ? -1 : queue.getLast();
    }

}
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        CustomQueue customQueue = new CustomQueue();

        for (int i = 0; i < n; ++i) {
            String line = br.readLine();
            String[] tokens = line.split(" ");
            String command = tokens[0];

            switch (command) {
                case "push":
                    customQueue.push(Integer.parseInt(tokens[1]));
                    break;
                case "pop":
                    bw.write(Integer.toString(customQueue.pop()));
                    bw.newLine();
                    break;
                case "size":
                    bw.write(Integer.toString(customQueue.size()));
                    bw.newLine();
                    break;
                case "empty":
                    bw.write(Integer.toString(customQueue.empty()));
                    bw.newLine();
                    break;
                case "front":
                    bw.write(Integer.toString(customQueue.front()));
                    bw.newLine();
                    break;
                default:
                    bw.write(Integer.toString(customQueue.back()));
                    bw.newLine();
                    break;
            }
        }

        br.close();
        bw.close();
    }
}
