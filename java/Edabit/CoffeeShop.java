import java.util.Deque;

public class CoffeeShop {
    private String nombre;
    private MenuItem[] menu;
    private Deque<String> orders;

    /**
     * addOrder: adds the name of the item to the end of the orders array if it exists on
     * the menu. Otherwise, return "This item is currently unavailable!"
     */
    public String addOrder(String order) {
        MenuItem menuItem = menuItemFromNombre(order);

        if (menuItem != null) {
            orders.add(order);
            return "Order added!";

        }

        return "This item is currently unavailable!";
    }

    /**
     * fulfillOrder: if the orders array is not empty, return
     * "The {item} is ready!". If the orders array is empty, return
     * "All orders have been fulfilled!"
     */
    public String fulfillOrder() {
        if (orders.isEmpty()) {
            return "All orders have been fulfilled!";
        }

        String item = orders.removeFirst();
        return String.format("The %s is ready!", item);
    }

    /**
     * listOrders: returns the list of orders taken, otherwise, an empty array.
     */
    public String[] listOrders() {
        String[] ret = new String[orders.size()];
        int i = 0;

        for (String order : orders) {
            ret[i++] = order;
        }

        return ret;
    }

    /**
     * dueAmount: returns the total amount due for the orders taken.
     */
    public double dueAmount() {
        double ret = 0.0;

        for (String order : orders) {
            ret += menuItemFromNombre(order).getPrice();
        }

        return ret;
    }

    /**
     * cheapestItem: returns the name of the cheapest item on the menu.
     */
    public String cheapestItem() {
        double min = Double.POSITIVE_INFINITY;
        String ret = null;

        for (MenuItem item : menu) {
            if (item.getPrice() < min) {
                ret = item.getItem();
                min = item.getPrice();
            }
        }

        return ret;
    }

    private MenuItem menuItemFromNombre(String nombre) {
        for (MenuItem item : menu) {
            if (item.getItem().equals(nombre)) {
                return item;
            }
        }
        return null;
    }

}

class MenuItem {
	private String item;
	private String type;
	private double price;

	public MenuItem(String item, String type, double price) {
		this.item = item;
		this.type = type;
		this.price = price;
	}

	public String getItem() { return item; }
	public String getType() { return type; }
	public double getPrice() { return price; }
}
