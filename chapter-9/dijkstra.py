from queue import Queue


def dijkstra(graph, start, stop, table, queue):
    if table == {}:
        table[start] = ["/", 0]
        queue.put(start)
    if queue.empty() == True:
        path = stop
        end = stop
        while True:
            end, _ = table[end]
            _, cost = table[stop]
            path = end + path 
            if end == start:
                return cost, path
    letter = queue.get()
    out_neighbours = graph[letter]
    _, accumulated_cost = table[letter]
    for out_letter, out_cost in out_neighbours:
        candidate_cost = accumulated_cost + out_cost
        try:
            _, current_cost = table[out_letter]
            if candidate_cost < current_cost:
                table[out_letter] = (letter, candidate_cost)
                if out_letter != stop:
                    queue.put(out_letter)
        except KeyError:
            table[out_letter] = (letter, candidate_cost)
            if out_letter != stop:
                queue.put(out_letter)
    return dijkstra(graph, start, stop, table, queue)

def main():
    graph = {}
    graph["A"] = [("B", 3), ("C", 10), ("D", 7)]
    graph["B"] = [("E", 17), ("C", 2)]
    graph["C"] = [("F", 4)]
    graph["D"] = [("F", 8)]
    graph["E"] = [("G", 2)]
    graph["F"] = [("E", 3), ("G", 6)]
    start = "D"
    stop = "G"
    table = {}
    queue = Queue(0)
    stop = "G"
    cost, path = dijkstra(graph, start, stop, table, queue)
    print(f"To get from {start} to {stop} it costs {cost} if you follow this path: {path}")


if __name__ == "__main__":
    main()
