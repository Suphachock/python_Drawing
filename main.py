import tkinter as tk
from tkinter import ttk

def update_inputs():
    current_widths = [entry.get() for entry in entry_widths if entry]
    current_heights = [entry.get() for entry in entry_heights if entry]
    current_types = [entry.get() for entry in entry_types if entry]

    for widget in frame_inputs.winfo_children():
        widget.destroy()

    quantity = int(combo_quantity.get())

    entry_widths.clear()
    entry_heights.clear()
    entry_types.clear()

    for i in range(quantity):
        ttk.Label(frame_inputs, text=f"Rectangle {i + 1} Width:").grid(row=i, column=0, padx=5, pady=5)
        entry_width = ttk.Entry(frame_inputs)
        entry_widths.append(entry_width)
        entry_width.grid(row=i, column=1, padx=5, pady=5)

        ttk.Label(frame_inputs, text=f"Rectangle {i + 1} Height:").grid(row=i, column=2, padx=5, pady=5)
        entry_height = ttk.Entry(frame_inputs)
        entry_heights.append(entry_height)
        entry_height.grid(row=i, column=3, padx=5, pady=5)
        
        ttk.Label(frame_inputs, text=f"Type:").grid(row=i, column=4, padx=5, pady=5)
        entry_type = ttk.Combobox(frame_inputs, values=["Type A", "Type B", "Type C"], state="readonly")  # Set to readonly
        entry_types.append(entry_type)
        entry_type.grid(row=i, column=5, padx=5, pady=5)

        if i < len(current_widths):
            entry_width.insert(0, current_widths[i])
        if i < len(current_heights):
            entry_height.insert(0, current_heights[i])
        if i < len(current_types):  # Restore type entries if available
            entry_type.set(current_types[i])  # Use set instead of insert for Combobox

def draw_rectangles():
    try:
        canvas.delete("all")

        quantity = int(combo_quantity.get())
        max_columns = 3
        max_rows = (quantity + max_columns - 1) // max_columns  # คำนวณจำนวนแถว
        cell_width = 250    # ความกว้างของแต่ละเซลล์
        cell_height = 200   # ความสูงของแต่ละเซลล์
        padding = 60        # ระยะห่างระหว่างเซลล์

        # ปรับขนาด canvas ตามจำนวนแถวและคอลัมน์
        canvas_width = max_columns * (cell_width + padding) + padding
        canvas_height = max_rows * (cell_height + padding) + padding
        canvas.config(width=canvas_width, height=canvas_height)

        for i in range(quantity):
            width = int(entry_widths[i].get())
            height = int(entry_heights[i].get())

            row = i // max_columns
            col = i % max_columns

            x = padding + col * (cell_width + padding)
            y = padding + row * (cell_height + padding)

            rect_x1 = x + (cell_width - width) / 2
            rect_y1 = y + (cell_height - height) / 2
            rect_x2 = rect_x1 + width
            rect_y2 = rect_y1 + height

            # วาดสี่เหลี่ยมในตำแหน่งที่คำนวณ
            canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, outline="blue", width=2)

            # แสดงข้อความ x และ y
            canvas.create_text(rect_x1 + width / 2, rect_y2 + 20, text=f"x = {width}", fill="black")
            canvas.create_text(rect_x2 + 30, rect_y1 + height / 2, text=f"y = {height}", fill="black")
            
            # ถ้าประเภทคือ Type A วาด "xxx" ที่กลางของด้านบน
            if entry_types[i].get() == "Type A":
                num_xs = 3  # จำนวน "x" ที่ต้องการวาด
                spacing = 0  # ระยะห่างที่น้อยที่สุด

                # คำนวณตำแหน่ง x สำหรับ "xxx"
                total_x_width = num_xs * 12 + (num_xs - 1) * spacing  # ความกว้างทั้งหมดที่ใช้สำหรับ "x"
                start_x = rect_x1 + (width - total_x_width) / 2  # ตำแหน่งเริ่มต้นที่กลางของ rectangle
                top_y = rect_y1  # ตำแหน่ง y ของด้านบน

                for j in range(num_xs):
                    x_position = start_x + j * (16 + spacing)  # ปรับตำแหน่ง "x"
                    canvas.create_text(x_position, top_y - 3, text="x", fill="black", font=("Arial", 14))


    except ValueError:
        label_status.config(text="Invalid input! Please enter positive integers for all rectangles.")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Draw Multiple Rectangles with Unique Sizes")
root.geometry("900x700")

ttk.Label(root, text="Quantity (1-6):").pack(pady=5)
combo_quantity = ttk.Combobox(root, values=[1, 2, 3, 4, 5, 6], state="readonly")
combo_quantity.set(1)
combo_quantity.pack()

ttk.Button(root, text="Update Inputs", command=update_inputs).pack(pady=10)

frame_inputs = ttk.Frame(root)
frame_inputs.pack(pady=10)

entry_widths = []
entry_heights = []
entry_types = []  # Ensure this list is initialized

label_status = ttk.Label(root, text="", foreground="red")
label_status.pack(pady=5)

ttk.Button(root, text="Draw Rectangles", command=draw_rectangles).pack(pady=10)

canvas = tk.Canvas(root, bg="white")
canvas.pack(expand=True, fill=tk.BOTH, pady=10)

root.mainloop()
