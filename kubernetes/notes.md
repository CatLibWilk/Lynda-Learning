# Kubernetes
def: software allowing for automation, deployment, scaling of applications on group or cluster of server machines
- Features
    - multi-host container scheduling
        - managed by `kube-scheduler`
        - assigns pods (containers) or nodes (hosts) at runtime
        - accounts for resources, quality of service, etc.
    - scalability
    - flexibility (plug and play architecture)
    - built-in application monitoring

## Chpt 2. Terminology
- master node: responsibly for overall management of cluster
    - three components: API server, scheduler (watches created pods without assigned node, then assigns to node), and controller manager (runs background threads that run tasks in cluster)
    - interact with master node with `kubectl` cli tool. 
        - kubectl has `kubeconfig` file with server information and authentication info to access API server. 
- worker nodes
    - communicate with master node, comm handled by kubelet process
        - kubelet checks if pods designated to node, executes pods, mounts/runs pod volumes and secrets, communicates node states back to master
- Docker
    - works with kubelet to run containers on nodes
- kube-proxy
    - network process and load balancer for service on a single worker node

- containers
    - containers are tightly coupled together in pods
    - pod is smallest unit that can be scheduled for deployment
        - share storage, linux namespace, and IP address