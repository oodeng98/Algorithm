import java.util.Scanner;
import java.util.ArrayList;

class Solution
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i=0;i<n;i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            ArrayList<Integer> list1 = new ArrayList<>();
            ArrayList<Integer> list2 = new ArrayList<>();
            for(int j=0;j<a;j++){
                list1.add(sc.nextInt());
            }
            for(int j=0;j<b;j++){
                list2.add(sc.nextInt());
            }
            int max = 0;
            for(int j=0;j<Math.abs(a - b) + 1;j++){
                int temp = 0;
                if (a>b){
                    for(int k=0;k<b;k++){
                        temp += list1.get(k + j) * list2.get(k);
                    }
                }
                else{
                    for(int k=0;k<a;k++){
                        temp += list1.get(k) * list2.get(k + j);
                    }
                }
                max = Math.max(max, temp);
            }
            System.out.println("#" + (i + 1) + " " + max);
        }
        
    }
}