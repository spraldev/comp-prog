import java.io.*;
import java.util.*;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("cowdance.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("cowdance.out")));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());    
        int T = Integer.parseInt(st.nextToken());    
        

        int[] cows = new int[N];

        for (int i = 0; i < N; i++) {
            cows[i] = Integer.parseInt(br.readLine());
        }

        int anws = 0;
        int lo = 1;
        int hi = N;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;

            if (res(mid, cows, T) <= T) {
                hi = mid - 1;
                anws = mid;
            } else {
                lo = mid + 1;
            }
        }

        pw.println(anws);   
        

        br.close();
        pw.close();
    }

    private static int max(ArrayList<Integer> list) {
        int max = Integer.MIN_VALUE;
        for (int num : list) {
            max = Math.max(max, num);
        }
        return max;
    }

    public static int res(int k, int[] cows, int T) {
        ArrayList<Integer> init = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            init.add(cows[i]);
        }
        ArrayList<Integer> other = new ArrayList<>();
        for (int i = k; i < cows.length; i++) {
            other.add(cows[i]);
        }
        init.sort(Comparator.naturalOrder());
        int time = init.get(0);

        for (int i = 0; i < init.size(); i++) {
            init.set(i, init.get(i) - time);
        }

        while (other.size() > 0) {
            init.sort(Comparator.naturalOrder());
            int zeroCount = 0;
            for (int i = 0; i < init.size(); i++) {
                if (init.get(i) == 0) {
                    zeroCount++;
                }
            }

            for (int j = 0;  j < zeroCount; j++) {
                if (other.size() > 0) {
                    int otherCow = other.get(0);
                    other.remove(0);
                    init.set(init.indexOf(0), otherCow);
                } else {
                    break;
                }
            }

            if (time + max(init) > T) {
                return time + max(init);
            }

            init.sort(Comparator.naturalOrder());
            time += init.get(0);
            int newTime = init.get(0);
            for (int i = 0; i < init.size(); i++) {
                init.set(i, init.get(i) - newTime);
            }


        }

        return time + max(init);
    }
}