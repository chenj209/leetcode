# Definition for a binary tree node.  class TreeNode:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        queue = [(root, [])]
        while len(queue) != 0:
            current_node, path = queue.pop()
            for node in path:
                parent_node, side = path
                if (node.val - parent_node.val) * side < 0:
                    old_node_val = node.val
                    node.val = parent_node.val
                    parent_node.val = old_node_val
                    break
                else:
                    left_node = current_node.left
                    left_path = path + [(left_node, 1)]
                    queue.append((left_node, left_path))
                    right_node = current_node.right
                    right_path = path + [(right_node, -1)]
                    queue.append((right_node, right_path))

def main(nodes):
    sol = Solution()
    root = init_tree(nodes)
    sol.recoverTree(root)
    print(root)

if __name__ == "__main__":
    main([1, 3, None, None, 2])
    main([3,1,4,None, None, 2])
