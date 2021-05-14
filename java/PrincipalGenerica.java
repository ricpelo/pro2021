import java.util.List;
import java.util.NoSuchElementException;
import java.util.ArrayList;
import java.util.Iterator;

public class PrincipalGenerica {
    public static void main(String[] args) {
        // ClaseGenerica<String> cs = new ClaseGenerica<>();
        // cs.setValor("hola");
        // System.out.println(cs.getValor());
        // ClaseGenerica<Integer> ci = new ClaseGenerica<>();
        // ci.setValor(25);
        // System.out.println(ci.getValor());

        List<StringBuilder> lst = new ArrayList<StringBuilder>();

        lst.add(new StringBuilder("a"));
        lst.add(new StringBuilder("b"));
        lst.add(new StringBuilder("c"));
        lst.add(new StringBuilder("d"));
        lst.add(new StringBuilder("e"));

        lst.forEach(PrincipalGenerica::sumaUno);

        Iterator<StringBuilder> it = lst.iterator();

        for (;;) {
            try {
                StringBuilder e = it.next();
                System.out.println(e);
            } catch (NoSuchElementException ex) {
                break;
            }
        }
    }

    public static void sumaUno(StringBuilder x) {
        x.append('z');
    }

    public static <T> int longitud(List<T> a) {
        return a.size();
    }
}
