import os 
os.system("sudo apt-get update")
os.system("sudo apt-get install docker.io")
os.system("sudo systemctl enable docker")
os.system("curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add")
os.system("sudo apt-add-repository 'deb http://apt.kubernetes.io/ kubernetes-xenial main' 
          ")
os.system("sudo apt-get install kubeadm kubelet kubectl")
os.system("sudo apt-mark hold kubeadm kubelet kubectl")
a=input("Enter the Host Name Eg:- Worker Node1")
os.system("sudo hostnamectl set-hostname {a}").format(a)
os.system("sudo cp /configure/daemon.json  /etc/docker/")
os.system("sudo systemctl restart docker ")
print("Enter the Key for join worker node to the master node")
