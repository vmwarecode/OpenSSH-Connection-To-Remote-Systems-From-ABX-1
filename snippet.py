def handler(context, inputs):
    import paramiko

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # set variables
    target_server = "192.168.100.30"
    Username = "administrator@mydomain.lan"
    Password = "T0pSecr3t!"
    
    # Command to run on the target
    exec_command = "ipconfig.exe /all"
    
    # Connect to target using username/password authentication.
    ssh.connect(hostname=target_server, username=Username, password=Password, look_for_keys=False)
    
    # Run command.
    (ssh_stdin, ssh_stdout, ssh_stderr) = ssh.exec_command(exec_command)
    output = ssh_stdout.readlines()
    
    # Close connection.
    ssh.close()
    
    outputs = {'output': output}
    print(outputs)
    return outputs