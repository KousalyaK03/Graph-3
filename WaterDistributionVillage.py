class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        """
        Approach:
        - Use Kruskal's Algorithm with Union-Find to build a Minimum Spanning Tree (MST).
        - Consider each house as a node and each pipe as an edge.
        - Introduce a virtual node (0) that connects to every house with the cost of digging a well.
        - Sort all edges (pipes + wells) by cost and use Union-Find to connect components.

        Time Complexity: O((n + m) log (n + m)), where n is the number of houses, and m is the number of pipes.
        Space Complexity: O(n + m), for storing the graph and DSU.
        """

        # Union-Find (Disjoint Set) with path compression and union by rank
        parent = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]

        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            if root1 == root2:
                return False  # They are already in the same set
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            return True

        # Step 1: Convert wells into "virtual edges" from node 0 to all houses
        edges = [(cost, 0, i + 1) for i, cost in enumerate(wells)]

        # Step 2: Add pipes as normal edges
        for house1, house2, cost in pipes:
            edges.append((cost, house1, house2))

        # Step 3: Sort edges by cost (Kruskal's algorithm requirement)
        edges.sort()

        # Step 4: Process edges using Union-Find
        total_cost = 0
        connections = 0

        for cost, house1, house2 in edges:
            if union(house1, house2):  # If we successfully connect two components
                total_cost += cost
                connections += 1
                if connections == n:  # If we connected all n houses, stop early
                    break

        return total_cost
s