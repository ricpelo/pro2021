public class Calculadora {
    public static void main(String[] args) {
        int op1 = Integer.parseInt(args[0]);
        int op2 = Integer.parseInt(args[2]);
        String op = args[1];

        switch (op) {
            case "+":
                System.out.println(op1 + op2);
                break;

            case "-":
                System.out.println(op1 - op2);
                break;

            case "/":
                System.out.println((double) op1 / op2);
                break;
        }
    }
}
