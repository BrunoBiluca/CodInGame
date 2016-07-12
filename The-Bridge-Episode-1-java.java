import java.util.*;
import java.io.*;
import java.math.*;

class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int road = in.nextInt(); // the length of the road before the gap.
        int gap = in.nextInt(); // the length of the gap.
        int platform = in.nextInt(); // the length of the landing platform.

        // game loop
        while (true) {
            int speed = in.nextInt(); // the motorbike's speed.
            int coordX = in.nextInt(); // the position on the road of the motorbike.

            String result = "";   //Ação tomada pela moto

            if(coordX < road-1){  //Antes do pulo
                if(speed < gap + 1) result = "SPEED"; 
                else if(speed > gap + 1) result = "SLOW";
                else result = "WAIT";
            }else if(coordX == road-1){ //Posição do pulo
                result = "JUMP";
            }else if(coordX > road-1){  //Depois do pulo
                result = "SLOW";    
            }
            
            System.out.println(result);
        }
    }
}
