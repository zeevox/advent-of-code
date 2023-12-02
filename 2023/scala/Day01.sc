import scala.io.Source

/** Map from digit text to digit number. */
val digitMap: Map[String, String] = Map(
  "zero" -> "0",
  "one" -> "1",
  "two" -> "2",
  "three" -> "3",
  "four" -> "4",
  "five" -> "5",
  "six" -> "6",
  "seven" -> "7",
  "eight" -> "8",
  "nine" -> "9"
)

/** Set of all digits, both as text and as numbers. */
val digits: Set[String] = digitMap.keySet ++ digitMap.values

/** Return the integer given a digit. */
def getDigit(digit: String): Int = digitMap.getOrElse(digit, digit).toInt

/** Get the number encoded by the line. */
def getCalibrationValue(encodedLine: String): Int = {
  val filtered: String = encodedLine.filter(_.isDigit)
  return filtered.head.asDigit * 10 + filtered.last.asDigit
}

/** Get the number encoded by line using updated rules. */
def getCalibrationValue2(encodedLine: String): Int = {
  val firstDigit: String =
    digits.filter(encodedLine.contains(_)).minBy(encodedLine.indexOf(_))
  val lastDigit: String = digits.maxBy(encodedLine.lastIndexOf(_))
  return getDigit(firstDigit) * 10 + getDigit(lastDigit)
}

val lines: List[String] = Source.fromFile("../inputs/01.txt").getLines().toList
println(lines.map(getCalibrationValue).sum)
println(lines.map(getCalibrationValue2).sum)
