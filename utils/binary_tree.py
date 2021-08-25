DEBUG = 1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree_helper(root, level):
    if root is None:
        return ""

    tree_str = ""
    if root.right:
        tree_str += print_tree_helper(root.right, level+1)

    level_indent = "    " * level
    tree_str += level_indent + f"->{root.val}\n"

    if root.left:
        tree_str += print_tree_helper(root.left, level+1)

    return tree_str

class BinaryTree:
    def __init__(self, val_lst):
        self.root = TreeNode(val_lst[0])
        build_tree(val_lst, self.root, 0)

    def __init__2(self, val_lst):
        """
        val_lst: [value] where value are sorted in layer order from left to right. Layer i always has 2^i nodes (empty nodes represented using None), except the last layer
        e.g.: [1#root,2,3#layer1, 4,5,6,7#layer2,...]
        """
        self.root = TreeNode(val_lst[0])

        # parse value into list of list, where each inner list represent the nodes in that layer
        l = 1
        layers = []
        while 2**l < len(val_lst):
            layer_st_idx = 2**l-1
            layer_ed_idx = min(2**(l+1)-1,len(val_lst)-1)
            if DEBUG:
                print(f"layer: {l}, start: {layer_st_idx}, end: {layer_ed_idx}")
            cur_layer = val_lst[layer_st_idx:layer_ed_idx]
            layers.append(cur_layer)
            l += 1
        if DEBUG:
            print(f"layers: {layers}")

        prev_layer = [self.root]
        for layer in layers:
            cur_layer = []
            for i, node in enumerate(prev_layer):
                if 2*i < len(layer):
                    node.left = TreeNode(layer[2*i])
                    cur_layer.append(node.left)
                if (2*i+1) < len(layer):
                    node.right = TreeNode(layer[2*i+1])
                    cur_layer.append(node.right)
                if DEBUG:
                    print(f"{node.val} L-> {node.left and node.left.val} R-> {node.right and node.right.val}")
            prev_layer = cur_layer

    def print_tree(self):
        return print_tree_helper(self.root, 0)

def build_tree(val_lst, parent, cur_index):
    # base case 1: cur_index represents out of bound node
    if cur_index == len(val_lst):
        # return current parent
        return parent
    # base case 2: parent is None
    if parent is None:
        return None

    # general case: 0 <= cur_index < len(val_lst), parent is not None
    if 2 * cur_index + 1 < len(val_lst):
        # TreeNode(val)
        parent.left = TreeNode(val_lst[cur_index * 2 + 1])
        parent.left = build_tree(val_lst, parent.left, cur_index * 2 + 1)
    if 2 * cur_index + 2 < len(val_lst):
        parent.right = TreeNode(val_lst[cur_index * 2 + 2])
        parent.right = build_tree(val_lst, parent.right, cur_index * 2 + 2)

    return parent




if __name__ == "__main__":
    btree = BinaryTree(list(range(10)))
    print("Tree representation:")
    print(btree.print_tree())

