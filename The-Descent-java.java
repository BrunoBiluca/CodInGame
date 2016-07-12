import java.util.*;
import java.io.*;
import java.math.*;

class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);

        int maiorM = 0; //Maior montanha
        int posM = 0;   //Posição da maior montanha

        // game loop
        while (true) {
            maiorM = 0;
            for (int i = 0; i < 8; i++) {
                int mountainH = in.nextInt(); // represents the height of one mountain, from 9 to 0.
                if(maiorM < mountainH) {    //Descobre a maior montanha
                    maiorM = mountainH;
                    posM = i;
                }
            }
            System.out.println(posM); // The number of the mountain to fire on.
        }
    }
}
