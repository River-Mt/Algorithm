import java.io.*;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    static int n;
    static int q_cnt=0;
    static int[] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        map = new int[n];
        dfs(0);
        System.out.println(q_cnt);
        br.close();
    }

    public static void dfs(int now) throws IOException{

        if(now==n){
            q_cnt++;
            return;
        }

        for(int r=0;r<n;++r){
            map[now]=r;
            if(chk(now))dfs(now+1);
        }

    }

    public static boolean chk(int c){

        for(int i=0;i<c;++i) {
            if (map[c] == map[i]) return false;
            else if (Math.abs(c - i) == Math.abs(map[c] - map[i])) return false;
        }
        return true;
    }
    
}
