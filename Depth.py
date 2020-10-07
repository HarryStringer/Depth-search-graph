def main():
    vertices = ('A','B','C','D','E','F','G','H','I')
    adjList = [['B','C','D'],['A','C','E'],['A','B','D','F','G'],['A','C','G'],['B'],['C','I'],['C','D','H'],['G'],['F']]
    DFSRec(vertices, adjList, vertices[0])

def DFSRec(vertices, adjList, start, visited=False):
    if not visited:
        visited = []
    current_neighbours =[]

    visited.append(start)

    print(start)

    currentNeighbours = adjList[vertices.index(start)]

    for neighbour in currentNeighbours:
        if neighbour not in visited:
            DFSRec(vertices, adjList, neighbour, visited)
    return visited

if __name__ == '__main__':
    main()
