import math._
import scala.util._
import scala.io.StdIn._

// TODO: solução parcial
// Não passou nos testes de performance
// Melhorias:
// - refatorar o código para melhorar a responsabilidade de cada elemento
// - encontrar loops no movimento do robô, assim não é necessário que seja iterado sobre todas as possibilidades

class Circuit(var height: Int, var width: Int){
    height += 2
    width += 2
    private var _map = Array.fill[Tile](height, width)(new Tile('#'))
    private var _robot_position: Tile = _

    def map = _map
    def robot_position = _robot_position
    
    def create_tile(pos_x: Int, pos_y: Int, content: Char): Unit = {
        var tile_pos = (pos_x + 1, pos_y + 1)
        var tile = _map(tile_pos._1)(tile_pos._2)
        
        tile.content_(content)
        tile.name_(s"${pos_y} ${pos_x}")
        tile.up_(_map(tile_pos._1 - 1)(tile_pos._2))
        tile.down_(_map(tile_pos._1 + 1)(tile_pos._2))
        tile.left_(_map(tile_pos._1)(tile_pos._2 - 1))
        tile.right_(_map(tile_pos._1)(tile_pos._2 + 1))
        
        if(tile.content == 'O'){
            _robot_position = tile
        }
    }
    
    def move_robot(operations: Long): Unit = {
        var num_operations = operations
        var direction = "up"
        while(num_operations > 0){
            if(direction == "up"){
                if(update_robot_position(_robot_position.up)){direction = "up"}
                else if(update_robot_position(_robot_position.right)){direction = "right"}
                else if(update_robot_position(_robot_position.down)){direction = "down"}
                else if(update_robot_position(_robot_position.left)){direction = "left"}
            }
            else if(direction == "right"){
                if(update_robot_position(_robot_position.right)){direction = "right"}
                else if(update_robot_position(_robot_position.down)){direction = "down"}
                else if(update_robot_position(_robot_position.left)){direction = "left"}
                else if(update_robot_position(_robot_position.up)){direction = "up"}
            }
            else if(direction == "down"){
                if(update_robot_position(_robot_position.down)){direction = "down"}
                else if(update_robot_position(_robot_position.left)){direction = "left"}
                else if(update_robot_position(_robot_position.up)){direction = "up"}
                else if(update_robot_position(_robot_position.right)){direction = "right"}
            }
            else if(direction == "left"){
                if(update_robot_position(_robot_position.left)){direction = "left"}
                else if(update_robot_position(_robot_position.up)){direction = "up"}
                else if(update_robot_position(_robot_position.right)){direction = "right"}
                else if(update_robot_position(_robot_position.down)){direction = "down"}
            }

            num_operations -= 1
        }
        
        println(_robot_position.name)
    }
    
    def update_robot_position(tile: Tile): Boolean = {
        if(tile.content != '.') return false
        
        _robot_position.content_('.')
        tile.content_('O')
        _robot_position = tile
        
        return true
    }
    
    def print_map(): Unit = {
        for(x <- 0 until height){
            for(y <- 0 until width){
                print(_map(x)(y).content)
            }
            println("")
        }
    }
}

class Tile(private var _content: Char = '.'){
    private var _name: String = _
    private var _up: Tile = _
    private var _down: Tile = _
    private var _left: Tile = _
    private var _right: Tile = _
    
    def name = _name
    def name_(new_name: String): Unit = {
        _name = new_name
    }
    
    def content = _content
    def content_(new_content: Char): Unit = {
        _content = new_content
    }
    
    def up = _up
    def up_(tile: Tile): Unit = {
        _up = tile
    }

    def down = _down
    def down_(tile: Tile): Unit = {
        _down = tile
    }

    def left = _left
    def left_(tile: Tile): Unit = {
        _left = tile
    }

    def right = _right
    def right_(tile: Tile): Unit = {
        _right = tile
    }
}

object Solution extends App {
    val Array(w, h) = (readLine split " ").map (_.toInt)
    val robot_operations = readLine.toLong

    val circuit = new Circuit(h, w)
    
    for(i <- 0 until h) {
        val line = readLine
        
        for(j <- 0 until w){
            circuit.create_tile(i, j, line(j))
        }
    }
    
    circuit.move_robot(robot_operations)
    
    //circuit.print_map()
}
