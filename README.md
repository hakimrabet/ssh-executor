# ssh-executor
execute command via ssh and looking for some line by paramiko module in python

## Command in linux for execute it

    chmod +x sshExecutor 

    python sshExecutor [host-address] [username] [password] [COMMAND] [search-line]
or
                  
    ./sshExecutor [host-address] [username] [password] [COMMAND] [search-line]


[host-address]  --> ip address of host that you want to connect it ex.10.10.10.1

[username]      --> username for ssh ex. admin

[password]      --> password for ssh ex. 123

[COMMAND]       --> command that you want to execute after connect to ssh ex in cisco switch. "do-exec show ip interface brief"

[search-line]   --> looking for what in out put of that command you execute ? ex. "GigabitEthernet1/0/13"

    ./sshExecutor 10.10.10.1  admin 123 "do-exec show ip interface brief" "GigabitEthernet1/0/13"

# output 
    GigabitEthernet1/0/13  unassigned      YES unset  up                    up 
