import sequtils
import strutils
import strformat

var b, c: int
(b, c) = stdin.readLine.split.map(parseInt)
let d = if ((b * c) mod 2) == 0: "Even" else: "Odd"
echo &"{d}"