import math._
import scala.util._
import scala.io.StdIn._
import scala.collection.mutable.ListBuffer

// TODO: arquitetar a solução para possíveis novas formas de pontuar

object Solution extends App {
    val score = readLine.toInt

    var try_points = 5
    var transformation_kick_points = 2
    var penalty_kick_points = 3
    
    var num_max_score_attempts = score / penalty_kick_points
    
    val score_combinations: ListBuffer[(Int, Int, Int)] = ListBuffer.empty
    for(try_p <- 0 to num_max_score_attempts){
        var try_attemp = try_p * try_points
        
        for(trans_p <- 0 to num_max_score_attempts){
            var transformation_kick_attemp = trans_p * transformation_kick_points
            
            for(penal_p <- 0 to num_max_score_attempts){
                var penalty_kick_attemp = penal_p * penalty_kick_points

                var combination_attemp = try_attemp + transformation_kick_attemp + penalty_kick_attemp
                if(score - combination_attemp == 0){
                    score_combinations.append((try_p, trans_p, penal_p))
                }
            }
        }
    }

    val valid_scores = score_combinations
                            .filter(x => x._2 <= x._1)
                            .sortBy(c => (c._1, c._2, c._3))
    
    valid_scores.map { c =>
        println(c.productIterator.mkString(" "))
    }
}
