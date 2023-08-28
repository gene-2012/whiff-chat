# WhiffyChat

## Introduction

This is a simple socket-based chat server and it's super lightweight! It allows multiple clients to connect to the server through the network and chat in real time. The following are the instructions for using this chat room server:

### Run the server

1. Run the `server.py` file on the server.

    ```bash
    If you are using Linux:
    python3 server.py

    If you are using Windows:
    python server.py
    ```

2. The server will start listening on the specified host and port (default is 0.0.0.0:4080). Make sure that the firewall settings allow incoming connections.

### Client Connection

1. The client needs to use `client.py` to connect to the server and send the user name and message.

    ```bash
    python client.py
    ```

Please use this command to start it.

2. The client connecting to the server will query the host and port of the server and display its user name to other clients.

3. The client can send messages to other clients in the chat room.

### Precautions

- Please ensure that the server and client are in the same network environment and can access each other. If the server and the client that needs to connect are not on the same local area network, please place the server on a server with a public IP address for operation.

- Please ensure that the port number is open in the firewall settings to allow clients to connect to the server.

- This chat room server is a simple example, without added user name and password authentication, and no security verification mechanism. Please use appropriate security measures in production environments.

### Copyright Information

Manufacturer: Geneluo

License: GNU GPL 3.0
