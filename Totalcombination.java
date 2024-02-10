import java.util.*;
public class Main{
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter the number of dice used :");
        int n = s.nextInt(); //Number of dices used
        int sides = 6; //Number of sides in a dice

        int totalCombinations = (int) Math.pow(sides,n);

        System.out.println("Total combinations: " + totalCombinations);
    }
}
