Another effective way to help prevent this even if you have root privs this can happen if a socket is not closed properly, here is a fix:

s=socket.socket( )
s.bind(("0.0.0.0", 8080))
while 1:
    try:
        c, addr = s.accept()
    except KeyBoardInterrupt:
        s.close()
        exit(0)
