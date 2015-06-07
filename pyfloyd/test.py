#! /usr/bin/python
#-*- coding=utf-8 -*-
from floyd_warshall import floyd_warshall
import sys, pprint, numpy


def import_datas_and_execute_algorithm(test_path):
  #We'll assume that the input file is well formatted
  with open(test_path) as test_file:
    #retrieve nodes and arcs amount
    node_count = int(test_file.readline())
    arc_count = int(test_file.readline())

    #initialize the input matrix for floyd warshall algorithm
    input_matrix = numpy.full((node_count, node_count), numpy.inf)

    for line in test_file.readlines():
      #clean input
      origin, dest, weight = map(int, line.strip().split(' '))

      input_matrix[origin - 1][origin - 1] = 0 #We'll assume that the weight from a node to itself is 0
      input_matrix[origin - 1][dest - 1] = weight

    print "Input: "
    pprint.pprint(input_matrix)

    floyd_warshall(input_matrix)


if  __name__ == "__main__":
  if len(sys.argv) < 2:
    print "Usage: ./test.py <path_to_test_file>"
  else:
    import_datas_and_execute_algorithm(sys.argv[1])
