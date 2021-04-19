public class Ambitos {
    public static void main(String[] args) {
        int x = 4;

        {
            int j = 5;

            System.out.println(x);
            System.out.println(j);
        }

        System.out.println(x);
        System.out.println(j);
    }
}
