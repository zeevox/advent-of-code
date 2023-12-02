import scala.io.Source
import scala.util.Using

case class Hand(red: Int = 0, green: Int = 0, blue: Int = 0) {
  def +(other: Hand): Hand =
    Hand(red + other.red, green + other.green, blue + other.blue)

  def <=(other: Hand): Boolean =
    red <= other.red && green <= other.green && blue <= other.blue

  def max(other: Hand): Hand =
    Hand(red max other.red, green max other.green, blue max other.blue)

  def power: Int = red * green * blue
}

case class Game(id: Int, hands: Array[Hand])

def parseColor(s: String): Hand = s match {
  case s"$count red"   => Hand(red = count.toInt)
  case s"$count green" => Hand(green = count.toInt)
  case s"$count blue"  => Hand(blue = count.toInt)
}

def parseHand(s: String): Hand =
  s.split(", ").map(parseColor).reduce(_ + _)

def parseGame(line: String): Game = line match {
  case s"Game $id: $hands" => Game(id.toInt, hands.split("; ").map(parseHand))
}

val games: Seq[Game] = Using.resource(Source.fromFile("../inputs/02.txt")) {
  _.getLines().map(parseGame).toSeq
}

println(
  games
    .filter(_.hands.forall(_ <= Hand(12, 13, 14)))
    .map(_.id)
    .sum
)

println(
  games
    .map(_.hands.reduce(_ max _).power)
    .sum
)
