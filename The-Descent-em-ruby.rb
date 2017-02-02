STDOUT.sync = true # DO NOT REMOVE
loop do
    # Altura da maior montanha
    higher_mountain = 0
    # Posicao da maior montanha
    higher_mountain_pos = 0
    8.times do |pos|
        mountain_h = gets.to_i
        if higher_mountain < mountain_h
            higher_mountain = mountain_h
            higher_mountain_pos = pos
        end
    end
    
    puts higher_mountain_pos
end
