import fitz  # PyMuPDF
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class PDFViewer:
    def __init__(self, pdf_path, dpi=300):
        self.pdf_path = pdf_path
        self.doc = fitz.open(self.pdf_path)
        self.current_page = 0

        # Set the resolution (DPI)
        zoom_factor = dpi / 72.0  # 72 DPI is the default resolution
        self.matrix = fitz.Matrix(zoom_factor, zoom_factor)

        self.root = tk.Tk()
        self.root.title("PDF Viewer")
        self.root.attributes('-fullscreen', True)

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.root.bind("<Escape>", self.exit_fullscreen)
        self.root.bind("<Left>", self.previous_page)
        self.root.bind("<Right>", self.next_page)

        self.display_page()

    def display_page(self):
        page = self.doc[self.current_page]
        pix = page.get_pixmap(matrix=self.matrix)
        img = ImageTk.PhotoImage(Image.frombytes("RGB", [pix.width, pix.height], pix.samples))

        self.canvas.config(width=img.width(), height=img.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

        self.root.mainloop()

    def next_page(self, event):
        if self.current_page < len(self.doc) - 1:
            self.current_page += 1
            self.display_page()

    def previous_page(self, event):
        if self.current_page > 0:
            self.current_page -= 1
            self.display_page()

    def exit_fullscreen(self, event):
        self.root.attributes('-fullscreen', False)
        self.root.destroy()


if __name__ == "__main__":
    pdf_path = r'C:\Users\alexa\Desktop\AI learn\Bishop C. Deep Learning. Foundations and Concepts 2023-crop.pdf'
    viewer = PDFViewer(pdf_path, dpi=100)
