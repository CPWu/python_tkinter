import socket
import requests
from vidstream import *
import tkinter as tk
import threading

local_ip_address = socket.gethostbyname(socket.gethostname())
public_ip_address = requests.get("https://api.ipify.org").text

print(local_ip_address)
print(public_ip_address)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600
PORT = 5555
server = StreamingServer(local_ip_address, 5555)


def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t1.start()


def start_camera_stream():
    camera_client = CameraClient(txt_target_ip.get(1.0, "end-1c"), 7777)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()


window = tk.Tk()
window.title("Robot View v0.0.1")
window.geometry("{}x{}".format(WINDOW_HEIGHT, WINDOW_WIDTH))
lbl_target_ip = tk.Label(window, text="Target IP: ")
lbl_target_ip.pack()
txt_target_ip = tk.Text(window, height=1)
txt_target_ip.pack()

btn_listen = tk.Button(
    window, text="Start Listening...", width=50, command=start_listening
)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(
    window, text="Start Camera Stream...", width=50, command=start_camera_stream
)
btn_camera.pack(anchor=tk.CENTER, expand=True)

window.mainloop()
