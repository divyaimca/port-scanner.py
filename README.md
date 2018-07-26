# port-scanner.py

Sometimes we need to check in remote servers if port is open or not. We use different tools like nmap, telnet, nc etc.

But in most of the cases we need to install various tools in platforms to run these.

So I created one small port scanner tool that using python socket, which comes with python and we dont need to install extra modules for it.

It works perfectly, irrespective of the platform, windows, linux unix, macos etc.


It can be modified further to automate large number of target and port inputs.

Usage :
Give the inputs as list as below

python port-scanner.py

Enter list of target IPs: ["127.0.0.1","192.168.0.100"]
Enter list of ports: [123,22,23,80]

Target Host: 127.0.0.1 TCP Port: 123 status : closed.
Target Host: 127.0.0.1 TCP Port: 22 status : open.
Target Host: 127.0.0.1 TCP Port: 23 status : open.
Target Host: 127.0.0.1 TCP Port: 80 status : closed.
Target Host: 192.168.0.100 TCP Port: 123 status : open.
Target Host: 192.168.0.100 TCP Port: 22 status : closed.
Target Host: 192.168.0.100 TCP Port: 23 status : closed.
Target Host: 192.168.0.100 TCP Port: 80 status : open.


