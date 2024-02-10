import java.util.*;
public class Main{
    static int calculate(int n,int[] x){
        int c=0;
        for(int i=0;i<36;i++){
            if(x[i]==n){
                c+=1;
            }
        }
        return c;
    }
    public static int[] removeElements(int[] array, int index1, int index2) {
        
        int newSize = array.length - 2; 
        int[] newArray = new int[newSize];
        int newIndex = 0;

        for (int i = 0; i < array.length; i++) {
            if (i != index1 && i != index2) {
                newArray[newIndex++] = array[i];
            }
        }

        return newArray;
    }
    public static int compare(double[] arr1,double[] arr2){
        for (int z = 0; z < arr1.length; z++) {
            if (arr1[z] != arr2[z]) {
                    return 0;             
            }
            }
        return 1;
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = 2; //Number of dices used
        int sides = 6; //Number of sides in a dice
        int[] dice1 = {1,2,3,4,5,6};
        int[] dice2 = {1,2,3,4,5,6};
        int[] sum = new int[36];
        
        double[] prob = new double[11];
        int pc = 0;
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
            System.out.println(count);
            double probability = (double)count/36;
            prob[pc] = probability;
            System.out.println("Probability of "+k+" = "+prob[pc]);
            pc+=1;
        }
        int[] NewDice1 = {1,4,0,0,0,0};
        int[] NewDice2 = {1,8,0,0,0,0};
        int a1=2,a2=2,a3=2,a4=2;
        for(int i=0;i<5;i++){
            if(i==1){
                a1+=1;
            }
            if(i==2){
                a2+=1;
            }
            if(i==3){
                a3+=1;
            }
            if(i==4){
                a4+=1;
            }
            NewDice1[2] = a1;
            NewDice1[3] = a2;
            NewDice1[4] = a3;
            NewDice1[5] = a4;
            for(int x=0;x<6;x++){
                int[] comb = {2,3,4,5,6,7};
                for(int y=0;y<6;y++){
                    if(x==y){
                        continue;
                    }
                    else{
                        
                        int[] newArray = removeElements(comb, x, y);
                        //System.out.println(Arrays.toString(newArray));
                        NewDice2[2] = newArray[0];
                        NewDice2[3] = newArray[1];
                        NewDice2[4] = newArray[2];
                        NewDice2[5] = newArray[3];
                        
                        int[] sum11 = new int[36];
                        double[] prob11 = new double[11];
                        int pc1 = 0;
                        int value1 = 0;
                        double count1;
                        for(int i1=0;i1<sides;i1++){
                            for(int j1=0;j1<sides;j1++){
                                sum11[value1] = NewDice1[i1]+NewDice2[j1];
                                value1+=1;
                            }
                        }
                        for(int k1=2;k1<=12;k1++){
                            count1=calculate(k1,sum11);
                            double probability1 = (double)count1/36;
                            prob11[pc1] = probability1;
                            pc1+=1;
                        }
                        int cv = compare(prob,prob11);
                        //System.out.println(cv);
                        if(cv==1){
                            System.out.println("The solution is :");
                            System.out.println(Arrays.toString(NewDice1));
                            System.out.println(Arrays.toString(NewDice2));
                        }
                        
                        
                        
                    }
                }
            }
            
        }
        
        
        
        
    }
}
