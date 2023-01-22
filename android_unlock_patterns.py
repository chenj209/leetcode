# https://leetcode.com/problems/android-unlock-patterns/
# 2020.12.24, medium
import math
DEBUG = 0
class Node:
    def __init__(self, id):
        self.id = id
        self.children = []
    def __str__(self):
        return f"Node {self.id}"

def bfs(nodes, sid, m, n):
    queue = [(nodes[sid], 1, [])]
    count = 0
    # counts = [0,0,0]
    cur_l = 1
    paths = []
    if DEBUG == 1:
        print(f"Starting from {sid}")
    while len(queue) > 0 and cur_l <= n:
        cur, cur_l, parents = queue.pop(0)
        if m <= cur_l <= n:
            count += 1
            if DEBUG:
                if len(parents) == 0:
                    paths.append(str(cur.id))
                else:
                    chain = f"{parents[0]}"
                    for p in parents[1:]:
                        chain += f"{p}"
                    chain += f"{cur.id}"
                    paths.append(chain)
        new_parents = parents + [cur.id]
        if cur_l < n:
            for child in cur.children:
                # if isinstance(child, list):
                #     if child[0].id in parents:
                #         queue.append((child[1].id, cur_l + 1, new_parents))
                # else:
                # move = False
                # if new_parents == [5, 2, 7]:
                #     print("break")
                if child.id not in parents:
                    queue.append((child, cur_l + 1, new_parents))
                    # move = True
                    # if new_parents == [5, 2, 7] and queue[-1][0].id == 9:
                    #     print("break 2")
                else:
                    next_neig = child.id + (child.id - cur.id)
                    if 1 <= next_neig <= 9 and next_neig not in parents:
                        if (next_neig + cur.id == 10) or (next_neig-1) % 3 == (cur.id-1) % 3 or (next_neig-1) // 3 == (cur.id-1) // 3:
                            queue.append((nodes[next_neig], cur_l + 1, new_parents))
                        # move = True
                        # if new_parents == [5, 2, 7] and queue[-1][0].id == 9:
                        #     print("break 2")
                # sanity check here
                # if DEBUG == 2 and move:
                #     valid = 0
                #     case = -1
                #     col_last = (cur.id-1) % 3 + 1
                #     col_next = (queue[-1][0].id-1) % 3 + 1
                #     row_last = math.ceil(cur.id / 3)
                #     row_next = math.ceil(queue[-1][0].id / 3)
                #     if (col_last == col_next and abs(cur.id - queue[-1][0].id) == 3) \
                #         or (row_last == row_next and abs(cur.id - queue[-1][0].id) == 1) \
                #         or (abs(col_last - col_next) + abs(row_last - row_next) == 3):
                #         case = 1
                #         counts[0] += 1
                #         if (cur.id + queue[-1][0].id) % 2 == 1:
                #             valid = True
                #     elif col_last == col_next or row_last == row_next or (abs(col_last - col_next) == 2 and abs(row_last - row_next) == 2):
                #         mid = (cur.id + queue[-1][0].id) / 2
                #         case = 2
                #         if mid in new_parents:
                #             valid = True
                #             counts[1] += 1
                #     elif (abs(col_last - col_next) == 1 and abs(row_last - row_next) == 1):
                #         case = 3
                #         counts[2] += 1
                #         valid = True
                #     if not valid:
                #         print(f"Invalid move, case {case}, {[cur.id, queue[-1][0].id, col_last, col_next, row_last, row_next]}: {new_parents} -> {queue[-1][0].id}")
    return count, paths

class Solution:
    def __init__(self):
        self.paths = []
    def numberOfPatterns(self, m: int, n: int) -> int:
        # construct a graph for all points
        nodes = {i:Node(i) for i in range(1, 10)}
        for i in [1,3,7,9]:
            for j in [2,4,5,6,8]:
                nodes[i].children.append(nodes[j])
            # for j in [1,3,7,9]:
            #     if i != j:
            #         nodes[i].children.append([nodes[(i+j)/2], nodes[j]])
        for i in [2,4,6,8]:
            for j in range(1,10):
                if i != j:
                    if i+j != 10:
                        nodes[i].children.append(nodes[j])
                    # else:
                    #     nodes[i].children.append([nodes[(i+j)/2], nodes[j]])
        nodes[5].children = [nodes[i] for i in [1,2,3,4,6,7,8,9]]
        if DEBUG:
            for i in range(1, 10):
                print(f"Node {i}: {[str(node) for node in nodes[i].children]}")
        all_paths = []
        count = 0
        for i in range(1,10):
            c, paths = bfs(nodes, i, m, n)
            count += c
            all_paths += paths
        if DEBUG:
            all_paths.sort()
            with open('output.txt', 'w') as f:
                for path in all_paths:
                    f.write(path)
                    f.write('\n')
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfPatterns(4,9))
