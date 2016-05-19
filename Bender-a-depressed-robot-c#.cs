using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

/// <summary>
/// classe responsável por operar o nosso robozinho depressivo
/// </summary>
public class Bender{
    
    /// <summary>
    /// Estrutura para armazenar cada passo dado pelo Bender. É utilizada para imprimir e verificar o caminho
    /// </summary>
    public struct Passo{
        public string direcao;
        int x;
        int y;
        
        public Passo(string dir, int x, int y){
            this.direcao = dir;
            this.x = x;
            this.y = y;
        }
    }

    //******************** Atributos públicos ********************//

    
    public bool breakerMode;        //Modo que permite passar por pontos X no mapa
    public int x, y;                //Coordenadas no mapa
    public bool loop;               //Robot entrou em loop
    public List<Passo> caminho = new List<Passo>(); //Caminho percorrido pelo robot
    public string direcaoAtual;    //Direção atual
    
    
    //******************** Atributos públicos ********************//
    
    private bool jogos;
    private bool prostitutas;
    private string[] priorDirecao;  //Direções permitidas
    private int prioridade;         //Prioridade atual para as direções
    private Passo pontoLoop;        //Primeiro ponto de loop encontrado no mapa
    private bool primeiroPontoLoop; //Controla o primeiro ponto de loop
    
    /// <summary>
    /// Construtor
    /// <param name="x"> Coordenada da posição inicial do robot no mapa</param>
    /// <param name="y"> Coordenada da posição inicial do robot no mapa</param>
    /// </summary>
    public Bender(int x, int y){
        jogos = true;
        prostitutas = true;
        
        this.x = x;
        this.y = y;
        
        this.breakerMode = false;
        priorDirecao = new string[] {"SOUTH", "EAST", "NORTH", "WEST"};
        this.prioridade = 0;
        this.direcaoAtual = this.priorDirecao[prioridade];
        
        this.pontoLoop = new Passo("Nao", 0, 0);
        this.primeiroPontoLoop = false;
    }
    
    /// <summary>
    /// Inverte as prioridades do robot
    /// </summary>
    public void InverterPrioridades(){
        string aux;
        aux = this.priorDirecao[0];
        this.priorDirecao[0] = this.priorDirecao[3];
        this.priorDirecao[3] = aux;
        aux = this.priorDirecao[1];
        this.priorDirecao[1] = this.priorDirecao[2];
        this.priorDirecao[2] = aux;

    }
    
    /// <summary>
    /// Atualiza a direcaoAtual do robot para a próxima prioridade
    /// </summary>   
    public void ProxPrioridade(){
        this.direcaoAtual = this.priorDirecao[this.prioridade];
        this.prioridade++;
        if(this.prioridade == this.priorDirecao.Length) this.prioridade = 0;
    }
    
    /// <summary>
    /// Atualiza a direcaoAtual de acordo com uma casa no mapa
    /// <param name="direcao"> Direção para a qual a direcaoAtual será atualizada </param>
    /// </summary> 
    public void MudaDirecao(char direcao){
        if(direcao == 'S') this.direcaoAtual = "SOUTH";
        else if(direcao == 'E') this.direcaoAtual = "EAST";
        else if(direcao == 'N') this.direcaoAtual = "NORTH";
        else if(direcao == 'W') this.direcaoAtual = "WEST";
    }
    
