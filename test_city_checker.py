import unittest
from collections import deque

def are_connected(graph, city1, city2):
    if city1 not in graph or city2 not in graph:
        return False
    visited = set()
    queue = deque([city1])
    while queue:
        current = queue.popleft()
        if current == city2:
            return True
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False
55
class TestCityChecker(unittest.TestCase):

    def setUp(self):
        # Define a small graph with only the 4 cities
        self.graph = {
            "Bengaluru": {"Hyderabad", "Chennai"},
            "Hyderabad": {"Bengaluru"},
            "Chennai": {"Bengaluru"},
            "Nagpur": set()  # No connections
        }

    def test_connected_bengaluru_hyderabad(self):
        self.assertTrue(are_connected(self.graph, "Bengaluru", "Hyderabad"))

    def test_connected_bengaluru_chennai(self):
        self.assertTrue(are_connected(self.graph, "Bengaluru", "Chennai"))

    def test_not_connected_nagpur_hyderabad(self):
        self.assertFalse(are_connected(self.graph, "Nagpur", "Hyderabad"))

    def test_not_connected_nagpur_chennai(self):
        self.assertFalse(are_connected(self.graph, "Nagpur", "Chennai"))

    def test_same_city(self):
        self.assertTrue(are_connected(self.graph, "Hyderabad", "Hyderabad"))

if __name__ == "__main__":
    unittest.main()