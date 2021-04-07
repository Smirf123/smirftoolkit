import os
TWHITE = '\033[37m'
TGREEN =  '\033[32m'

print (TGREEN + "Welcome to the Smirf Multi Tool for Cybersecurity" , TWHITE)
print (TGREEN + "This was built by Smirf123 Development, Smirf123 is not responsible for your use of the tool" , TWHITE)



def menu():
    print (TGREEN + "Follow the following options for the tool you want to use" , TWHITE)
    print (TGREEN + "1:Ping" , TWHITE)
    print (TGREEN + "2:NMap" , TWHITE)
    print (TGREEN + "3:NetCat" , TWHITE)
    print (TGREEN + "4:Quit", TWHITE)
    val = input("Enter your value: ")

    if val=="1":
        ping()
    elif val=="2":
        nmap()
    elif val=="3":
        netcat()
    elif val=="4":
        print (TGREEN + "Thank you for using the Smirf Multi Tool, Goodbye", TWHITE)
        quit()


def ping():
    ip = input("Enter the IP you want to ping: ")
    os.system(f"ping {ip}")
    print(TGREEN + "Thank you for using the Smirf toolkit", TWHITE)
    menu()

def nmap():
    ip = input("Enter the hostname you want to nmap: ")
    print (TGREEN + "Select from the following options" , TWHITE)
    print (TGREEN + "1:Basic Port Scan" , TWHITE)
    print (TGREEN + "2:Add a service scan for a certain port" , TWHITE)
    print (TGREEN + "3:Add Verbose" , TWHITE)
    print (TGREEN + "4:Quit to Menu", TWHITE)
    baseopt = input("Enter flag you want to add to the nmap session: ")
    if baseopt=="1":
        os.system(f"nmap {ip}")
        print(TGREEN + "Thank you for using the Smirf toolkit", TWHITE)
        menu()
    elif baseopt=="2":
        portus = input("Enter the port/portrange you want to scan: ")
        os.system(f"nmap -sV {ip} -p {portus}")
        print(TGREEN + "Thank you for using the Smirf toolkit", TWHITE)
        menu()
    elif baseopt=="3":
        os.system(f"nmap -v {ip}")
        print(TGREEN + "Thank you for using the Smirf toolkit", TWHITE)
        menu()

    elif baseopt=="4":
        menu()
def netcat():
    ip = input("Enter the hostname you want to netcat: ")
    ports = input("Enter the port you want to connect to: ")
    os.system(f"nc {ip} {ports}")
    print(TGREEN + "Thank you for using the Smirf toolkit", TWHITE)
    menu()

menu()