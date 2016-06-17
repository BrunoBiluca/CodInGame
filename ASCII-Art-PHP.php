<?php
fscanf(STDIN, "%d",
    $L
);
fscanf(STDIN, "%d",
    $H
);
$T = stream_get_line(STDIN, 256 + 1, "\n");

//Alfabeto ASCII
$alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?";
$dicionario = array();
for ($i = 0; $i < $H; $i++){
    $ROW = stream_get_line(STDIN, 1024 + 1, "\n");
    
    //Para cada linha é acrescentada a letra no dicionário
    for($j = 0; $j < strlen($alfabeto); $j++){
        $dicionario[$alfabeto[$j]][$i] = substr($ROW, $j*$L, $L);
    }
}

$result = "";
for($i = 0; $i < $H; $i++){
    for($j = 0; $j < strlen($T); $j++){
        $letra = strtoupper($T[$j]); //Determina a letra a ser colocada na resposta
        //Se a letra não existe no dicionário ela é substituida por interrogação
        if(!array_key_exists($letra, $dicionario)) $letra = "?";
        $result .= $dicionario[$letra][$i]; //Acrescenta a letra na resposta
    }
    $result .= "\n"; //Quebra de linha quando todas letras da linha foram acrecentadas
}

echo("{$result}\n");
?>
