import socket


def get_host_name():
    host_name = socket.gethostname()
    return host_name


# get hostname
host_name1 = get_host_name()
print("Host name of the machine is: "+host_name1)
