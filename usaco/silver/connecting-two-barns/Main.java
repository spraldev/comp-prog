import java.util.*;
import java.io.*;

public class Main {

    public static void rec(int num) {
        if (num == 0) {
            return;
        }

        rec(num / 10);
        System.out.println(num % 10);
    }
}
