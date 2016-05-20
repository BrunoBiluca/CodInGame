<?php
fscanf(STDIN, "%d",
    $road // the length of the road before the gap.
);
fscanf(STDIN, "%d",
    $gap // the length of the gap.
);
fscanf(STDIN, "%d",
    $platform // the length of the landing platform.
);

// game loop
while (TRUE){
    fscanf(STDIN, "%d",
        $speed // the motorbike's speed.
    );
    fscanf(STDIN, "%d",
        $coordX // the position on the road of the motorbike.
    );

    $action = "";   //Ação da motocicleta neste turno

    //Se a moto está na estrada
    if($coordX < $road-1){
        //Velocidade necessário para pular o buraco é $gap+1
        if($speed < $gap+1){ 
            $action = "SPEED";
        }elseif($speed > $gap+1){
            $action = "SLOW";
        }else{
            $action = "WAIT";
        }
    }elseif($coordX == $road-1){ //Última posição da estrada
        $action = "JUMP";
    }
    else{ //Moto já pulo, agora é só freiar
        $action = "SLOW";
    }

    // A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
    echo("{$action}\n");
}
?>
