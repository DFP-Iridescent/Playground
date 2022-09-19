#!/usr/bin/env python3
# Make a simple times table
import os, sys
for row in range(0,6):
    if row==0:
        x=sys.stdout.write("%4s" % "|")
    else:
        x=sys.stdout.write("%3d|" % row)
    for col in range(1,6):
        prod = row * col if (row>0) else col
        x=sys.stdout.write("%4d" % prod)
    x=sys.stdout.write("\n")
    if (row==0):
        x=sys.stdout.write("-"*(6*4)+"\n")
