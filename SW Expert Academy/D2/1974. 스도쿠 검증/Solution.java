import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashSet;

class Solution{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int i=0;i<t;i++){
            ArrayList<Integer> list = new ArrayList<>();
            for(int j=0;j<81;j++){
                list.add(sc.nextInt());
            }
            int check = 0;
            for(int j=0;j<9;j++){
                HashSet<Integer> set1 = new HashSet<>();
                HashSet<Integer> set2 = new HashSet<>();
                
                for(int k=0;k<9;k++){
                    set1.add(list.get(j * 9 + k));
                    set2.add(list.get(j + k * 9));
                }
                if (set1.size() != 9 || set2.size() != 9){
                    check = 1;
                    break;
                }
            }
            HashSet<Integer> set3 = new HashSet<>();
            for(int j=0;j<3;j++){
                for(int k=0;k<3;k++){
                    set3.add(list.get(j * 27 + k * 3));
                    set3.add(list.get(j * 27 + k * 3 + 1));
                    set3.add(list.get(j * 27 + k * 3 + 2));
                    set3.add(list.get(j * 27 + 9 + k * 3));
                    set3.add(list.get(j * 27 + 9 + k * 3 + 1));
                    set3.add(list.get(j * 27 + 9 + k * 3 + 2));
                    set3.add(list.get(j * 27 + 18 + k * 3 + 0));
                    set3.add(list.get(j * 27 + 18 + k * 3 + 1));
                    set3.add(list.get(j * 27 + 18 + k * 3 + 2));
                    if (set3.size() != 9){
                        check = 1;
                        break;
                    }
                }
            }
            if (check == 1){
                result = 0;
                System.out.println("#" + (i + 1) + " 0");
            }
            else{
                System.out.println("#" + (i + 1) + " 1");
            }
        }
    }
}