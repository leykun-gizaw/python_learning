"""Module defines a graph class"""

from ..LinkedList.SLList import SLList

class Graph:
    def __init__(self, vertices: int) -> None:
        # Total number of vertices
        self.vertices = vertices
        # List of Linked lists to store vertices
        self.array = []

        for _ in range(vertices):
            self.array.append(SLList())

    def print_graph(self) -> None:
        """Prints the graph"""

        print(">> Adjacency List of Directed Graph <<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            print(self.array[i])
        pass

    def add_edge(self, source: int, destination: int) -> None:
        """Add an edge to a source vertex in our graph

        Args:
            source (int): Source index
            destination (int): Destination index
        """
        if source < self.vertices and destination < self.vertices:
            src: SLList = self.array[source]
            src.insert_at_head(destination)


if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 2)
    g.add_edge(0, 1)
    g.add_edge(1, 3)
    g.add_edge(2, 3)

    g.print_graph()

    print(g.array[1].get_head().data)
