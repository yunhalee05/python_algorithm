// import java.io.BufferedReader;
// import java.io.IOException;
// import java.io.InputStreamReader;
// import java.util.Arrays;

// public class test{
//     public static void main(String[] args) throws IOException{
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         String[] inputs = br.readLine().split(" ");
//         int n = Integer.parseInt(inputs[0]);
//         int k = Integer.parseInt(inputs[1]);

//         int[][] product = new int[n][2];
//         int[] dp = new int[k+1];
    
//         for(int i = 0; i<n; i++){
//             inputs = br.readLine().split(" ");
//             product[i][0] = Integer.parseInt(inputs[0]);
//             product[i][1] = Integer.parseInt(inputs[1]);
//             for (int j =k ; j>(product[i][0]-1); j--){
//                 dp[j] = Math.max(dp[j-product[i][0]]+ product[i][1], dp[j]);
//             }

//         }
//         System.out.println(Arrays.stream(dp).max().getAsInt());
//     }
// }


// import java.util.*;
// import java.io.BufferedReader;
// import java.io.IOException;
// import java.io.InputStreamReader;
// import java.util.Arrays;


// public class test{

//     static int answer = 0;
//     static boolean[] check = new boolean[10];
//     static HashSet<Integer> arr = new HashSet<>();
        
//     private static void createNumbers(int depth, String numbers, String tmp) {
//         if (depth == tmp.length()) {
//             Integer number = Integer.parseInt(tmp);
//             arr.add(number);
//             return;
//         }

//         for(int i = 0 ; i<numbers.length(); i++) {
//             if (!check[i]) {
//                 tmp += numbers.charAt(i);
//                 check[i] = true;
//                 createNumbers(depth, numbers, tmp);
//                 tmp.substring(0, tmp.length()-1);
//                 check[i] = false;
//             }
//         }
//     }
    
//     private static boolean isPrimeNumber(Integer number){
//         if (number == 0 || number == 1) {
//             return false;
//         }
//         for (int i = 2; i<=Math.sqrt(number); i++) {
//             if (number%i == 0) {
//                 return false;
//             }
//         }
//         return true;
//     }
    

//     public static void main(String[] args) throws IOException{
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         String n = br.readLine();

//         for( int i = 1; i<n.length()+1; i++){
//             createNumbers(i, n, "");
//         }
        
//         arr.forEach(a -> {
//             System.out.println(a);
//             if (isPrimeNumber(a)) {
//                 answer ++;
//             }
//         });

//     }
    
// }

