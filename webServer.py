# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection
    
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start - accept a connection   #Fill in end
    
    try:
      message = connectionSocket.recv(1024).decode() #Fill in start - receive the request message from the client   #Fill in end
      filename = message.split()[1]
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], 'rb') #Fill in start - open the file requested by the client. Remember to remove the leading "/" from the filename!   #Fill in end
      
      

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
      #Fill in start 
      status_line = b"HTTP/1.1 200 OK\r\n"
      server_header = b"Server: PythonWebServer/1.0\r\n"
      connection_header = b"Connection: close\r\n"

              
      #Content-Type is an example on how to send a header as bytes. There are more!
      outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"


      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
      headers = status_line + server_header + connection_header + outputdata + b"\r\n"
      #Fill in end

      body = b""
               
      for i in f: 
        body += i #for line in file
      #Fill in start - append your html file contents #Fill in end 
        
      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!
      connectionSocket.sendall(headers + body) #Fill in start - send the headers and the body of the response to the client   #Fill in end

      # Fill in start


      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      error_status_line = b"HTTP/1.1 404 Not Found\r\n"
      error_server_header = b"Server: PythonWebServer/1.0\r\n"
      error_connection_header = b"Connection: close\r\n"
      error_outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"
      error_headers = error_status_line + error_server_header + error_connection_header + error_outputdata + b"\r\n"
      error_body = b"<html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1></body></html>"
      connectionSocket.sendall(error_headers + error_body)

      #Fill in end


      #Close client socket
      #Fill in start

      #Fill in end

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
