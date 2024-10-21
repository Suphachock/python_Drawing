import tkinter as tk

class RectangleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Draw Rectangle with Canvas Border")

        # Create a canvas widget with a border
        self.canvas = tk.Canvas(root, width=300, height=200, bg="white", borderwidth=2, relief="solid")
        self.canvas.pack(padx=10, pady=10)  # Add some padding around the canvas

        # Call the method to draw the rectangle
        self.draw_rectangle()

    def draw_rectangle(self):
        # Draw a rectangle: (x1, y1, x2, y2)
        self.canvas.create_rectangle(50, 50, 200, 150, outline="blue", fill="lightblue", width=2)

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    app = RectangleApp(root)
    root.mainloop()
