import math._
import scala.util._
import scala.io.StdIn._
import scala.collection.mutable.Map

object Solution extends App {
    val N = readLine.toInt
    val Q = readLine.toInt
    
    val mime_table = Map.empty[String, String]
    for(i <- 0 until N) {
        val ext_mt_input = readLine split " "
        
        mime_table += (ext_mt_input(0).toLowerCase() -> ext_mt_input(1))
    }
    
    for(i <- 0 until Q) {
        var f_name = readLine
        
        var extension_pattern = ".*[.]{1}[a-zA-Z0-9]+$"
        var is_f_name_have_extension = f_name matches extension_pattern
        if(!is_f_name_have_extension){
            println("UNKNOWN")
        }
        else {
            var f_extension = (f_name split "[.]").last
            println(mime_table.getOrElse(f_extension.toLowerCase(), "UNKNOWN"))    
        }
    }
}
