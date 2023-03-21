import time
from random import randint

import matplotlib.pyplot as plt
import networkx as nx


def generate_flow_network(n):
    print("generate_flow_network")
    G = nx.DiGraph()
    source = 0
    sink = n + 1
    G.add_node(source)
    G.add_node(sink)
    for i in range(1, n + 1):
        capacity = randint(1, 10)
        G.add_edge(source, i, capacity=capacity)
        G.add_edge(i, sink, capacity=capacity)
        for j in range(i + 1, n + 1):
            capacity = randint(1, 10)
            G.add_edge(i, j, capacity=capacity)
            G.add_edge(j, i, capacity=capacity)
    return G


def measure_running_time(G, algorithm):
    start_time = time.time()
    if algorithm == "ford-fulkerson":
        max_flow = nx.maximum_flow(G, 0, len(G) - 1, flow_func=nx.algorithms.flow.edmonds_karp)
    elif algorithm == "edmond-karp":
        max_flow = nx.algorithms.flow.edmonds_karp(G, 0, len(G) - 1)
    end_time = time.time()
    running_time = end_time - start_time
    return running_time


def compare_running_times():
    n_values = range(1, 21)
    ford_fulkerson_times = []
    edmond_karp_times = []
    for n in n_values:
        G = generate_flow_network(n)
        ford_fulkerson_time = measure_running_time(G, "ford-fulkerson")
        edmond_karp_time = measure_running_time(G, "edmond-karp")
        ford_fulkerson_times.append(ford_fulkerson_time)
        edmond_karp_times.append(edmond_karp_time)
    print("starting the plotting..")
    plt.plot(n_values, ford_fulkerson_times, label="Ford-Fulkerson")
    plt.plot(n_values, edmond_karp_times, label="Edmond-Karp")
    plt.xlabel("n")
    plt.ylabel("Running time (s)")
    plt.legend()
    plt.title(" A graph comparing complexity of the values of Ford-Fulkerson "
              "and Edmond-Karp n being the x a-xis")
    plt.show()



if __name__ == '__main__':
    print("measure_running_time")
    print("compare_running_times of the two ")
    compare_running_times()
