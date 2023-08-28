import tkinter as tk
import socket
import threading
from datetime import datetime

def receive_message():
    while True:
        try:
            # 接收服务器发送的消息
            data = client_socket.recv(1024).decode()
            message_list.insert(tk.END, data)
        except OSError:
            break

def send_message(event=None):
    message = input_entry.get("1.0", tk.END).strip()

    if message:
        # 获取当前时间
        now = datetime.now().strftime("%H:%M:%S")

        # 发送消息给服务器
        client_socket.send(f"{username} {now}: {message}".encode())

        # 清空输入框
        input_entry.delete("1.0", tk.END)

def handle_keypress(event):
    if event.keysym == 'Return' and event.state == 0:
        send_message()
    elif event.keysym == 'Return' and event.state == 8:
        input_entry.insert(tk.INSERT, '\n')

def close_connection():
    # 关闭客户端连接
    client_socket.close()
    root.destroy()

def get_username():
    global username
    # 获取用户名输入框的内容
    username = username_entry.get()

    if username:
        # 发送用户名给服务器
        client_socket.send(username.encode())

        # 隐藏用户名输入框，显示聊天界面
        username_entry.pack_forget()
        start_button.pack_forget()
        message_list.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        input_frame.pack(side=tk.BOTTOM, fill=tk.X)
        input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        send_button.pack(side=tk.LEFT)
        close_button.pack(side=tk.RIGHT)

        # 启动接收消息的线程
        receive_thread = threading.Thread(target=receive_message)
        receive_thread.start()
    else:
        # 提示用户输入用户名
        username_entry.config(bg='pink')
        username_entry.delete(0, tk.END)
        username_entry.insert(0, "请输入用户名")

# 连接服务器
HOST = input('Your chatroom IP:')
PORT = int(input('Port:'))
print(PORT, HOST)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# 创建GUI窗口
root = tk.Tk()
root.title("聊天程序")

# 设置窗口大小和位置
window_width = 300
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width - window_width
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# 添加用户名输入框和开始按钮
username_entry = tk.Entry(root)
username_entry.pack(fill=tk.BOTH)

start_button = tk.Button(root, text="开始", command=get_username)
start_button.pack(fill=tk.BOTH)

# 添加消息列表框和滚动条
message_list = tk.Listbox(root, height=15, width=50)
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.config(command=message_list.yview)
message_list.config(yscrollcommand=scrollbar.set)

# 添加输入框和发送、关闭按钮（放置在一个Frame中）
input_frame = tk.Frame(root)
input_entry = tk.Text(input_frame, height=3)
input_entry.bind('<Key>', handle_keypress)
send_button = tk.Button(input_frame, text="发送", command=send_message)
close_button = tk.Button(input_frame, text="关闭", command=close_connection)

root.mainloop()