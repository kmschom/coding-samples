class Node(object):
    """
    A class to represent a node.
    Stores an integer.

    Attributes
    ----------
    data : an integer
    """
    def __init__(self, data, left=None, right=None, parent=None, color='red'):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color


class rb_tree(object):
    """
    A class to represent a red-black tree which is built of the rule for a binary search tree.

    When initialized, creates a tree with nothing at the root.
    A sentinel node is used to indicate that there is a "None" value stored as the parent node or
        the left and right children on a node.
    A tree is built as the insert method is called to add new nodes to the tree.
    Nodes are sorted upon insertion so that any node to the left of it's parent node is
        smaller than the parent node and any node to the right of it's parent node is
        larger than the parent node.
    Red-Black tree properties:
        1. Every node is either red or black
        2. Every leaf node counts as black
        3. If a node is red, then both its children are black
        4. Every simple path from a node to a descendant leaf contains the same number of black nodes
        5. The root node is always black
    The class constants are used to define different traversal types in the traversal method.

    Methods
    -------
    print_tree():
        Prints the data of all nodes in order
    __print_tree(curr_node):
        Recursively prints a subtree in preorder, rooted at curr_node
    __print_with_colors(curr_node):
        Recursively print a subtree in preorder, rooted at curr_node
        Extracts the color of the node and prints it in the format -dataC- where C is B for black and R for red
    print_with_colors():
        Prints the data of all nodes but with color indicators
    inorder(self):
        Calls for an inorder traversal
    preorder(self):
        Calls for a preorder traversal
    postorder(self):
        Calls for a postorder traversal
    __traverse(curr_node, traversal_type):
        Uses generators to run a traversal based on the traversal type called that starts at the curr_node
    find_min():
        Travels across the leftChild of every node, and returns the node who has no leftChild
        This is the min value of a subtree
    find_node(self, data):
        Expects a data and returns the Node object for the given data
    __get(data, current_node):
        Receives a data and a node and returns the node with the given data
    find_successor(data):
        Finds the successor to the node that holds the given data value, else returns None
    def insert(data):
        Adds a node to the tree that holds data
    bst_insert(data):
        Insertion of a node that holds data for Binary Search Tree
    __put(data, current_node)
        Finds the appropriate place to add a node holding data in the tree
    delete(data):
        Finds the node that hold data, deletes the node, and calls rb_delete fixup at the end
    left_rotate(current_node):
        Performs a left rotation on current_node
    right_rotate(current_node):
        Performs a right rotation on current_node
    __rb_insert_fixup(z):
        Maintains the balancing and coloring property after bst insertion into the tree.
    __rb_delete_fixup(x):
        Maintains the balancing and coloring property after bst deletion from the tree.
    """
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    # initialize root and size
    def __init__(self):
        self.root = None
        self.sentinel = Node(None, color='black')
        self.sentinel.parent = self.sentinel
        self.sentinel.left = self.sentinel
        self.sentinel.right = self.sentinel

    def print_tree(self):
        """
        Prints the data of all nodes in order
        """
        self.__print_tree(self.root)

    def __print_tree(self, curr_node):
        """
        Recursively prints a subtree in order, rooted at curr_node
        Printing in preorder
        ...

        Parameters
        ----------
        curr_node :  Root node of subtree to print
        """
        if curr_node is not self.sentinel:
            print(str(curr_node.data), end=' ')  # save space
            self.__print_tree(curr_node.left)
            self.__print_tree(curr_node.right)

    def __print_with_colors(self, curr_node):
        """
        Recursively prints a subtree in order, rooted at curr_node
        Printed in preorder
        Extracts the color of the node and print it in the format -dataC- where C is B for black and R for red
        ...

        Parameters
        ----------
        curr_node :  Root node of subtree to print
        """
        if curr_node is not self.sentinel:

            if curr_node.color is "red":
                node_color = "R"
            else:
                node_color = "B"

            print(str(curr_node.data) + node_color, end=' ')  # save space
            self.__print_with_colors(curr_node.left)
            self.__print_with_colors(curr_node.right)

    def print_with_colors(self):
        """
        Prints the data of all nodes but with color indicators
        """
        self.__print_with_colors(self.root)

    def __iter__(self):
        return self.inorder()

    def inorder(self):
        """
        Calls the traverse method for an inorder traversal
        """
        return self.__traverse(self.root, rb_tree.INORDER)

    def preorder(self):
        """
        Calls the traverse method for an preorder traversal
        """
        return self.__traverse(self.root, rb_tree.PREORDER)

    def postorder(self):
        """
        Calls the traverse method for an postorder traversal
        """
        return self.__traverse(self.root, rb_tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        """
        Uses generators to run a traversal based on the traversal type called.
        Traversal starts at curr_node and yields data of each node in the traversal path.
        ...

        Parameters
        ----------
        curr_node :  Node that serves as the root of the traversal
        traversal_type :  Integer associated with a traversal type by the class constants
        """
        if curr_node is not self.sentinel:
            if traversal_type == self.PREORDER:
                yield curr_node
            yield from self.__traverse(curr_node.left, traversal_type)
            if traversal_type == self.INORDER:
                yield curr_node
            yield from self.__traverse(curr_node.right, traversal_type)
            if traversal_type == self.POSTORDER:
                yield curr_node

    def find_min(self):
        """
        Returns the minimum value held in a tree by traveling across the left child of every node
            and returning node with no left child.
        """
        # find_min travels across the leftChild of every node, and returns the
        # node who has no leftChild. This is the min value of a subtree
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node

    def find_node(self, data):
        """
        Returns the node object with that particular data value, else returns a KeyError
        Returns a KeyError if tree has no root
        ...

        Parameters
        ----------
        data :  Data value being searched for
        """
        if self.root:
            res = self.__get(data, self.root)
            if res:
                return res
            else:
                raise KeyError('Error, data not found')
        else:
            raise KeyError('Error, tree has no root')

    def __get(self, data, current_node):
        """
        Receives data and current_node and returns node with the given data.
        Returns a KeyError if tree has no root
        ...

        Parameters
        ----------
        data :  Data value being searched for
        current_node : Node to start the search for data at
        """
        if current_node is self.sentinel:  # if current_node does not exist return None
            print("couldnt find data: {}".format(data))
            return None
        elif current_node.data == data:
            return current_node
        elif data < current_node.data:
            # recursively call __get with data and current_node's left
            return self.__get(data, current_node.left)
        else:  # data is greater than current_node.data
            # recursively call __get with data and current_node's right
            return self.__get(data, current_node.right)

    def find_successor(self, data):
        """
        Finds the successor to the node that holds the given data value, else returns None.
        If the right subtree of the node is nonempty, then the successor is the leftmost node
            in the right subtree.
        If the right subtree of the node is empty, then goes up the tree until finding a node
            that is the left child of it's parent. Parent of that node is the successor.
        ...

        Parameters
        ----------
        data :  data value for the node that function is trying to find successor for
        """
        current_node = self.find_node(data)

        if current_node is self.sentinel:
            raise KeyError

        # Travel left down the rightmost subtree
        if current_node.right:
            current_node = current_node.right
            while current_node.left is not self.sentinel:
                current_node = current_node.left
            successor = current_node

        # Travel up until the node is a left child
        else:
            parent = current_node.parent
            while parent is not self.sentinel and current_node is not parent.left:
                current_node = parent
                parent = parent.parent
            successor = parent

        if successor:
            return successor
        else:
            return None

    def insert(self, data):
        """
        Finds the right place in the tree to insert the new node holding value data
        ...

        Parameters
        ----------
        data :  Data value held by the new node being inserted
        """
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            new_node = self.__put(data, self.root)
            self.__rb_insert_fixup(new_node)
        else:  # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent=self.sentinel, left=self.sentinel, right=self.sentinel)
            new_node = self.root
            self.__rb_insert_fixup(new_node)

    def bst_insert(self, data):
        """
        Finds the right place in the tree to insert the new node holding value data according to
            insertion rules for a binary search tree
        ...

        Parameters
        ----------
        data :  Data value held by the new node being inserted
        """
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            self.__put(data, self.root)
        else:  # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent=self.sentinel, left=self.sentinel, right=self.sentinel)

    # helper function __put finds the appropriate place to add a node in the tree
    def __put(self, data, current_node):
        """
        Helper function that finds the appropriate place to add a node in the tree
        ...

        Parameters
        ----------
        data :  Data value held by the new node being put into the tree
        current_node : Node to start looking for the proper insertion place at
        """
        if data < current_node.data:
            if current_node.left != self.sentinel:
                new_node = self.__put(data, current_node.left)
            else:  # current_node has no child
                new_node = Node(data,
                                parent=current_node,
                                left=self.sentinel,
                                right=self.sentinel)
                current_node.left = new_node
        else:  # data is greater than or equal to current_node's data
            if current_node.right != self.sentinel:
                new_node = self.__put(data, current_node.right)
            else:  # current_node has no right child
                new_node = Node(data,
                                parent=current_node,
                                left=self.sentinel,
                                right=self.sentinel)
                current_node.right = new_node
        return new_node

    def delete(self, data):
        """
        Finds the node that holds value data to delete from tree.
        If the node has no children, the parent's pointer is set to None.
        If the node has one child, the parent's pointer is set to that child.
        If the node has two children, replace the node with it's successor and remove
            successor from previous location.
        Call rb_delete fixup at the end to ensure that the Red-Black tree properties are maintained
        ...

        Parameters
        ----------
        data :  data value for the node that function is trying to delete
        """
        z = self.find_node(data)
        if z.left is self.sentinel or z.right is self.sentinel:
            y = z
        else:
            y = self.find_successor(z.data)

        if y.left is not self.sentinel:
            x = y.left
        else:
            x = y.right

        if x is not self.sentinel:
            x.parent = y.parent

        if y.parent is self.sentinel:
            self.root = x

        else:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x

        if y is not z:
            z.data = y.data

        if y.color == 'black':
            if x is self.sentinel:
                self.__rb_delete_fixup(y)
            else:
                self.__rb_delete_fixup(x)

    def left_rotate(self, current_node):
        """
        Performs a left rotation on current_node
        If x is the root of the tree to rotate with left child subtree T1 and right child y,
            where T2 and T3 are the left and right children of y then:
                x becomes left child of y and T3 as its right child of y
                T1 becomes left child of x and T2 becomes right child of x
        ...

        Parameters
        ----------
        current_node :  node to perform the rotation on
        """

        if current_node == None:
            raise KeyError('Tree is empty')
        pivot = current_node.right
        if pivot != self.sentinel:
            current_node.right = pivot.left
            if pivot.left != self.sentinel:
                pivot.left.parent = current_node
            pivot.parent = current_node.parent
            if current_node.parent == self.sentinel:
                self.root = pivot
            elif current_node == current_node.parent.left:
                current_node.parent.left = pivot
            else:
                current_node.parent.right = pivot
            pivot.left = current_node
            current_node.parent = pivot

    def right_rotate(self, current_node):
        """
        Performs a right rotation on current_node
        If y is the root of the tree to rotate with right child subtree T3 and left child x,
            where T1 and T2 are the left and right children of x then:
                y becomes right child of x and T1 as its left child of x
                T2 becomes left child of y and T3 becomes right child of y
        ...

        Parameters
        ----------
        current_node :  node to perform the rotation on
        """
        if current_node == None:
            raise KeyError('Tree is empty')
        pivot = current_node.left
        if pivot != self.sentinel:
            current_node.left = pivot.right
            if pivot.right != self.sentinel:
                pivot.right.parent = current_node
            pivot.parent = current_node.parent
            if current_node.parent == self.sentinel:
                self.root = pivot
            elif current_node == current_node.parent.left:
                current_node.parent.left = pivot
            else:
                current_node.parent.right = pivot
            pivot.right = current_node
            current_node.parent = pivot

    def __rb_insert_fixup(self, z):
        """
        Checks to see if the tree breaks any of the Red-Black properties after a node has been inserted into the tree.
        If so, performs the appropriate rotations or re-colorings.
        ...

        Parameters
        ----------
        current_node :  node to perform the rotation on
        """
        while z.parent.color is "red":
            if z.parent == z.parent.parent.left:
                uncle = z.parent.parent.right
                if uncle.color is "red":
                    z.parent.color = "black"
                    uncle.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.right_rotate(z.parent.parent)
            else:
                uncle = z.parent.parent.left
                if uncle.color is "red":
                    z.parent.color = "black"
                    uncle.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.left_rotate(z.parent.parent)
        self.root.color = "black"

    def __rb_delete_fixup(self, x):
        """
        Checks to see if the tree breaks any of the Red-Black properties after a node has been deleted from the tree.
        If so, performs the appropriate rotations or re-colorings.
        ...

        Parameters
        ----------
        current_node :  node to perform the rotation on
        """
        while x != self.root and x.color is "black":
            if x == x.parent.left:
                w = x.parent.right
                if w.color is "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color is "black" and w.right.color is "black":
                    w.color = "red"
                    x = x.parent
                else:
                    if w.right.color is "black":
                        w.left.color = "black"
                        w.color = "red"
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color is "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color is "black" and w.left.color is "black":
                    w.color = "red"
                    x = x.parent
                else:
                    if w.left.color is "black":
                        w.right.color = "black"
                        w.color = "red"
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.left.color = "black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "black"
