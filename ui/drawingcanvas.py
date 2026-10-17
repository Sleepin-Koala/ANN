import customtkinter as ctk
from tkinter import Canvas
from PIL import Image, ImageDraw

class DrawingCanvas(Canvas):
    SIZE = 8          # trait plus épais = plus lisible pour un réseau
    COLOR = "#1a1a2e"  # encre sombre, pas noir pur

    def __init__(self, frame: ctk.CTkFrame):
        super().__init__(
            frame,
            bg="#f8f8f5",          # blanc cassé, moins agressif que #ffffff
            width=260,
            height=260,
            highlightthickness=0,
            cursor="crosshair",
            borderwidth=0,
        )

        self.cursor_x = None
        self.cursor_y = None
        self.paintcolor = self.COLOR

        self.image = Image.new("L", (260, 260), 0)
        self.draw_img = ImageDraw.Draw(self.image)

        self.bind("<Button-1>", self.start_draw)
        self.bind("<B1-Motion>", self.draw)
        self.bind("<ButtonRelease-1>", self.stop_draw)

    def clear(self):
        self.delete("all")
        self.draw_img.rectangle([0, 0, 260, 260], fill=0)

    def start_draw(self, event):
        self.cursor_x = event.x
        self.cursor_y = event.y
        r = self.SIZE / 2
        self.create_oval(
            event.x - r, event.y - r,
            event.x + r, event.y + r,
            fill=self.COLOR, outline=self.COLOR
        )

        self.draw_img.ellipse([event.x - r, event.y - r, event.x + r, event.y + r], fill=255)

    def draw(self, event):
        if self.cursor_x is None or self.cursor_y is None:
            return
        self.create_line(
            self.cursor_x, self.cursor_y,
            event.x, event.y,
            fill=self.paintcolor,
            width=self.SIZE,
            capstyle="round",
            joinstyle="round",
            smooth=True
        )

        self.draw_img.line([self.cursor_x, self.cursor_y, event.x, event.y],
                       fill=255, width=self.SIZE)

        
        self.cursor_x = event.x
        self.cursor_y = event.y

    def stop_draw(self, event):
        self.cursor_x = None
        self.cursor_y = None

        # self.image.save("test.png")

    