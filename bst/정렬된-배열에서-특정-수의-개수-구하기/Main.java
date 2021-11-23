import java.util.*;

public class Main {

    public static int lowerBound(ArrayList<Integer> a, int x) {
        int start = 0;
        int end = a.size();
        while (start < end) {
            int mid = (start + end) / 2;
            if (a.get(mid) >= x) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return end;
    }

    public static int upperBound(ArrayList<Integer> a, int x) {
        int start = 0;
        int end = a.size();
        while (start < end) {
            int mid = (start + end) / 2;
            if (a.get(mid) <= x) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return end;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            arr.add(sc.next());
        }

        int lower = lowerBound(arr, x);
        int upper = upperBound(arr, x);

        int result = upper - lower;
        if (result != 0) {
            System.out.println(result);
        } else {
            System.out.println(-1);
        }
    }

}
