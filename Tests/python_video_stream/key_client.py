import io
import socket
import struct
import time
from pygame import key, K_w, K_a, K_s, K_d

client_socket = socket.socket()

client_socket.connect(('127.0.1.1', 7000))  # ADD IP HERE

# Make a file-like object out of the connection
connection = client_socket.makefile('wb')

try:
    keys = key.get_pressed()
    connection.write(keys[K_w])
finally:
    connection.close()
    client_socket.close()
