import java.util.*;

class Main {
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        int C = scanner.nextInt();

        B += C;

        if (B >= 60)
        {
            int remain = B / 60;
            A += remain;
            B -= 60*remain;
            if (A >= 24)
            {
                A = A-24 ;
            }
        }
        System.out.print(A + " ");

        System.out.print(B);

    }
}