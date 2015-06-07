from copy import deepcopy
import numpy


def get_path(pre_matrix, origin, dest):
  """
  Reconstruct shortest path from origin to destination using the predecessor matrix passed as input
  """
  path_list = [origin]

  while 1:
    predecessor = pre_matrix[origin - 1][dest - 1] + 1
    if predecessor == origin:
      path_list.append(dest)
      return map(str, path_list)

    path_list.append(int(predecessor))

    origin = predecessor

def generate_report(dist_matrix, pre_matrix):
  """
  Print well-formatted report
  """
  print "-" * 60
  node_count = len(dist_matrix)

  for from_node, i in enumerate(range(0, node_count), 1):
    for to_node, j in enumerate(range(0, node_count), 1):

      if numpy.isinf(dist_matrix[i][j]):
        continue

      print "From : %s To : %s" % (from_node, to_node)
      print "Path : %s" % ' '.join(get_path(pre_matrix, from_node, to_node))
      print "Distance : %s" % int(dist_matrix[i][j])
      print "\n"

def generate_predecessors_matrix(input_matrix):
  """
  Return a matrix of predecessors
  """
  node_count = len(input_matrix)

  pre_matrix = numpy.zeros( shape = (node_count, node_count))
  #Initialize predecessor matrix
  for i in range(0, node_count):
    for j in range(0,node_count):
      if not numpy.isinf(input_matrix[i][j]):
        pre_matrix[i][j] = i
      else:
        pre_matrix[i][j] = numpy.inf

  return pre_matrix

def floyd_warshall(input_matrix):
  """
  Execute Floyd Warshall algorithm on matrix passed as input.
  """
  node_count = len(input_matrix)

  dist_matrix = deepcopy(input_matrix) #Matrix storing results
  pre_matrix = generate_predecessors_matrix(input_matrix) #Matrix storing predecessors

  for intermediate in range(0, node_count): #Pick a node that will be tested as intermediary position
    for origin in range(0, node_count): #pick origin
      for dest in range(0, node_count): #and destination

        alternative_dist = dist_matrix[origin][intermediate] + dist_matrix[intermediate][dest]

        if alternative_dist < dist_matrix[origin][dest]:
          #check for absorbing path
          if origin == dest:
            print "Negative cycle at : %s" % (origin + 1)
            return

          dist_matrix[origin][dest] = alternative_dist #store shorter path in distance_matrix
          predecessor = pre_matrix[origin][intermediate] #get predecessor from origin to intermediate
          #Test if predecessor is the starting node.
          #This test avoid to have an overriden node (e.g : 4 ==> 1 ==> 3 instead of 4 ==> 2 ==> 1 ==> 3)
          pre_matrix[origin][dest] = predecessor if predecessor != origin else intermediate


  generate_report(dist_matrix, pre_matrix)
