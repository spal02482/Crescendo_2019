from flask import Flask, render_template
import socket

import socket

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('home.html')
	

if __name__=='__main__':
	app.run(debug=True, port=4000)
	PORT = 2000
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('', PORT))
	s.listen(2)
	conn, addr = s.accept()
	print("Connected by", addr)