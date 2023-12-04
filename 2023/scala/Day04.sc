import scala.io.Source
import scala.util.Using

case class Card(id: Int, matches: Int) {
  lazy val worth = 1 << (matches - 1)
  lazy val next = (id + 1 to id + matches)
  lazy val count: Int = next.map(cards(_).count).sum + 1
}

def extract(s: String): Set[Int] =
  raw"\d+".r.findAllIn(s).map(_.toInt).toSet

def parse(line: String): Card = line match {
  case s"Card $id: $winners | $deck" =>
    Card(id.trim.toInt, (extract(winners) & extract(deck)).size)
}

val cards: Map[Int, Card] =
  Using.resource(Source.fromFile("../inputs/04.txt"))(
    _.getLines().map(parse).map(c => (c.id, c)).toMap
  )

val part1 = cards.values.map(_.worth).sum
val part2 = cards.values.map(_.count).sum

println(s"Part 1: $part1")
println(s"Part 2: $part2")
