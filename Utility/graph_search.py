def bfs(node):
    queue = [node]
    while len(queue) > 0:
        cur = queue.pop(0)
        cur.visited = True
        # do something
        for child in cur.children:
            if child.visited is False:
                queue.append(child)


