import socket
import os

# 创建一个UDP socket对象， AF_INET表示使用IPv4地址，SOCK_DGRAM表示使用UDP协议
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口号，假设端口号为12345，""表示接受任意IP地址的连接
server_port = 12345
server_socket.bind(("", server_port))

# 打印服务器启动信息，告知用户服务器正在监听的端口号
print(f"UDP Server is running on port {server_port}...")

# 无限循环以接收数据
while True:
   # 接收客户端发送的数据，recvfrom方法返回数据和发送者的地址
    data, addr = server_socket.recvfrom(1024)  # 缓冲区大小为1024字节
    print(f"Received {len(data)} bytes from {addr}")

    # 将接收到的数据写入文件，'ab'模式表示以二进制格式追加数据到文件末尾
    with open("received_file", "ab") as file:  # 'ab'模式表示追加到文件末尾
        file.write(data)
    # 打印信息，告知用户数据已经被写入文件
    print("Data has been written to 'received_file'")