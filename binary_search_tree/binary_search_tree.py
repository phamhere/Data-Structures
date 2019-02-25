class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current_node = self
        while True:
            # if value is less than current node's value
            if value < current_node.value:
                # assign to current node's left if empty and stop loop
                if not current_node.left:
                    current_node.left = BinarySearchTree(value)
                    break
                # otherwise will move to left node and loop again
                else:
                    current_node = current_node.left
            # if value is greater than current node's value
            elif value > current_node.value:
                # assign to current node's right if empty and stop loop
                if not current_node.right:
                    current_node.right = BinarySearchTree(value)
                    break
                # otherwise will move to right node and loop again
                else:
                    current_node = current_node.right
            # does nothing if values are equal
            else:
                break

    def contains(self, target):
        current_node = self
        # keeps looping until value is found or reaches end of bst
        while True:
            # returns True and breaks out if target value is found
            if current_node.value == target:
                return True
            elif target < current_node.value:
                # returns False if no left node exists
                if not current_node.left:
                    return False
                # if left node exists, reloops setting it as current node
                else:
                    current_node = current_node.left
            else:
                # returns False no right node exists
                if not current_node.left:
                    return False
                # if right node exists, reloops setting it as current node
                else:
                    current_node = current_node.right

    def get_max(self):
        current_node = self
        max = self.value
        while current_node.right:
            max = current_node.right.value
            current_node = current_node.right
        return max
