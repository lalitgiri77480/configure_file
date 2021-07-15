import os 
os.system("sudo  kubeadm init --pod-network-cidr=10.240.0.0/16 --ignore-preflight-errors=NumCPU --ignore-preflight-errors=Mem")
os.system("mkdir -p $HOME/.kube")
os.system("sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config")
os.system("sudo chown $(id -u):$(id -g) $HOME/.kube/config")
os.system("sudo kubectl apply  -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml")
