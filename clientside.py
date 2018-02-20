import socket


socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = []

operation = input(
    """
        Net-Centric Math Server
        
        Please select an operation to perform:
        1 - Addition   2 - Subtraction     3 - Multiplication
                    4 - Division    5 - Modulus
    """
)

message.append(str(operation))

input1 = input('please enter the first value: ')
input2 = input('please enter the second value: ')

message.append(str(input1))
message.append(str(input2))

message = ','.join(message)

socket.sendto(message, ('localhost', 5555))

result, server = socket.recvfrom(1024*4)
print('server result: ' + result)

socket.close();
