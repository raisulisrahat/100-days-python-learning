# Here I am showing DevOps Project Day 3

import difflib

nginx_server_conf = "server.conf"

with open(nginx_server_conf, 'r') as files:
    server_contents = files.readlines()

differ = difflib.Differ()
diff = list(differ.compare(server_contents, 'b'))

df = any(line.startswith('- ') or line.startswith('+ ') for line in diff)

if df:
    print("Drift detected in Nginx configuration:")
    for line in diff:
        if line.startswith('- ') or line.startswith('+ '):
            print(line)

else:
    print("No configuration drift detected in Nginx configuration.")
