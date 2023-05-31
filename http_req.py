import socket

# Define the target website and path
host = 'www.google.com'
path = 'index'

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the website
client_socket.connect((host, 80))

# Send an HTTP GET request
request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
client_socket.send(request.encode())

# Receive the response data
response = b""
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    response += data

# Close the socket
client_socket.close()

# Extract the body of the response
header_end = response.find(b"\r\n\r\n")
body = response[header_end+4:]

# Write the body to a file
filename = f"www_{host}.html"
with open(filename, "wb") as file:
    file.write(body)
    
print(f"Saved response body to {filename}")
