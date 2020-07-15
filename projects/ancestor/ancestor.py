class Queue():
    def __init__(self):
        self.queue = []
    def append(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def earliest_ancestor(ancestors, starting_node):
    # create a dictionary with children as keys
    # parents as values in a list
    parents_by_child = {}
    for parent, child in ancestors:
        if child in parents_by_child:
            parents_by_child[child].append(parent)
        else:
            parents_by_child[child] = [parent]

    # Early exit if the starting node has no parents
    if starting_node not in parents_by_child:
        return -1

    path_queue = Queue()
    last_path = [starting_node]

    path_queue.append(last_path)

    while path_queue.size() > 0:
        last_path = path_queue.dequeue()
        oldest_ancestor = last_path[-1]

        if oldest_ancestor in parents_by_child:
            # make sure lowest id goes in queue last
            parents_by_child[oldest_ancestor] = sorted(parents_by_child[oldest_ancestor],reverse=True)
            for parent in parents_by_child[oldest_ancestor]:
                print(f"parent: {parent}")
                new_path = last_path.copy()
                new_path.append(parent)

                path_queue.append(new_path)
    print(f"last_path: {last_path}")
    return last_path[-1]

if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    result = earliest_ancestor(test_ancestors, 1) # 10
    result = earliest_ancestor(test_ancestors, 2) # -1
    # result = earliest_ancestor(test_ancestors, 3) # 10
    print(f"result: {result}")