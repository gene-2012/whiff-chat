import socket
import threading

def handle_client(client_socket, client_address):
    # 接收客户端发送的用户名
    username = client_socket.recv(1024).decode()
    print(f"新用户加入聊天室：{username}")
    
    # 广播新用户加入的消息给其他客户端
    broadcast(f"{username} 加入了聊天室".encode())
    
    while True:
        try:
            # 接收客户端发送的消息
            data = client_socket.recv(1024)
            if data:
                # 广播消息给其他客户端
                broadcast(data)
            else:
                # 如果没有收到数据，说明客户端断开连接
                remove_client(client_socket)
                break
        except:
            # 发生异常，说明客户端断开连接
            remove_client(client_socket)
            break

def broadcast(message):
    # 广播消息给所有连接的客户端
    for client in clients:
        client.send(message)

def remove_client(client_socket):
    # 从客户端列表中移除断开连接的客户端
    clients.remove(client_socket)
    client_socket.close()

# 创建服务器套接字
HOST = 'localhost'
PORT = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

clients = []

print("服务器启动，等待客户端连接...")

while True:
    # 接受客户端连接
    client_socket, client_address = server_socket.accept()
    print(f"新的客户端连接：{client_address}")
    
    # 将新客户端添加到客户端列表
    clients.append(client_socket)
    
    # 创建新的线程来处理客户端
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()