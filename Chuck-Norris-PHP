<?php
$MESSAGE = stream_get_line(STDIN, 100 + 1, "\n");

$result = "";       //Inicia o resultado
$binary = "";       //Inicia o número binário
for($i = 0; $i < strlen($MESSAGE); $i++){
    //Desempacota uma string para dados binário
    //Nesta caso gera o código ASCII de cada caracter
    $ascii = unpack('H*', $MESSAGE[$i]);
    
    //Converte o número da base 16 para a base 2, gera uma string
    $numBi = base_convert($ascii[1], 16, 2);
    $aux = "";  //Auxiliar para deixar todos os números com 7 bit de tamanho
    for($j = 0; $j < (7 - strlen($numBi)); $j++){
        $aux .= "0";
    }
    
    $binary .= $aux . $numBi;   //Numéros binários de 7 bit
}

//Iterar sobre todo o número binário
$sequencia = false;     //Verifica se está em sequencia os números
$numSeq = '0';          //Número da sequência
for($j = 0; $j < strlen($binary); $j++){
    //Verifica se a sequencia de números foi trocada
    if(!$sequencia){
        if($binary[$j] == '0'){         // Sequencia de 0s
            $result .= "00 0";
            $numSeq = '0';
        }
        else if($binary[$j] == '1'){    // Sequencia de 1s
            $result .= "0 0";
            $numSeq = '1';
        }
        $sequencia = true;
    }else{
        if($numSeq != $binary[$j]){     //Verificar se a sequencia foi trocada
            $result .= " ";    
            $sequencia = false;         //Sequencia quebrada
            $j--;                       //Retorna a posição para ser adicionada
        }else{
            $result .= "0";
        }
    }
}

//error_log(var_export($binary, true));

echo("{$result}\n");
?>
