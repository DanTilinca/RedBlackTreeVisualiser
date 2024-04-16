class Node:
    def __init__(self, data, color="red"):
        self.data = data  # Valoarea nodului
        self.color = color  # Culoarea nodului: rosu sau negru
        self.parent = None  # Referinta catre parintele nodului
        self.left = None  # Referinta catre copilul stang
        self.right = None  # Referinta catre copilul drept

class RBTree:
    def __init__(self):
        self.TNULL = Node(0, "black")
        self.TNULL.left = self.TNULL
        self.TNULL.right = self.TNULL
        self.root = self.TNULL

    # Traversare in preordine - radacina, stanga, dreapta
    def pre_order_helper(self, node):
        if node != self.TNULL:
            print(node.data, end=" ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    # Traversare in inordine - stanga, radacina, dreapta
    def in_order_helper(self, node):
        if node != self.TNULL:
            self.in_order_helper(node.left)
            print(node.data, end=" ")
            self.in_order_helper(node.right)

    # Traversare in postordine - stanga, dreapta, radacina
    def post_order_helper(self, node):
        if node != self.TNULL:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            print(node.data, end=" ")

    # Cauta un nod cu o cheie data in arbore
    def search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.data:
            return node

        if key < node.data:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    # Repara arborele dupa stergerea unui nod
    def fix_delete(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 'black' and s.right.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.right.color == 'black':
                        s.left.color = 'black'
                        s.color = 'red'
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 'black' and s.right.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.left.color == 'black':
                        s.right.color = 'black'
                        s.color = 'red'
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

    # Rotirea la stanga a unui nod
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # Rotirea la dreapta a unui nod
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Inlocuieste un subarbore ca fiu al parintelui sau cu un alt subarbore
    def rb_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Ajuta la stergerea unui nod din arbore
    def delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.data == key:
                z = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Couldn't find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'black':
            self.fix_delete(x)

    # Repara arborele dupa inserarea unui nod
    def fix_insert(self, k):
        while k.parent.color == 'red':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'black'

    # Insereaza un nod in arbore
    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = "red"

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = "black"
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    # Gaseste nodul cu valoarea minima in arbore
    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    # Returneaza radacina arborelui
    def get_root(self):
        return self.root

    # Sterge un nod din arbore
    def delete_node(self, data):
        self.delete_node_helper(self.root, data)

    # Afiseaza arborele
    def print_tree(self):
        self.pre_order_helper(self.root)

# Afiseaza detalii despre arbore (traversari)
def print_tree_details(rb_tree):
    print("In-order Traversal:")
    rb_tree.in_order_helper(rb_tree.get_root())
    print("\nPre-order Traversal:")
    rb_tree.pre_order_helper(rb_tree.get_root())
    print("\nPost-order Traversal:")
    rb_tree.post_order_helper(rb_tree.get_root())
    print("\n")

# Codul principal care testeaza insertii si stergeri in arbore
if __name__ == "__main__":
    rb_tree = RBTree()

    print("Testing Insertions:")
    values_to_insert = [7, 3, 18, 10, 22, 8, 11, 26, 2, 6, 13]
    for value in values_to_insert:
        rb_tree.insert(value)
    print_tree_details(rb_tree)

    print("Testing Deletion (deleting 18):")
    rb_tree.delete_node(18)
    print_tree_details(rb_tree)