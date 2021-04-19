import java.math.BigInteger;

class Matematicas {
    public static int mcd(int a, int b) {
        return BigInteger.valueOf(a)
            .gcd(BigInteger.valueOf(b))
            .intValue();
    }
}
