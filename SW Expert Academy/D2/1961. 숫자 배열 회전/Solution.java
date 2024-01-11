import java.util.Scanner;
import java.util.ArrayList;

class Solution{
    public static void main(String[] args)    {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int i=0;i<T;i++){
            int N = sc.nextInt();
            ArrayList<Integer>[] list = new ArrayList[N];
            for(int j=0;j<N;j++){
                list[j] = new ArrayList<Integer>();
                for(int k=0;k<N;k++){
                    list[j].add(sc.nextInt());
                }
            }

            ArrayList<Integer> case1 = new ArrayList<>();
            for(int j=0;j<N;j++){
                for(int k=0;k<N;k++){
                    case1.add(list[N - k - 1].get(j));
                }
            }

            ArrayList<Integer> case2 = new ArrayList<>();
            for(int j=0;j<N;j++){
                for(int k=0;k<N;k++){
                    case2.add(list[N - 1 - j].get(N - 1 - k));
                }
            }

            ArrayList<Integer> case3 = new ArrayList<>();
            for(int j=0;j<N;j++){
                for(int k=0;k<N;k++){
                    case3.add(list[k].get(N - 1 - j));
                }
            }
            System.out.println("#" + (i + 1));
            for (int j=0;j<N;j++){
                for (int k=0;k<N;k++){
                    System.out.print(case1.get(j * N + k));
                }
                System.out.print(" ");
                for (int k=0;k<N;k++){
                    System.out.print(case2.get(j * N + k));
                }
                System.out.print(" ");
                for (int k=0;k<N;k++){
                    System.out.print(case3.get(j * N + k));
                }
                System.out.print("\n");
            }
        }
    }
}