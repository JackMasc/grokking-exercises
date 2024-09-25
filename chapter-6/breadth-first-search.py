from queue import Queue


def breadth_first(graph, start, wanted):
    doublecheck = {key: False for key in graph.keys()}
    queue = Queue(0)
    queue.put(start)
    doublecheck[start] = True
    while True:
        if queue.empty():
            return "NOT FOUND"
        node = queue.get()
        if node == wanted:
            return node
        for nth_grade in graph[node]:
            if doublecheck[nth_grade] == False:
                queue.put(nth_grade)
                doublecheck[nth_grade] = True



def main():

    # Network implementation
    graph = {}
    graph["A"] = ["B", "C", "D"]
    graph["B"] = ["A", "D", "E"]
    graph["C"] = ["E"]
    graph["D"] = []
    graph["E"] = ["D", "F", "G", "H"]
    graph["F"] = []
    graph["G"] = ["I", "L"]
    graph["H"] = ["L"]
    graph["I"] = ["M"]
    graph["L"] = []
    graph["M"] = []

    # Running the algorithm on the network
    start = "A"
    wanted = input("Please enter the capital letter to look for in the network: ")
    letter = breadth_first(graph, start, wanted)
    print("The letter " + letter + " was found")


if __name__ == "__main__":
    main()
