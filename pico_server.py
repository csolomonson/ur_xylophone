import socket
import song
#import threading
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER_IP = '10.30.21.200'
PORT = 8000

server.bind((SERVER_IP,PORT))
server.listen(0)
print(f'listening on {SERVER_IP}:{PORT}')

client_socket, client_address = server.accept()
print(f'Accepted connection from {client_address[0]}:{client_address[1]}')

def buttons_encode(n):
    #n from 0 to 15
    p = 15
    ans = [0]*p
    
    for i in range(p):
        if n >= 2**(p-i-1):
            ans[i] = 1
            n -= 2**(p-i-1)
    return ans

SONG_TO_PLAY = song.RICK
current_note = 0

while True:
        request = client_socket.recv(1024)
        request = int(request.decode('utf-8'))
        #play_note(request) #NOT YET IMPLEMENTED
        if request = SONG_TO_PLAY[current_note]:
            if current_note < len(SONG_TO_PLAY):
                current_note += 1
            else:
                current_note = 0
            client_socket.send(SONG_TO_PLAY[current_note])
        
        print("RECV>> " + str(request))
        


    


          
