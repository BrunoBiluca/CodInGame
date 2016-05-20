<?php
fscanf(STDIN, "%d",
    $n // the number of temperatures to analyse
);
$temps = stream_get_line(STDIN, 256 + 1, "\n"); // the n temperatures expressed as integers ranging from -273 to 5526

$temps = explode(' ', $temps);          //Separa as temperatura em um array
$maisProxZero = ($n > 0 ? 5527 : 0);    //Verificação quando não existem valores de temperaturas

for($i = 0; $i < $n; $i++){
    if(abs($temps[$i]) < abs($maisProxZero)){   //Verifica a temperatura mais próxima de zero
        $maisProxZero = $temps[$i];
    }
    elseif(abs($temps[$i]) == abs($maisProxZero)){  
        if($maisProxZero < $temps[$i]){  //Temperaturas com valor absoluto iguais, preferência temp positiva
            $maisProxZero = $temps[$i];
        }
    }    
}

echo("{$maisProxZero}\n");
?>
