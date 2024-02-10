import java.util.*;
public class Probability{
    static int calculate(int n,int[] x){
        int c=0;
        for(int i=0;i<36;i++){
            if(x[i]==n){
                c+=1;
            }
        }
        return c;
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = 2; //Number of dices used
        int sides = 6; //Number of sides in a dice
        int[] dice1 = {1,2,3,4,5,6};
        int[] dice2 = {1,2,3,4,5,6};
        int[] sum = new int[36];
        int value = 0;
        double count;
        for(int i=0;i<sides;i++){
            for(int j=0;j<sides;j++){
                sum[value] = dice1[i]+dice2[j];
                value+=1;
            }
        }
        for(int k=2;k<=12;k++){
            count=calculate(k,sum);
            double probability = count/36;
            System.out.println("Probability of "+k+" = "+probability);
        }
        
        
    }
}
