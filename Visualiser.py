import tkinter as tk
from RBTree import RBTree, Node

class RBTreeVisualizer:
    def __init__(self, rb_tree):
        self.rb_tree = rb_tree
        self.window = tk.Tk()
        self.window.title("Red-Black Tree Visualizer")
        self.canvas = tk.Canvas(self.window, width=800, height=600, bg='white')
        self.canvas.pack()

    def draw_node(self, node, x, y, dx):
        if node is None or node == self.rb_tree.TNULL:
            return

        fill = 'red' if node.color == 'red' else 'black'
        self.canvas.create_oval(x-20, y-20, x+20, y+20, fill=fill, outline='black')
        self.canvas.create_text(x, y, text=str(node.data), fill='white')

    
    def draw_tree(self, node, x, y, dx):
        if node is None or node == self.rb_tree.TNULL:
            return

        if node.left and node.left != self.rb_tree.TNULL:
            self.canvas.create_line(x, y, x-dx, y+60, fill='black')
            self.draw_tree(node.left, x-dx, y+60, dx//2)

        if node.right and node.right != self.rb_tree.TNULL:
            self.canvas.create_line(x, y, x+dx, y+60, fill='black')
            self.draw_tree(node.right, x+dx, y+60, dx//2)

        self.draw_node(node, x, y, dx)


    def display(self):
        self.draw_tree(self.rb_tree.root, 400, 30, 200)
        self.window.mainloop()


if __name__ == "__main__":
    rb_tree = RBTree()
    
    values_to_insert = [7, 3, 18, 10, 22, 8, 11, 26, 2, 6, 13, 27]
    for value in values_to_insert:
        rb_tree.insert(value)
    rb_tree.delete_node(18)

    visualizer = RBTreeVisualizer(rb_tree)
    visualizer.display()