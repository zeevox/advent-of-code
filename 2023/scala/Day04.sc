import scala.io.Source
import scala.util.Using

case class Card(id: Int, winners: Set[Int], deck: Set[Int]) {
  def worth = math.pow(2, matches - 1).toInt
  def matches = winners.intersect(deck).size
  def next = (id + 1 to id + matches)
  def count: Int = 1 + next.map(id => cards(id).count).sum
}

def extract(s: String): Set[Int] =
  raw"\d+".r.findAllIn(s).map(_.toInt).toSet

def parse(line: String): Card = line match {
  case s"Card $id: $winners | $deck" =>
    Card(id.trim.toInt, extract(winners), extract(deck))
}

val cards: Map[Int, Card] =
  Using.resource(Source.fromFile("../inputs/04.txt"))(
    _.getLines().map(parse).map(c => (c.id, c)).toMap
  )

val part1 = cards.values.map(_.worth).sum
val part2 = cards.values.map(_.count).sum

println(s"Part 1: $part1")
println(s"Part 2: $part2")
