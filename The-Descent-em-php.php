<?php
// game loop
while (TRUE){
    $maisAlta = 0;      //Armazena a montanha mais alta
    $pos = 0;           //Armazena a posição da montanha mais alta
    for ($i = 0; $i < 8; $i++){
        fscanf(STDIN, "%d",
            $mountainH // represents the height of one mountain, from 9 to 0.
        );
        if($mountainH > $maisAlta): //Descobre a montanha mais alta neste turno
            $pos = $i;
            $maisAlta = $mountainH;
        endif;
    }

    //Atira na montanha mais alta encontrada, perigo iminente
    echo("{$pos}\n"); // The number of the mountain to fire on.
}
?>
