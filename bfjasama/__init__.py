import networkx as nx
import itertools
""" Check if cycle is a hamiltoniano cycle in graph"""
def is_hamiltonian_cycle(graph, cycle):
    # Obtener la longitud del ciclo propuesto
  n = len(cycle)
    
    # Verificar que el ciclo contenga TODOS los vértices del grafo
    # graph.order() devuelve el número total de vértices del grafo
  if n != graph.order():
      return False  # No visita todos los vértices
    
    # Verificar que existan aristas entre cada par consecutivo de vértices
    # Itera desde el primer vértice hasta el penúltimo
  for i in range(n - 1):
        # Si NO hay arista entre el vértice actual y el siguiente
      if not graph.has_edge(cycle[i], cycle[i + 1]):
          return False  # El ciclo se rompe, no hay conexión
    
    # Verificar la última arista: del último vértice al primero
    # Esto "cierra" el ciclo
  if not graph.has_edge(cycle[n - 1], cycle[0]):
      return False  # No se puede regresar al inicio
    
    # Si todas las verificaciones anteriores fueron exitosas:
    # - El ciclo tiene la longitud correcta (todos los vértices)
    # - Todas las aristas consecutivas existen
    # - La arista que cierra el ciclo existe
    # Entonces es un ciclo Hamiltoniano válido
  return True
def is_hamiltonian(graph):
  vertices = list(graph.nodes())
  if len(vertices) < 4:
    return False
  perms = itertools.permutations(vertices)
  for perm in perms:
    if is_hamiltonian_cycle(graph, perm):
      return perm
  return False

################################################
def is_proper_coloring(graph, coloring):
  for edge in graph.edges():
    if coloring[edge[0]]==coloring[edge[1]]:
      return False
  return True

def is_3_colorable(graph):
  n = graph.order()
  colorings = product([0,1,2], repeat = n)
  for coloring in colorings:
    if is_proper_coloring(graph, coloring):
      return coloring
  return False
######################################################################################
import itertools

def sum_of_values(values, keys):
    sum = 0
    n = len(values)
    for i in range(n):
        sum+=values[i]*keys[i]
    return sum

def knapsack_problem(profits, weights, capacity, goal):
    n = len(profits)
    sequences = itertools.product([0, 1], repeat = n)
    for sequence in sequences:
        if sum_of_values(weights, sequence) <= capacity: 
            if sum_of_values(profits, sequence)>=goal:
                return sequence
    return False