import socket

PORT = 2011
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(2)


conn, addr = s.accept()
print("Connected by", addr)

while True:
	print('> ', end='')
	choice = input()
	if (choice == "help"):
		print(" list\n", "shutdown [IP]\n", "restart [IP]\n", "screenshot [IP]\n",
			"notify [IP]\n", "quit\n")
		continue
	if (choice == "list"):
		print(addr)
	elif (choice == "shutdown"):
		conn.send("shutdown now".encode())
		conn.close()
	elif (choice == "restart"):
		conn.send("restart".encode())
		conn.close()
	elif (choice == "screenshot"):
		conn.send("gnome-screenshot -f screenshot.jpg".encode())
		data = conn.recv(100000)
		with open('screenshot1.jpg', 'wb') as file:
			file.write(data)
	elif (choice == "notify"):
		message = 'zenity '
		message += input()
		conn.send(message.encode())
	elif (choice == "quit"):
		conn.close()
		break