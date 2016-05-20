<?php

$alignment = stream_get_line(STDIN, 7 + 1, "\n");
fscanf(STDIN, "%d",
    $n
);

$linhas = array();  //array que contém o texto
$mLinha = 0;        //Maior linha, todas as outras linhas se baseam na maior

for ($i = 0; $i < $n; $i++){
    $linhas[$i] = $text = stream_get_line(STDIN, 256 + 1, "\n");

    if(strlen($text) > $mLinha) $mLinha = strlen($text);
}

if($alignment == "LEFT"){
//Apenas imprime o texto como foi obtido
}
elseif($alignment == "RIGHT"){
    for($i = 0; $i < $n; $i++){
        //Enquanto a linha menor não tem o mesmo tamanho que a mairo são adicionados espaços a esquerda
        while(strlen($linhas[$i]) < $mLinha){
            $linhas[$i] = " " . $linhas[$i];    //Adição dos espaços 
        }
    }
}
elseif($alignment == "CENTER"){
    for($i = 0; $i < $n; $i++){
        $numEspacos = floor(($mLinha-strlen($linhas[$i]))/2);   //Espaços a adicionar a esquerda
        for($j = 0; $j < $numEspacos; $j++){
            $linhas[$i] = " " . $linhas[$i];                    //Adição dos espaços
        }
    }
}
elseif($alignment == "JUSTIFY"){
    for($i = 0; $i < $n; $i++){
        
        $numEspacosTotal = $mLinha - strlen($linhas[$i]);   //Espaços a adicionar a esquerda
        $words = explode(' ', $linhas[$i]);                 //Palavras da linha
        
        $razao = $numEspacosTotal / (count($words)-1);      //Número de espaço / pares de palavras
        $espAdd = 0;                                        //Número de espaços adicionados na iteração
        $espAddAnterior = 0;                                //Número de espaços adicionados até a iteração anterior

        $linhas[$i] = "";
        for($j = 0 ; $j < count($words)-1; $j++){
            $linhas[$i] .= $words[$j] . " ";                //Adição das palavras
            
            $espAddAnterior = floor($espAdd);
            $espAdd += $razao;
            $numEspacos = floor($espAdd) - $espAddAnterior; //Num espaços a serem adicionados neste par de palavras
            
            for($k = 0 ; $k < $numEspacos; $k++){
                $linhas[$i] .= " ";                         //Adição dos espaços
            }
        }
        $linhas[$i] .= $words[count($words)-1];             //Última palavra
    }
}

//Imprime o texto
for($i = 0; $i < $n; $i++){
    echo("{$linhas[$i]}\n");   
}
?>
