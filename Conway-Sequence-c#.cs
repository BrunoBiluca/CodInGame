using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution{
    static void Main(string[] args){
        int R = int.Parse(Console.ReadLine()); //Número inicial
        int L = int.Parse(Console.ReadLine()); //Número da linha para mostrar

        string str = "" + R; //String de resultado
        for(int i = 1; i < L; i++){
            
            int count = 0;
            string[] numbers = str.Split(' '); //Divido os números da string
            string atual = numbers[0];
            str = "";
            
            for(int j = 0; j < numbers.Length; j++){
                if(numbers[j] == atual){
                    count++;                        //Conto os números iguais ao número atual
                } 
                else{
                    str += count + " " + atual + " ";
                    atual = numbers[j];             //Quando o número é diferente, atual é substituido pelo novo número e a contagem e reiniciada
                    count = 1;
                }
            }
            str += count + " " + atual; //Para o último número ele sai do loop antes de ser salvo na string
        }

        Console.WriteLine(str);
    }
}
