'''
create a TCP/IP banner server to center and to scroll what is sent to it onto a tkinter screen. Tkinter resizable screen size is 800 by 300. Font size is the height of the display area. Font face is STENCIL . Window title is TOTAL PYTHONEERING . Include the ability to change the color of the message.
'''
import socket
import threading
import tkinter as tk
from tkinter import font

class BannerServer:
    def __init__(self, host='127.0.0.1', port=65432):
        self.root = tk.Tk()
        self.root.title("TOTAL PYTHONEERING")
        self.root.geometry("800x300")
        self.root.configure(bg='black')

        self.display_text = "WAITING FOR DATA..."
        self.text_color = "lime"
        self.scroll_pos = 800

        # Setup Canvas
        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Start TCP Server thread
        self.server_thread = threading.Thread(target=self.start_server, args=(host, port), daemon=True)
        self.server_thread.start()

        self.update_scroll()
        self.root.mainloop()

    def start_server(self, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            while True:
                conn, addr = s.accept()
                with conn:
                    data = conn.recv(1024).decode('utf-8').strip()
                    if data:
                        # Logic to change color: if message starts with COLOR:RED|message
                        if data.startswith("COLOR:"):
                            try:
                                parts = data.split("|", 1)
                                self.text_color = parts[0].split(":")[1]
                                self.display_text = parts[1]
                            except:
                                self.display_text = data
                        else:
                            self.display_text = data
                        self.scroll_pos = self.root.winfo_width()

    def update_scroll(self):
        self.canvas.delete("all")
        
        # Calculate dynamic font size based on current window height
        win_height = self.root.winfo_height()
        win_width = self.root.winfo_width()
        banner_font = font.Font(family="Stencil", size=-(win_height)) # Negative size = pixels

        # Draw text
        self.canvas.create_text(
            self.scroll_pos, win_height // 2,
            text=self.display_text,
            fill=self.text_color,
            font=banner_font,
            anchor="w"
        )

        # Update position
        text_width = banner_font.measure(self.display_text)
        self.scroll_pos -= 5
        if self.scroll_pos < -text_width:
            self.scroll_pos = win_width

        self.root.after(30, self.update_scroll)

if __name__ == "__main__":
    BannerServer()
