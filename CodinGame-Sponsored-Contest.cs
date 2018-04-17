using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;


class Player
{
    static void Main(string[] args)
    {
        int firstInitInput = int.Parse(Console.ReadLine());
        int secondInitInput = int.Parse(Console.ReadLine());
        int numCharacters = int.Parse(Console.ReadLine());

        int count = 0;
        // game loop
        while (true)
        {
            
            Console.Error.WriteLine("Initial input");
            Console.Error.WriteLine(firstInitInput);
            Console.Error.WriteLine(secondInitInput);
            Console.Error.WriteLine(numCharacters);

            string northRoomSide = Console.ReadLine();
            string eastRoomSide = Console.ReadLine();
            string southRoomSide = Console.ReadLine();
            string westRoomSide = Console.ReadLine();
            
            Console.Error.WriteLine("4 inputs");
            Console.Error.WriteLine(firstRoomSide);
            Console.Error.WriteLine(secondRoomSide);
            Console.Error.WriteLine(thirdRoomSide);
            Console.Error.WriteLine(fourthRoomSide);
            
            Console.Error.WriteLine("array input");
            // Last line is hero
            for (int i = 0; i < numCharacters - 1; i++)
            {
                string[] coordinates = Console.ReadLine().Split(' ');
                int x = int.Parse(coordinates[0]);
                int y = int.Parse(coordinates[1]);
                
                // Console.Error.WriteLine(x);
                // Console.Error.WriteLine(y);
            }
            
            string[] heroCoordinates = Console.ReadLine().Split(' ');
            int heroX = int.Parse(heroCoordinates[0]);
            int heroY = int.Parse(heroCoordinates[1]);
            Console.Error.WriteLine(heroX);
            Console.Error.WriteLine(heroY);


            // Write an action using Console.WriteLine()
            // To debug: Console.Error.WriteLine("Debug messages...");

            string moveNorth = "C";
            string moveSouth = "D";
            string moveWest = "E";
            string moveEast = "A";
            string holdOn = "B";

            // Determinar qual o personagem é movido pela resposta
            if(count == 0){
                Console.WriteLine(moveWest);
            }
            else {
                Console.WriteLine(moveSouth);
            }
            Console.Error.WriteLine(count);
            count++;
        }
    }
}
