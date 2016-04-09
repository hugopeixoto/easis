#!/usr/bin/env python3
import sys

lines = open(sys.argv[1]).readlines()
f = open(sys.argv[1] + ".mw", "w")

indices = [i for i, x in enumerate(lines) if x == "\n"]

cols = len(indices) + 1

n = lines.index("\n")

translations = zip(*[ lines[i*(n+1):i*(n+1)+n] for i in range(0, cols)])

print("{| style=\"width: 100%\"", file=f)
for tr in translations:
  tr = list(tr)
  print("|-", file=f)


  if tr[0][0] == '#':
    for t in tr:
      print("! {0}".format(t[1:].strip()), file=f)
  else:
    tr[-1] = "'''{0}'''".format(tr[-1].strip())
    for t in tr:
      print("| {0}".format(t.strip()), file=f)

print("|}", file=f)
