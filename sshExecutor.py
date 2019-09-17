#!/usr/bin/env python
import paramiko;
import sys;

if(len(sys.argv)<2):
    print("give me input argument");
    print("python sshExecutor [host-address] [username] [password] [COMMAND] [search-line]");
else:
    HOST_ADDRESS = sys.argv[1];
    USERNAME = sys.argv[2];
    PASSWORD = sys.argv[3];
    COMMAND = sys.argv[4];
    SEARCH_LINE = sys.argv[5];
    client = paramiko.SSHClient();
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy());
    # client.connect('192.168.1.3',22, 'kayer','kayer')
    client.connect(HOST_ADDRESS,22,USERNAME,PASSWORD,look_for_keys=False);
    stdin, stdout, stderr = client.exec_command(COMMAND);
    # output=stdout.read().decode('utf-8');

    # print(output);

    for line in stdout:
        if SEARCH_LINE in line:
            print(line.strip('\n'))

    client.close();
