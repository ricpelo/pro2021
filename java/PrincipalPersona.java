public class PrincipalPersona {
    public static void main(String[] args) {
        Persona p = new Persona("Ricardo Pérez");

        try {
            Persona o = p.clone();
            System.out.println(p.nombre);
            System.out.println(p.numero);
            System.out.println(o.nombre);
            System.out.println(o.numero);
            System.out.println(p.equals(o));
        } catch (CloneNotSupportedException e) {
            System.err.println("Error al intentar clonar algo que no es clonable.");
        }
    }
}
