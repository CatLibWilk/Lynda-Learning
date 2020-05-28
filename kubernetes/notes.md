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
- components overview
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
- nodes
    - serves as worker machine in K8 cluster.  Can be physical or virtual machine
    - needs: kubelet running, container tooling (docker), kube-proxy running, process like `supervisord` to handle restarting and etc.
- pods
    - simplest unit you can interact with. Represents one running process in cluster
        - contains: docker app container, storage resources, unique network IP, operations governing how container runs

- Controllers
    - types: 
        - `ReplicaSets`: ensures specified # of replicas of a pod are running (can only use within deployment )
        - `DaemonSets`: ensure all nodes run copy of specified pods
        - `Deployments`: provides declarative updates for pods and repSets. Deployment manages -> repSet manages -> pod
        - `Jobs`: supervisor process for pods carrying out batch jobs. Run indiv processes that run once and complete successfully
        - `services`: allows for communication between one set of deployments and another

- Labels, selectors, and namespaces
    - labels: key/value pair attached to objects s.a. pods, services, deployments
    - selectors: allow you to select sets of objects based on labels
    - namespaces: 
- kubelet and kube-proxy
    - kubelet: kubelet uses `podspec` (YAML file describing a pod) and ensures containers described in podspec are running and healthy
    - kube-proxy: reflects services as defined on each node, handles forwarding across several backends
        - three modes: userspace, iptables, and ipvs

## Chpt. 3 Kubernetes Setup
- install/have running docker, a hypervisor (virtualbox), kubectl, minikube
- hello world startup
    - start minikube: `minikube start`
        - check vbox and minikube are communicating with `kubectl get nodes`
    - pull image and run: `kubectl run [name] --image=karthequian/helloworld --port=80`
    - expose service: `kubectl expose pod [name] --type=NodePort`
    - bring up service in browser: `minikube service [name]`
- starting an application from deployment yaml file: `kubectl create -f filename.yml`

## Chpt. 4 Labels, Upgrades, Healthchecks
- add labels: `kubectl label [podname] [label] --overwrite`
    - eg. `kubectl label helloworldapp app=helloworld --overwrite`
- delete labels: `kubectl label [labelname]-`
- search by label: `kubectl get pods --selector [labelname]=[labelval]`
    - search with several selectors: `kubectl get pods --selector [labelname]=[labelval],[labelname]=[labelval]`
        - use `!=`for NOT in searching
    - IN selector
        - `kubectl get pods --selector [labelname] in (lorange, hirange)`
            - eg. `kubectl get pods --selector 'release-version in (1.0,2.0)'`