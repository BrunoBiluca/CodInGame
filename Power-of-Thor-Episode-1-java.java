import java.util.*;
import java.io.*;
import java.math.*;

class Player {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int lightX = in.nextInt(); // the X position of the light of power
        int lightY = in.nextInt(); // the Y position of the light of power
        int initialTX = in.nextInt(); // Thor's starting X position
        int initialTY = in.nextInt(); // Thor's starting Y position

        // game loop
        while (true) {
            int remainingTurns = in.nextInt(); 
            
            String direcao = ""; //Caminho de Thor 
            
            //Verifica a direção para Norte ou Sul
            if(initialTY < lightY){
                initialTY++;
                direcao += "S";
            }
            else if(initialTY > lightY){
                initialTY--;
                direcao += "N";                
            }

            //Verifica a direção para Leste ou Oeste
            if(initialTX < lightX){
                initialTX++;
                direcao += "E";
            }
            else if(initialTX > lightX){
                initialTX--;
                direcao += "W";                
            }

            System.out.println(direcao);
        }
    }
}
