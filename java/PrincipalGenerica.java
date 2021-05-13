import java.util.List;
import java.util.ArrayList;

public class PrincipalGenerica {
    public static void main(String[] args) {
        // ClaseGenerica<String> cs = new ClaseGenerica<>();
        // cs.setValor("hola");
        // System.out.println(cs.getValor());
        // ClaseGenerica<Integer> ci = new ClaseGenerica<>();
        // ci.setValor(25);
        // System.out.println(ci.getValor());

        ArrayList<String> lista = new ArrayList<>();
        lista.add("pepe");
        System.out.println(longitud(lista));
        ArrayList<Integer> lista2 = new ArrayList<>();
        lista2.add(25);
        System.out.println(longitud(lista2));

        List<List<Integer>> lli = new ArrayList<>();

        lli.add(lista2);
        System.out.println(longitud(lli));
    }

    public static <T> int longitud(List<T> a) {
        return a.size();
    }
}
