#!/usr/bin/env python3
import sys

lines = open(sys.argv[1]).readlines()
f = open(sys.argv[1] + ".mw", "w")

#indices = [i for i, x in enumerate(lines) if x == "\n"]

n = lines.index("\n")

a = (lines[0:n])
b = (lines[n+1:n*2+1])
c = (lines[2*n+2:n*3+2])

print("{|", file=f)
for pt, en, ph in zip(a, b, c):
  print("|-", file=f)
  if pt[0] == "#":
    print("! {0} !! {1} !! ''{2}''".format(pt[1:].strip(), en[1:].strip(), ph[1:].strip()), file=f)
  else:
    print("| {0} || {1} || ''{2}''".format(pt.strip(), en.strip(), ph.strip()), file=f)

print("|}", file=f)
