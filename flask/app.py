from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route("/")
def main():
    return f"Container ID: {socket.gethostname()}, Worker ID: {os.getpid()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

