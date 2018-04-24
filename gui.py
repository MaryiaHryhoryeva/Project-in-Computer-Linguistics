
import Tkinter as tk
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    root = tk.Tk()
    v = tk.IntVar()
    v.set(0)  # initializing the choice, i.e. Python

    languages = [
        ("Present Simple"),
        ("Present Continuous"),
        ("Present Perfect"),
        ("Present Perfect Continuous"),
        ("Past Simple"),
        ("Past Continuous"),
        ("Past Perfect"),
        ("Past Perfect Continuous"),
        ("Future Simple"),
        ("Future Continuous"),
        ("Future Perfect"),
        ("Future Perfect Continuous")
    ]

    def ShowChoice():
        message = str(v.get()+1)
        sock.sendall(message)


    tk.Label(root,
             text="""Choose the language to train:""",
             justify = tk.LEFT,
             padx = 20).pack()

    for val, language in enumerate(languages):
        tk.Radiobutton(root,
                      text=language,
                      padx = 20,
                      variable=v,
                      command=ShowChoice,
                      value=val).pack(anchor=tk.W)


    root.mainloop()

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
