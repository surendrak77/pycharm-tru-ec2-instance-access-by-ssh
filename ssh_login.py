import paramiko
user_name="root"
passwd="P@ssw0rd"
ip="54.235.14.139"
print "Please wait,creating ssh client.."
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print "Please wait,connecting with remote server"
ssh_client.connect(hostname=ip,username=user_name,password=passwd)
cmd="pcs cluster start --all "
print "Please wait, Executing command on remote server"
stdin,stdout,sterr=ssh_client.exec_command(cmd)
print "Successfully excute command on remote server. "
stdout=stdout.readlines()
print stdout