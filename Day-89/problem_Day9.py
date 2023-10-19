# Here I am showing Problem Solve Day 9

# SSH-Based Automation with Paramiko:
# Implement a solution using paramiko to automate SSH-based tasks, such as running commands on remote servers or copying files securely. This is valuable for tasks like server maintenance and administration.

import paramiko

# Define the SSH server details
ssh_host = '192.168.0.7'
ssh_port = 22
ssh_user = 'root'
ssh_password = '1234'  # For SSH password authentication

# Define the local and remote paths for file transfer
local_file_path = 'data.txt'
remote_file_path = '/home/'

# SSH connection and command execution
try:
    # Create an SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the remote server
    ssh_client.connect(ssh_host, ssh_port, ssh_user, ssh_password)

    # Run a command on the remote server
    stdin, stdout, stderr = ssh_client.exec_command('ls -l')

    # Print the command output
    print('Remote Server Output:')
    for line in stdout:
        print(line.strip())

    # Copy a file to the remote server (you can use sftp.put() for file upload)
    sftp = ssh_client.open_sftp()
    sftp.get(remote_file_path, local_file_path)

    # Close the SSH and SFTP connections
    sftp.close()
    ssh_client.close()

except paramiko.AuthenticationException:
    print('Authentication failed, please check your credentials')
except paramiko.SSHException as e:
    print(f'SSH connection failed: {e}')
except Exception as e:
    print(f'An error occurred: {e}')
