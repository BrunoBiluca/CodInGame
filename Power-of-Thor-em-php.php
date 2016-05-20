<?php
fscanf(STDIN, "%d %d %d %d",
    $lightX, // the X position of the light of power
    $lightY, // the Y position of the light of power
    $initialTX, // Thor's starting X position
    $initialTY // Thor's starting Y position
);

// game loop
while (TRUE){
    fscanf(STDIN, "%d",
        $remainingTurns // The remaining amount of turns Thor can move. Do not remove this line.
    );

    $direcao = "";  //Armazena a direção que Thor irá andar

    //Verifica a posição em Y
    //A posição inicial do Thor deve ser atualizada para a nova posição
    if($initialTY > $lightY){
        $initialTY--;
        $direcao = "N";
    }
    else if ($initialTY < $lightY){
        $initialTY++;
        $direcao = "S";
    }

    //Verifica a posição em X
    //A posição inicial do Thor deve ser atualizada para a nova posição    
    if($initialTX > $lightX){
        $initialTX--;
        $direcao .= "W";
    }
    else if ($initialTX < $lightX){
        $initialTX++;
        $direcao .= "E";
    }

    echo("{$direcao}\n");
}
?>
