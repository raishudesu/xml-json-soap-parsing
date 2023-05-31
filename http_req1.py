import socket

#user input for domain name
hostname = input("Enter Domain Name: ")
path = "/"

#tryexcept condition for socket object creation
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Creation Success")
except socket.error as err:
    print("Socket Creation Failed. Error %s" %(err))

# default port for socket
port = 80

#tryexcept for hostname/ip creation
try:
    host_ip = socket.gethostbyname(hostname)
except socket.gaierror:
    print ("Host Connection Error")
    exit()

# connecting to the server
s.connect((host_ip, port))
print(f"Connection Established to {hostname}")

# Request the HTML for this web page:
request = f"GET {path} HTTP/1.1\r\nHost: {hostname}\r\n\r\n"
s.send(request.encode('utf-8'))

#receive the response
response = b""
data = s.recv(1024)
response += data
s.close()

#format the response
header_end = response.find(b"\r\n\r\n")
body = response[header_end+4:]

# Write the body into a file
filename = f"www_{hostname[4:-4]}_com.html"
with open(filename, "wb") as file:
    file.write(body)
    
print(f"Saved response body to {filename}")