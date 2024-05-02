import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

class MapMaker:
    def __init__(self, root):
        self.root = root
        self.root.title("Map Maker")
        self.map_image = tk.Image.open("map.png")
        self.map_photo = tk.PhotoImage(self.map_image)
        self.map_label = tk.Label(self.root, image=self.map_photo)
        self.map_label.pack()
        self.is_drawing = False
        self.last_x, self.last_y = None, None
        self.map_label.bind("<ButtonPress-1>", self.start_draw)
        self.map_label.bind("<B1-Motion>", self.draw)
        self.map_label.bind("<ButtonRelease-1>", self.stop_draw)
    
    def start_draw(self, event):
        self.is_drawing = True
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.is_drawing:
            if self.last_x and self.last_y:
                self.map_image = self.map_image.convert("RGB")  # Convert to RGB for editing
                draw = ImageDraw.Draw(self.map_image)
                draw.line((self.last_x, self.last_y, event.x, event.y), fill="green", width=3)
                self.last_x, self.last_y = event.x, event.y
                self.map_photo = ImageTk.PhotoImage(self.map_image)
                self.map_label.config(image=self.map_photo)

    def stop_draw(self, event):
        self.is_drawing = False
    
    root = tk.Tk()

    app = MapMaker(root)

    root.mainloop()

        