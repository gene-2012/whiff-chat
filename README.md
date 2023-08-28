# WhiffyChat

## 简介

这是一个基于Socket的简单聊天室服务器，它允许多个客户端通过网络连接到服务器并实时聊天。下面是使用该聊天室服务器的说明：

### 运行服务器

1. 在服务器上运行 `server.py` 文件。

   ```bash
   如果您使用的是linux:
   python3 server.py
   如果使用windows:
   python server.py
   ```

2. 服务器将开始监听指定的主机和端口（默认为 0.0.0.0:4080）。确保防火墙设置允许传入的连接。

### 客户端连接

1. 客户端需要使用 `client.py` 连接到服务器，并发送用户名和消息。

   ```bash
      python client.py
   ```

   请使用这个指令进行启动。

2. 连接到服务器的客户端将询问服务端的Host和Port，并将其用户名显示给其他客户端。

3. 连接到服务器后，需要输入一个密码，密码将存储在服务器所在的目录下`users.json`文件中，该文件默认未添加，请按照以下的格式添加：

   ```json
   {
      "username1":"password1",
      "username2":"password2"
   }
   ```

4. 客户端可以发送消息给聊天室中的其他客户端。

### 注意事项

- 请确保服务器和客户端在相同的网络环境中，并且可以相互访问。如果服务器与需要连接的客户端不存在于同一个局域网内，请 您将服务端放置在有公网ip的服务器进行操作。
- 请确保端口号在防火墙设置中是开放的，以允许客户端连接到服务器。
- 该聊天室服务器是一个简单的示例，仅进行了简单的用户名密码验证，没有实现安全性验证机制。请在生产环境中使用适当的安全措施。

### 版权信息 Copyright

制作者：Geneluo

许可证：CC BY-SA4.0
![CC BY-SA4.0](https://static.wikia.nocookie.net/central/images/f/f3/1000px-cc-by-sa_icon-svg.png/revision/latest/scale-to-width-down/180?cb=20120717220047)
