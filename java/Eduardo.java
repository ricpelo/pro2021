public class Eduardo {
    public static void main(String[] args) {
        int[][] m = new int[3][3];
        final int w;

        w = 1;

        int c = 0;
        for (int i = 0; i < m.length; i++) {
            for (int j = 0; j < m[i].length; i++) {
                m[i][j] = c++;
            }
        }
    }
}

// Visibilidad predeterminada
class Juan {

}
