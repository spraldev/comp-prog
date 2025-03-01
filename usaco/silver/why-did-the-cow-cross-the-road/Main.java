import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("helpcross.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("helpcross.out")));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int C = Integer.parseInt(st.nextToken());    
        int N = Integer.parseInt(st.nextToken());    

        int[] chickens = new int[C];
        int[][] cows = new int[N][2];

        for (int i = 0; i < C; i++) {
            chickens[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < N; i++) {
            // input will be a pair of integers
            st = new StringTokenizer(br.readLine());
            cows[i][0] = Integer.parseInt(st.nextToken());
            cows[i][1] = Integer.parseInt(st.nextToken());
        }

        HashSet<String> setCh = new HashSet<String>();
        HashSet<String> setC = new HashSet<String>();

        int anws = 0;

        for (int ch : chickens) {
            for (int[] c : cows) {
                if (c[0] <= ch && ch <= c[1] && !setCh.contains(ch + "") && !setC.contains(Arrays.toString(c))) {
                    setCh.add(ch + "");
                    setC.add(Arrays.toString(c));
                    anws++;
                    break;

                }
            }
        }


        pw.println(anws);


        
        

        br.close();
        pw.close();
    }

}