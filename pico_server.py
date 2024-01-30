import socket
import song
#import threading
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

NOTES = ['G0', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2','G2']

ROBOT_IP = '10.30.21.100'
ROBOT_PORT = 30002

ur.bind((ROBOT_IP, ROBOT_PORT))

def robot_init():
    with open('xylo_init.txt', 'r') as f:
        for cmd in f.readlines():
            ur.send(cmd)

def play_note(note):
    notes = ['G0', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2','G2']
    note_name = NOTES[note-1]
    ur.send(f'movej({note_name}_q, a=8, v=6')
    print(ur.recv(1024))
    #ur.send('movej(pose_add(get_target_tcp_pose(), pose_sub(bonk_to_p, bonk_from_p)), a=52.35987755982989, v=6.283185307179586)')
    
    
    
    

SERVER_IP = '10.30.21.200'
PORT = 8000

server.bind((SERVER_IP,PORT))
server.listen(0)
'''print(f'listening on {SERVER_IP}:{PORT}')

client_socket, client_address = server.accept()
print(f'Accepted connection from {client_address[0]}:{client_address[1]}')'''

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

robot_init()

while True:
        '''request = client_socket.recv(1024)
        request = int(request.decode('utf-8'))
        #play_note(request) #NOT YET IMPLEMENTED
        if request = SONG_TO_PLAY[current_note]:
            if current_note < len(SONG_TO_PLAY):
                current_note += 1
            else:
                current_note = 0
            client_socket.send(SONG_TO_PLAY[current_note])
        
        print("RECV>> " + str(request))'''
        note = int(input())
        play_note(note)
        
        


    


          
