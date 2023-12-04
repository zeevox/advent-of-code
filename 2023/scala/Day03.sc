import scala.io.Source
import scala.util.Using

case class Part(row: Int, colStart: Int, colEnd: Int, value: Int)
case class Symbol(row: Int, col: Int, value: Char)
type Engine = Seq[Part]

val input: Seq[String] = Using.resource(Source.fromFile("../inputs/03.txt")) {
  _.getLines().toSeq
}

def parseEngine(lines: Seq[String]) =
  lines.zipWithIndex.flatMap { (line, row) =>
    {
      val numberRegex = raw"\d+".r
      numberRegex
        .findAllMatchIn(line)
        .map { m =>
          Part(row, m.start, m.end - 1, m.matched.toInt)
        }
        .toSeq
    }
  }

val engine = parseEngine(input)

def adjacentSymbols(part: Part): Seq[Symbol] = part match {
  case Part(row, colStart, colEnd, _) =>
    for {
      r <- row - 1 to row + 1
      c <- colStart - 1 to colEnd + 1
      if !(r == row && c >= colStart && c <= colEnd)
      if r >= 0 && r < input.length
      if c >= 0 && c < input(r).length
      if input(r)(c) != '.'
    } yield Symbol(r, c, input(r)(c))
}

// Part 1
println(engine.filter(adjacentSymbols(_).nonEmpty).map(_.value).sum)

// Part 2
println(
  engine
    .flatMap(part =>
      adjacentSymbols(part)
        .map(symbol => (symbol, part))
    )
    .groupMap(_._1)(_._2)
    .filter((s, ps) => s.value == '*' && ps.size == 2)
    .map(_._2.map(_.value).product)
    .sum
)
