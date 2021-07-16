import os 
os.system("sudo yum install docker -y")
os.system("sudo systemctl enable docker --now")
os.system("sudo cp /configure/kubernetes.repo  /etc/yum.repos.d/ ")
os.system("sudo yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes")
os.system("sudo systemctl enable --now kubelet") 
os.system("sudo cp /configure/daemon.json  /etc/docker/")
os.system("sudo systemctl restart docker ")
os.system("sudo yum install iproute-tc -y")
os.system("sudo cp /configure/k8s.conf  /etc/sysctl.d/ ")

