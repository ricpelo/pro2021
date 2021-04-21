class ClaseExterna {
    int x = 10;

    class ClaseInterna {
        int y = 5;
    }
}

public class PrincipalInternaAnidada {
    public static void main(String[] args) {
        ClaseExterna miExterna = new ClaseExterna();
        ClaseExterna.ClaseInterna miInterna = miExterna.new ClaseInterna();
        System.out.println(miInterna.y + miExterna.x);
    }
}
