import socket
import sys

# 检查命令行参数数量
if len(sys.argv) != 3:
    print("Usage: python udpclient.py <ServerIP> <ServerPort>")
    sys.exit(1)
# sys.argv是一个列表，其中包含了命令行调用时传递的参数
# 如果参数数量不等于3（脚本名+两个参数），则打印使用方法并退出
# 从命令行参数获取服务器的IP地址和端口号
server_ip = sys.argv[1]
# sys.argv[0]是脚本名称，sys.argv[1]是第一个参数，即服务器IP地址
server_port = int(sys.argv[2])
# sys.argv[2]是第二个参数，即服务器端口号，转换成整数类型
# 创建UDP socketp AF_INET表示使用IPv4地址，SOCK_DGRAM表示使用UDP协议
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 打开要发送的文件
file_path = "file"  # 这里假设要发送的文件名为file
try:
    with open(file_path, "rb") as file:
        # 读取文件并发送
        while True:
            data = file.read(1024)  # 每次读取1024字节
            if not data:
                break  # 如果读取的数据为空，说明文件已经读取完毕，跳出循环
            client_socket.sendto(data, (server_ip, server_port))   # sendto方法发送数据到指定的IP地址和端口号

    print(f"File '{file_path}' has been sent to {server_ip}:{server_port}")# 打印文件发送成功的信息
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")

# 关闭socket连接，释放资源[pd]
client_socket.close()
#输入python3 udpclient.py 192.168.244.21(目标地址) 12345(目标端口号与udpserver.py中的端口号保持一致)