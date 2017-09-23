var L = parseInt(readline());
var H = parseInt(readline());
var T = readline();

// Cria o alfabeto utilizado pelo ASC
var alfabetoAux = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?";
var alfabeto = {};

// Inicializa as strings do alfabeto
for(var j = 0; j < alfabetoAux.length; j++){
    alfabeto[alfabetoAux[j]] = '';
}

// Lê as strings das letras para o alfabeto
for (var i = 0; i < H; i++) {
    var ROW = readline();
    for(var j = 0; j < alfabetoAux.length; j++){
        alfabeto[alfabetoAux[j]] += ROW.substring(j * L, j * L + L);
    }
}

// Monta a string ASC de resposta
var str = "";
for (var i = 0; i < H; i++) {
    for(var j = 0; j < T.length; j++){
        letra = T[j].toUpperCase();
        // Se a letra não existe deve ser respondida como uma ?
        if(alfabetoAux.indexOf(letra) === -1){
            str += alfabeto['?'].substring(i * L, i * L + L);
        }    
        else{
            str += alfabeto[letra].substring(i * L, i * L + L);
        }
    }
    str += `\n`;
}

print(str);
