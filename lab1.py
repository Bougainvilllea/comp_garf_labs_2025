import tkinter as tk
import math

root = tk.Tk()
root.title("Лаба 1")
root.geometry("600x600")

canvas = tk.Canvas(root, width=500, height=500, bg="yellow")
canvas.pack(pady=20)

circle = None
square = None
triangle = None


def toggle_circle():
    global circle
    if circle:
        points = []
        center_x, center_y = 100, 150
        radius = 50
        for angle in range(0, 360, 5):
            rad = angle * math.pi / 180
            x = center_x + radius * math.cos(rad)
            y = center_y + radius * math.sin(rad)
            points.extend([x, y])
        circle = canvas.create_polygon(points, fill="yellow")
        circle = None
    else:
        points = []
        center_x, center_y = 100, 150
        radius = 50
        for angle in range(0, 360, 5):
            rad = angle * math.pi / 180
            x = center_x + radius * math.cos(rad)
            y = center_y + radius * math.sin(rad)
            points.extend([x, y])
        circle = canvas.create_polygon(points, fill="red")

def toggle_square():
    global square
    if square:
        start_x, start_y = 250, 100
        size = 100
        points = [
            start_x, start_y,
            start_x + size, start_y,
            start_x + size, start_y + size,
            start_x, start_y + size
        ]
        square = canvas.create_polygon(points, fill="yellow")
        square = None
    else:
        start_x, start_y = 250, 100
        size = 100
        points = [
            start_x, start_y,
            start_x + size, start_y,
            start_x + size, start_y + size,
            start_x, start_y + size
        ]
        square = canvas.create_polygon(points, fill="blue")

def toggle_triangle():
    global triangle
    if triangle:
        start_x, start_y = 400, 200
        size = 100
        height = size * math.sqrt(3) / 2
        points = [
            start_x, start_y,
            start_x + size, start_y,
            start_x + size/2, start_y - height
        ]
        triangle = canvas.create_polygon(points, fill="yellow")
        triangle = None
    else:
        start_x, start_y = 400, 200
        size = 100
        height = size * math.sqrt(3) / 2
        points = [
            start_x, start_y,
            start_x + size, start_y,
            start_x + size/2, start_y - height
        ]
        triangle = canvas.create_polygon(points, fill="green")

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

circle_btn = tk.Button(btn_frame, text="Круг", command=toggle_circle, width=12)
circle_btn.pack(side=tk.LEFT, padx=5)

square_btn = tk.Button(btn_frame, text="Квадрат", command=toggle_square, width=12)
square_btn.pack(side=tk.LEFT, padx=5)

triangle_btn = tk.Button(btn_frame, text="Треугольник", command=toggle_triangle, width=12)
triangle_btn.pack(side=tk.LEFT, padx=5)

root.mainloop()
