import java.io.*;
import java.util.Arrays;
import java.util.stream.LongStream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        long[] bars = Arrays.stream(br.readLine().split(" "))
                .mapToLong(Long::parseLong)
                .sorted()
                .toArray();

        long bar_length = LongStream.of(bars).sum();

        long ans = 0;

        for (long length : bars) {
            bar_length -= length;
            ans += bar_length * length;
        }

        bw.write(Long.toString(ans));
        br.close();
        bw.close();
    }
}
