/************************************************************************************
Problem: Dwarfs standing on the shoulders of giants
************************************************************************************/

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

//Estrutura do nodo em grafo
struct Node{
    public int id;  //Identificador do nodo
    public List<int> adjacentes; //Lista dos identificadores dos nodos adjacentes
    
    public Node(int id){
        this.id = id;
        adjacentes = new List<int>();
    }
}


class Solution{
    
    static int pessoas = 0;     //Número de pessoas influenciadas atual
    static int maxPessoas = 0;  //Número máximo de pessoas influenciadas
    static List<Node> lista = new List<Node>(); //Lista de adjacência dos nodos do grafo
    
    static void Main(string[] args){

        int n = int.Parse(Console.ReadLine()); // the number of relationships of influence
        for (int i = 0; i < n; i++){
            string[] inputs = Console.ReadLine().Split(' ');
            int x = int.Parse(inputs[0]); // a relationship of influence between two people (x influences y)
            int y = int.Parse(inputs[1]);
            if(!lista.Any(s => s.id == x)){ //Se não contém o nodo adiciona na lista
                Node novo = new Node(x);
                lista.Add(novo);
            }
            if(!lista.Any(s => s.id == y)){ //Se não contém o nodo adiciona na lista
                Node novo = new Node(y);
                lista.Add(novo);            
            }
            
            int index = lista.FindIndex(s => s.id == x);
            //Console.Error.WriteLine(index);
            lista[index].adjacentes.Add(y);
            //Console.Error.WriteLine(string.Join(",", lista[index].adjacentes.ToArray()));
        }
        
        for(int i = 0; i < lista.Count; i++){
            BuscaProfundidade(lista[i]);           
        }

        // The number of people involved in the longest succession of influences
        Console.WriteLine(maxPessoas);
    }
    
    //Função de busca em profundidade
    //A função desce na lista de adjacência até um nodo que não possui adjacentes
    //Depois esta lista volta na recursão até percorrer todo o grafo
    static void BuscaProfundidade(Node no){
        
        pessoas++;
        if(pessoas > maxPessoas) maxPessoas = pessoas;
        
        for(int j = 0; j < no.adjacentes.Count; j++){
            int index = lista.FindIndex(s => s.id == no.adjacentes[j]); //Busca o nó adjacente referente a lista de adjacencia
            BuscaProfundidade(lista[index]);
        }

        pessoas--;
        return;
    }
    
}