    /// <summary>
    /// Atualiza a posição do robot de acordo com a direção atual
    /// Reinicia também a prioridade de direção e verifica se o robot entrou em Loop
    /// </summary> 
    public void Anda(){
        if(this.direcaoAtual == "SOUTH") this.y++;
        else if(this.direcaoAtual == "EAST") this.x++;
        else if(this.direcaoAtual == "NORTH") this.y--;
        else if(this.direcaoAtual == "WEST") this.x--;
        
        this.prioridade = 0;
        
        Passo novo = new Passo(this.direcaoAtual, this.x, this.y);
        if(!this.caminho.Contains(novo)){   //Passo já foi feito no mesmo lugar no mapa
            this.primeiroPontoLoop = false;
            this.pontoLoop = new Passo("Nao", 0, 0);
        }else{
            if(!this.primeiroPontoLoop){ //Crio ponto de loop
                this.pontoLoop = novo;
                this.primeiroPontoLoop = true;
            }else{ //Já tenho ponto de loop        
                if(this.pontoLoop.Equals(novo)){
                    this.loop = true;
                }
            }
        }
        this.caminho.Add(novo);
    }
    
}

class Solution{
    static void Main(string[] args){

        string[] inputs = Console.ReadLine().Split(' ');
        int L = int.Parse(inputs[0]);   //Número de linhas do arquivo
        int C = int.Parse(inputs[1]);   //Número de colunas do arquivo
        
        string[] mapa = new string[L];  //Mapa
        int posX = 0;
        int posY = 0;
        int[] tx = new int[2];          //Posição dos teleportadores
        int[] ty = new int[2];
        int tpos = 0;
        
        //Leitura do arquivo e inicialização das posições
        for (int i = 0; i < L; i++){
            string row = Console.ReadLine();
            mapa[i] = row;
            if(row.Contains("@")){
                posX = row.IndexOf("@");
                posY = i;
            }
            if(row.Contains("T")){
                tx[tpos] = row.IndexOf("T");
                ty[tpos] = i;
                tpos++;
            }
        }
        
        Bender bender = new Bender(posX, posY);
        
        //Loop principal
        while(true){
            
            //Verifica a próxima posição no mapa
            if(bender.direcaoAtual == "SOUTH"){
                posX = bender.x;
                posY = bender.y + 1;
            }
            else if(bender.direcaoAtual == "EAST"){
                posX = bender.x + 1;
                posY = bender.y;
            }
            else if(bender.direcaoAtual == "NORTH"){
                posX = bender.x;
                posY = bender.y - 1;
            }
            else if(bender.direcaoAtual == "WEST"){
                posX = bender.x - 1;
                posY = bender.y;
            }

            //Define o que deve ser feito dada a próxima direção do mapa
            if(mapa[posY][posX] == '#'){
                bender.ProxPrioridade();
            }
            else if(mapa[posY][posX] == 'I'){ 
                bender.Anda();
                bender.InverterPrioridades();
            }
            else if(mapa[posY][posX] == 'X'){
                if(!bender.breakerMode){
                    bender.ProxPrioridade();
                }else{
                    StringBuilder sb = new StringBuilder(mapa[posY]);
                    sb[posX] = ' ';
                    mapa[posY] = sb.ToString();
                    bender.Anda();
                }
            }
            else if(mapa[posY][posX] == 'N' || 
                    mapa[posY][posX] == 'E' || 
                    mapa[posY][posX] == 'W' || mapa[posY][posX] == 'S'){
                bender.Anda();
                bender.MudaDirecao(mapa[posY][posX]);
            }
            else if(mapa[posY][posX] == 'B'){ 
                bender.Anda();
                bender.breakerMode = (bender.breakerMode ? false : true);
            }
            else if(mapa[posY][posX] == 'T'){ 
                bender.Anda();
                if(posX == tx[0] && posY == ty[0]){
                    bender.x = tx[1];
                    bender.y = ty[1];
                }else{
                    bender.x = tx[0];
                    bender.y = ty[0];                    
                }
            }
            else if(mapa[posY][posX] == '$'){ 
                bender.Anda();
                break;
            }
            else{
                bender.Anda();
            }    

            if(bender.loop){
                break;    
            }
        }
        
        //Imprime o caminho obtido ou se foi LOOP
        if(bender.loop){
            Console.WriteLine("LOOP");    
        }else{
            foreach(var passo in bender.caminho){
                Console.WriteLine(passo.direcao);    
            }    
        }
    }
}
