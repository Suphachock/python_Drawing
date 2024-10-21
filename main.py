import tkinter as tk
from tkinter import ttk

class RectangleDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Draw Multiple Rectangles with Unique Sizes")
        self.root.geometry("900x700")

        self.entry_widths = []
        self.entry_heights = []
        self.entry_types = []

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Quantity (1-6):").pack(pady=5)
        self.combo_quantity = ttk.Combobox(self.root, values=[1, 2, 3, 4, 5, 6], state="readonly")
        # self.combo_quantity.set(1)
        self.combo_quantity.bind("<<ComboboxSelected>>", self.update_inputs)
        self.combo_quantity.pack()

        # ttk.Button(self.root, text="Update Inputs", command=self.update_inputs).pack(pady=5)

        self.frame_inputs = ttk.Frame(self.root)
        self.frame_inputs.pack(pady=10)

        self.label_status = ttk.Label(self.root, text="", foreground="red")
        self.label_status.pack(pady=5)

        ttk.Button(self.root, text="Draw Rectangles", command=self.draw_rectangles).pack(pady=5)

        self.canvas = tk.Canvas(self.root, bg="white", borderwidth=2, relief="solid")
        self.canvas.pack(expand=True, fill=tk.BOTH, pady=15, padx=15)

    def update_inputs(self,event):
        current_widths = [entry.get() for entry in self.entry_widths if entry]
        current_heights = [entry.get() for entry in self.entry_heights if entry]
        current_types = [entry.get() for entry in self.entry_types if entry]

        for widget in self.frame_inputs.winfo_children():
            widget.destroy()

        quantity = int(self.combo_quantity.get())

        self.entry_widths.clear()
        self.entry_heights.clear()
        self.entry_types.clear()

        for i in range(quantity):
            ttk.Label(self.frame_inputs, text=f"Rectangle {i + 1} Width:").grid(row=i, column=0, padx=5, pady=5)
            entry_width = ttk.Entry(self.frame_inputs)
            self.entry_widths.append(entry_width)
            entry_width.grid(row=i, column=1, padx=5, pady=5)

            ttk.Label(self.frame_inputs, text=f"Rectangle {i + 1} Height:").grid(row=i, column=2, padx=5, pady=5)
            entry_height = ttk.Entry(self.frame_inputs)
            self.entry_heights.append(entry_height)
            entry_height.grid(row=i, column=3, padx=5, pady=5)
            
            ttk.Label(self.frame_inputs, text="Type:").grid(row=i, column=4, padx=5, pady=5)
            entry_type = ttk.Combobox(self.frame_inputs, values=["Type A", "Type B", "Type C"], state="readonly")
            self.entry_types.append(entry_type)
            entry_type.grid(row=i, column=5, padx=5, pady=5)

            if i < len(current_widths):
                entry_width.insert(0, current_widths[i])
            if i < len(current_heights):
                entry_height.insert(0, current_heights[i])
            if i < len(current_types):
                entry_type.set(current_types[i])

    def draw_rectangles(self):
        try:
            if (self.entry_widths and self.entry_heights) :
                self.canvas.delete("all")
                quantity = int(self.combo_quantity.get())
                max_columns = 3
                max_rows = (quantity + max_columns - 1) // max_columns
                cell_width = 250
                cell_height = 200
                padding = 60

                canvas_width = max_columns * (cell_width + padding) + padding
                canvas_height = max_rows * (cell_height + padding) + padding
                self.canvas.config(width=canvas_width, height=canvas_height)

                for i in range(quantity):
                    width = int(self.entry_widths[i].get())
                    height = int(self.entry_heights[i].get())

                    row = i // max_columns
                    col = i % max_columns

                    x = padding + col * (cell_width + padding)
                    y = padding + row * (cell_height + padding)

                    rect_x1 = x + (cell_width - width) / 2
                    rect_y1 = y + (cell_height - height) / 2
                    rect_x2 = rect_x1 + width
                    rect_y2 = rect_y1 + height

                    self.canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, outline="blue", width=2)
                    self.canvas.create_text(rect_x1 + width / 2, rect_y2 + 20, text=f"x = {width}", fill="black")
                    self.canvas.create_text(rect_x2 + 30, rect_y1 + height / 2, text=f"y = {height}", fill="black")

                    if self.entry_types[i].get() == "Type A":
                        num_xs = 3
                        spacing = 0
                        total_x_width = num_xs * 12 + (num_xs - 1) * spacing
                        start_x = rect_x1 + (width - total_x_width) / 2
                        top_y = rect_y1

                        for j in range(num_xs):
                            x_position = start_x + j * (16 + spacing)
                            self.canvas.create_text(x_position, top_y - 3, text="x", fill="black", font=("Arial", 14))

        except ValueError:
            self.label_status.config(text="Invalid input! Please enter positive integers for all rectangles.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RectangleDrawer(root)
    root.mainloop()
