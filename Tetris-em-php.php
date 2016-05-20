<?php
$peca = array();            //Array que armazena a peça
$tabuleiro = array();       //Array que armazena o tabuleiro
$maxCleanLines = 0;         //Máximo de linhas eliminadas com a peça
$posX = 0;                  //Posição X da peça no tabuleiro que elimina o máximo de linhas
$posY = 0;                  //Posição Y da peça no tabuleiro que elimina o máximo de linhas

fscanf(STDIN, "%d %d",
    $SW,                    //Largura da peça
    $SH                     //Altura da peça
);

//Leitura de cada linha da peça
for ($i = 0; $i < $SH; $i++){
    $peca[$i] = $SROW = stream_get_line(STDIN, 4 + 1, "\n");    
}

fscanf(STDIN, "%d %d",
    $FW,                    //Largura do tabuleiro
    $FH                     //Altura do tabuleiro
);

//Leitura de cada linha do tabuleiro
for ($i = 0; $i < $FH; $i++){
    $tabuleiro[$i] = $FROW = stream_get_line(STDIN, 20 + 1, "\n");
}

//Percorre cada posição do tabuleiro tentando encaixar a peça
for($i = 0 ; $i < $FH; $i++){
    for($j = 0 ; $j < $FW; $j++){
        $auxTabuleiro = $tabuleiro;     //Tabuleiro com a adição da peça
        
        //Verificação se a peça encaixa no tabuleiro nesse ponto
        if(($i + $SH)-1 < $FH && ($j + $SW)-1 < $FW){
            $ocupado = false;
            for($y = 0; $y < $SH; $y++){
                for($x = 0; $x < $SW; $x++){
                    
                    //Verifica se a posição já está ocupada no tabuleiro
                    if($peca[$y][$x] == "*"){
                        if($tabuleiro[$i+$y][$j+$x] == "*"){
                            $ocupado = true;    
                        }else{
                            $auxTabuleiro[$i+$y][$j+$x] = $peca[$y][$x];    //Adiciona peça ao tabuleiro   
                        }                        
                    }
                    
                }                
            }
        }

        //Se a peça está encaixado no tabuleiro
        if(!$ocupado){        
            //Verificar as linhas completas com a adição da peça
            $countClean = 0;
            for($k = 0 ; $k < $FH; $k++){
                $cleanLine = true;
                for($l = 0 ; $l < $FW; $l++){
                    if($auxTabuleiro[$k][$l] != "*"){
                        $cleanLine = false;
                        break;
                    }
                }
                if($cleanLine) $countClean++;       //Aumenta número de linhas limpas
            }
                
            //Atualiza a melhor posição para encaixar a peça
            //Preferência para a última posição encontrada, ou seja, a mais no chão do tabuleiro
            if($countClean >= $maxCleanLines){
                $posX = $j;
                $posY = ($FH - $i) - 1;
                $maxCleanLines = $countClean;
            }
        }
    }    
}

echo("{$posX} {$posY}\n");
echo("{$maxCleanLines}\n");
?>
