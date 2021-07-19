import os 
os.system("sudo yum install docker -y")
os.system("sudo systemctl enable docker --now")
os.system("sudo cp /configure/kubernetes.repo  /etc/yum.repos.d/ ")
os.system("sudo yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes")
os.system("sudo systemctl enable --now kubelet")
os.system("sudo kubeadm config images pull")
os.system("sudo cp /configure/daemon.json  /etc/docker/")
os.system("sudo systemctl restart docker ")
os.system("sudo yum install iproute-tc -y")
os.system("sudo  kubeadm init --pod-network-cidr=10.240.0.0/16 --ignore-preflight-errors=NumCPU --ignore-preflight-errors=Mem")
os.system("mkdir -p $HOME/.kube")
os.system("sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config")
os.system("sudo chown $(id -u):$(id -g) $HOME/.kube/config")
os.system("sudo kubectl apply  -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml")
print("K8s Master Is Succefully Created .......")
print("Now... ingress controller is configuring ... ")
os.system("sudo kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.48.1/deploy/static/provider/aws/deploy.yaml ")
