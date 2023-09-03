# Here I am here smtp python

import smtplib

def prompt(prompt):
    return input(prompt).strip()

fromadd = prompt("From: ")
toaddrs = prompt("To: ").split()
print("Enter your message: ")


msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromadd, ", ".join(toaddrs)))
        
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break

print("Message length is", len(msg))

server = smtplib.SMTP('localhost')
server.set_debuglevel(1)
server.sendmail(fromadd, toaddrs, msg)
server.quit()