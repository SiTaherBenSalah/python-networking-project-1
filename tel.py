import getpass
import telnetlib
Host="192.168.1.120"
user=input("enter your account name")
password=getpass.getpass()
tn=telnetlib.Telnet(Host)
tn.read_until(b"username")
tn.write(user.encode('ascii')+b"\n")
if password :
    tn.read_until(b"password")
    tn.write(password.encode('ascii')+b"\n")
tn.write(b"enable")
tn.write(b"bayern")
tn.write(b"conf t")
tn.write(b"hostname taher")
tn.write(b"exit\n")
tn.write(b"exit\n")
tn.write(b"mrigl")
print(tn.read_all.decode('ascii'))