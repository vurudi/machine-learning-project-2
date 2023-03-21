import random
import math

def generate_flow_network(n):
    capacity_range = range(int(math.sqrt(n)))  # range of capacities for each node

    # Generate capacities for source node (node 0)
    source_capacities = [random.choice(capacity_range) for _ in range(n+2)]

    # Generate capacities for sink node (node n+1)
    sink_capacities = [random.choice(capacity_range) for _ in range(n+2)]

    # Generate capacities for intermediate nodes (nodes 1 to n)
    intermediate_capacities = [[random.choice(capacity_range) for _ in range(n+2)] for _ in range(n)]

    # Return the generated capacities as a dictionary
    return {
        "source_capacities": source_capacities,
        "sink_capacities": sink_capacities,
        "intermediate_capacities": intermediate_capacities
    }

if __name__ == "__main__":
    print("Flow Networks started...")
    n = input("\nEnter a positive number of nodes in the flow network: ")
    while not n.isdigit():
        n = input("\nPlease enter positive number for the number of nodes: ")
    n = int(n)

    capacities = generate_flow_network(n)

    print("Source capacities:", capacities["source_capacities"])
    print("Sink capacities:", capacities["sink_capacities"])
    for i in range(n):
        print(f"Node {i+1} capacities:", capacities["intermediate_capacities"][i])
