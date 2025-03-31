import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[][] cows;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("moocast.in"));
        PrintWriter pw = new PrintWriter(new FileWriter("moocast.out"));

        // read the input
        N = Integer.parseInt(br.readLine().trim());
        cows = new int[N][2];

        for (int i = 0; i < N; i++) {
            String[] parts = br.readLine().trim().split("\\s+");
            cows[i][0] = Integer.parseInt(parts[0]);
            cows[i][1] = Integer.parseInt(parts[1]);
        }

        br.close();

        // binary search

        int anws = 0;

        int lo = 0;
        int hi = 1000000000;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;

            if (check(mid, cows)) {
                anws = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }

        // close stuff lol

        pw.println(anws);
        pw.close();

        
    }

    // sq dist

    public static int squared_distace(int[] cow1, int[] cow2) {
        return (cow1[0] - cow2[0]) * (cow1[0] - cow2[0]) + (cow1[1] - cow2[1]) * (cow1[1] - cow2[1]);
    }



    public static boolean check(int P, int[][] cows) {
        // build the graph
        
        HashMap<Integer, ArrayList<Integer>> adj = new HashMap<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (i == j) {
                    continue;
                }

                if (squared_distace(cows[i], cows[j]) <= P) {
                    adj.putIfAbsent(i, new ArrayList<>());
                    adj.get(i).add(j);
                }
            }
        }

        boolean p = false;

        // bfs

        for (int i = 0; i < N; ++i) {
            Deque<Integer> q = new ArrayDeque<>();
            Boolean[] visited = new Boolean[N];

            for (int j = 0; j < N; j++) {
                visited[j] = false;
            }


            q.add(i);
            visited[i] = true;

            while (!q.isEmpty()) {
                int node = q.poll();
                if (adj.containsKey(node)) {
                    for (int neighbor : adj.get(node)) {
                        if (!visited[neighbor]) {
                            visited[neighbor] = true;
                            q.add(neighbor);
                        }
                    }
                }
            }

            // check if all nodes have been visited

            if (Arrays.stream(visited).allMatch(b -> b)) {
                p = true;
                break;
            }
        }

        return p;
    }


}
