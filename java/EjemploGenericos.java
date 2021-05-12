import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class EjemploGenericos {
    public static void main(String[] args) {
        List<String> lista = new ArrayList<String>();
        List<String> otro = new LinkedList(lista);

        lista.add("hola");
        lista.add("pepe");
        lista.add("juan");

        for (String e : lista) {
            System.out.println(e);
        }

        for (int i = lista.size() - 1; i >= 0; i--) {
            System.out.println(lista.get(i));
        }
    }
}
