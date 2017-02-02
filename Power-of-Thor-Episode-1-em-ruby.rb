STDOUT.sync = true # DO NOT REMOVE
# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
@light_x, @light_y, @initial_tx, @initial_ty = gets.split(" ").collect {|x| x.to_i}

# game loop
loop do
    remaining_turns = gets.to_i # The remaining amount of turns Thor can move. Do not remove this line.
    
    direction = ""
    
    # Verifica o eixo Y
    if @initial_ty > @light_y
        @initial_ty -= 1
        direction += "N"
    elsif @initial_ty < @light_y
        @initial_ty += 1
        direction += "S"
    end
    
    # Verifica o eixo X
    if @initial_tx > @light_x
        @initial_tx -= 1
        direction += "W"
    elsif @initial_tx < @light_x
        @initial_tx += 1
        direction += "E"
    end

    # A direcao e decida levando em conta os dois eixos X Y
    puts direction
end
