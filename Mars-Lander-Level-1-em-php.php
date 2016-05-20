<?php
/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

fscanf(STDIN, "%d",
    $surfaceN // the number of points used to draw the surface of Mars.
);
for ($i = 0; $i < $surfaceN; $i++){
    fscanf(STDIN, "%d %d",
        $landX, // X coordinate of a surface point. (0 to 6999)
        $landY // Y coordinate of a surface point.
    );
}

// game loop
while (TRUE){
    fscanf(STDIN, "%d %d %d %d %d %d %d",
        $X,
        $Y,
        $hSpeed, // the horizontal speed (in m/s), can be negative.
        $vSpeed, // the vertical speed (in m/s), can be negative.
        $fuel, // the quantity of remaining fuel in liters.
        $rotate, // the rotation angle in degrees (-90 to 90).
        $power // the thrust power (0 to 4).
    );

    //Se a velocidade for maior que o permitido
    if($vSpeed < -39){
        $power++;        
    }else{
        $power--;
    }

    //Normalização do $power
    $power = ($power < 0 ? 0 : $power);
    $power = ($power > 4 ? 4 : $power);

    // 2 integers: rotate power.
    echo("0 {$power}\n");
}
?>
