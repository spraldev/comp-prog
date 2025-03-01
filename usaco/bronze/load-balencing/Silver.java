import java.io.*;
import java.util.*;

public class Silver {
    public static void main(String[] args) throws IOException {
        BufferedReader read = new BufferedReader(new FileReader("balancing.in"));
        int N = Integer.parseInt(read.readLine());
        int[][] cows = new int[N][2];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(read.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            cows[i][0] = x;
            cows[i][1] = y;
        }

        read.close();

        int result = solve(N, cows);

        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("balancing.out")));
        out.println(result);
        out.close();
    }

    public static int solve(int N, int[][] cows) {
        int[] x_vals = new int[N];
        int[] y_vals = new int[N];
        for (int i = 0; i < N; i++) {
            x_vals[i] = cows[i][0];
            y_vals[i] = cows[i][1];
        }

        Arrays.sort(x_vals);
        Arrays.sort(y_vals);

        Map<Integer, Integer> x_res = new HashMap<>();
        Map<Integer, Integer> y_res = new HashMap<>();


        for (int i = 1; i < N; i++) {
            double xMid = ((double)x_vals[i] - x_vals[i - 1]) / 2.0 + x_vals[i - 1];
            x_res.put(i, count_points_x(xMid, cows));
        }


        for (int i = 1; i < N; i++) {
            double yMid = ((double)y_vals[i] - y_vals[i - 1]) / 2.0 + y_vals[i - 1];
            y_res.put(i, count_points_y(yMid, cows));
        }

        List<Map.Entry<Integer,Integer>> x_entries = new ArrayList<>(x_res.entrySet());
        x_entries.sort(Comparator.comparingInt(Map.Entry::getValue));

        int xCount = Math.min(300, x_entries.size());

        List<Map.Entry<Integer,Integer>> y_entries = new ArrayList<>(y_res.entrySet());
        y_entries.sort(Comparator.comparingInt(Map.Entry::getValue));
        int yCount = Math.min(300, y_entries.size());

        int[] x_final = new int[xCount];
        int[] y_final = new int[yCount];

        for (int i = 0; i < xCount; i++) {
            int index = x_entries.get(i).getKey();
            x_final[i] = x_vals[index];
        }

        for (int i = 0; i < yCount; i++) {
            int index = y_entries.get(i).getKey();
            y_final[i] = y_vals[index];
        }


        Arrays.sort(x_final);
        Arrays.sort(y_final);


        int result = Integer.MAX_VALUE;
        for (int i = 1; i < x_final.length; i++) {
            double xMid = ((double)x_final[i] - x_final[i - 1]) / 2.0 + x_final[i - 1];

            for (int j = 1; j < y_final.length; j++) {
                double yMid = ((double)y_final[j] - y_final[j - 1]) / 2.0 + y_final[j - 1];

                int cur = count_points(xMid, yMid, cows);
                result = Math.min(result, cur);
            }
        }

        return result;
    }


    public static int count_points(double x, double y, int[][] cows) {
        int q1 = 0, q2 = 0, q3 = 0, q4 = 0;
        for (int[] c : cows) {
            if (c[0] > x && c[1] > y) {
                q1++;
            } else if (c[0] < x && c[1] > y) {
                q2++;
            } else if (c[0] < x && c[1] < y) {
                q3++;
            } else {
                q4++;
            }
        }
        return Math.max(Math.max(q1, q2), Math.max(q3, q4));
    }

    public static int count_points_x(double x, int[][] cows) {
        int q1 = 0, q2 = 0;
        for (int[] c : cows) {
            if (c[0] > x) q1++;
            else          q2++;
        }
        return Math.abs(q1 - q2);
    }


    public static int count_points_y(double y, int[][] cows) {
        int q1 = 0, q3 = 0;
        for (int[] c : cows) {
            if (c[1] > y) q1++;
            else          q3++;
        }
        return Math.abs(q1 - q3);
    }
}
