import java.util.*;
public class Combination{
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = 2; //Number of dices used
        int sides = 6; //Number of sides in a dice
        int[] dice1 = new int[6];
        int[] dice2 = new int[6];
        //Get the dice faces
        System.out.println("Enter the dice faces values for all 6 sides :");
        for(int i=0;i<sides;i++)
        {
            dice1[i]=s.nextInt();
            dice2[i]=dice1[i];
        }
        //Print the combinations
        System.out.println("The dice combinations are :");
        for(int i=0;i<sides;i++)
        {
            for(int j=0;j<sides;j++){
                System.out.println(dice1[i]+" "+dice2[j]);
            }
        }
    }
}
