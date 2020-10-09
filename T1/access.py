import sys
import random as rn
import commons as comm


def read_line(file, pos):
    f = open(file, 'r')
    f.seek(pos*10,0)
    buffer = int(f.read(10))
    f.close()
    return buffer


def read_block(file, pos):
    f = open(file,'r')
    f.seek(pos*10,0)
    buffer = str(f.read(comm.B))
    buffer = list(filter(None, buffer.split('\n')))
    buffer = list(map(int, buffer))
    f.close()
    return buffer
