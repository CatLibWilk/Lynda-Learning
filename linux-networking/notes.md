## Chpt.1 Configuring Network Settings
- 2 ways to configure
    - Physical changes to config files at `/etc/network/interfaces` (interfaces is file not dir)
    - with `NetworkManager` 
        - use NM to create connections: groups of config settings for a device
        - uses `nmcli` command, which requires `apt install network-manager` (at least for the U16 I have on D.O.)
            - if need to install, need to `service NetworkManager start` as well
            - (working on D.O. droplet) = change `managed=false` to true in /etc/NetworkManager/NetworkManager.conf for devices to appear managed in output of `nmcli d`
- when configuring networks, can make static or dynamic
    - dynamic: IP assigned by DHCP (Dynamic Host Configuration Protocol)
    - static: unchanging address set by admin
    - clients usually use dynamic (with NetworkManager), servers static
- finding connection information
    - use `ip` command
    - `ip a`:
        - results named by `Predictable Network Interface Names` protocol
            - eno[number] eg. `eno1`: network device is "onboard" ie. built into mainboard
            - en[numbers_and_letters] eg. `enp0s1`: device is on different card or presented to system as such
                 - number refers to location on bus, eg for above, "slot 3 on PCI bus 0"
            - wl[numletter]: WLAN/Wifi
            - enx[number]: MAC address
        - following name is block of allcaps info eg `<BROADCAST,MULTICAST,UP,LOWER_UP>`
            - `UP` means interface is up, `LOWER_UP` underlying network is connect physically
            - `STATE [UP/DOWN]` a little further down the line indicates general status of connection
        - `ip -4 a` returns device info shortened to just the ipv4 address
        - `ip route` shows routes

- Dynamic Address configuration with NetworkManager
    - check managed devices: `nmcli d`
    - edit/create a connection: `nmcli c e [cname]` (without name, editor will create new connection)
    - delete a connection: `nmcli c delete [connection_name_in_double_quotes]`
    - creating a connection using DHCP
        - after cmd `nmcli c e [cname]`:
            - ipv4.method needs to be set to auto
            - add connection to device: `set connection.interface-name [adapter name]`
            - write cmd `save` 

- Static Address configuration
    - create net connection `nmcli c e`:
        - set type of connection
        - `set connection.id [name]`
        - `set connection.interface-name [adapter_name]`
        - change ipv4 settings:
            - `method` from auto to manual
            - set `ipv4.addresses` to new address
            - set `ipv4.gateway`
            - set `ipv4.dns` ex. google's `8.8.8.8`

- Configuring dynamic address manually (no NetworkManager)
    - open `/etc/network/interfaces`
    - add "stanza", definition of interfaces
        - ex:  
        auto enp0s3  
        iface enp0s3 inet dhcp  
          
        static:  
        auto enp0s3  
        iface enp0s3 inet dhcp  
        address 10.0.2.24/10  
        gateway 10.0.2.1  
    - `restart NetworkManager service` to prevent Manager from managing this device
    - `restart networking service`
    - `reboot` 

## Chpt. 2 Firewall and Routing
- ufw
    - firewall management in ubuntu through uwf (uncomplicated firewall)
        - rules
        - `ufw enable` starts firewall
        -  `ufw status verbose` to show current status of firewall
        - `ufw reject [port]` will reject connections to a given port
        - `ufw allow [port]` to allow on a port
        - `ufw delete [rule_name]` will delete a rule that's been added to the ufw table 
            - eg. `ufw delete allow 3000` will delete the `allow 3000` rule
        - `ufw allow proto tcp from [remote_ip_addr] to [local_ip_addr] port [portnumber]`
    - ufw has default rules at `/etc/ufw`
- packet forwarding
    - `gateway device` acts as intermediary for sending data between devices in-network and outside.
    - routing vs. forwarding
        - routing defines where packets intended for another network are sent
        - forwarding moves packets from one network interface to another (in same network)
    - linux machines can be configured to perform routing/forwarding tasks by enabling `ipv4_forwarding`
        - `sudo sysctl -w net.ipv4.ip_forward=1` to enable temporarily
        - uncommenting in the `/etc/sysctl.conf `file to permanently enable
- Addresses on Private Networks
    - 10.0.0/8, 72.16.0.0/12 and 192.168.0.0/16 ranges are reserved for devices on private networks
    - for information on private networks to get to the internet, networks use NAT (network address translation) to convert packet addresses between networks
    - NAT
        - converts packet addresses for different networks
        - firewall configured to use `masquerading`: to outside network, packets appear to come from router 
    - Setup
        - change firewalls default forwarding behavior at `/etc/default/ufw`: `DEFAULT_FORWARD_POLICY` from DROP to ACCEPT
        - to `/etc/ufw/before.rules` add:
            - *nat  
            :POSTROUTING ACCEPT [0:0]  
            -A POSTROUTING -s [PRIV_NET_IP] -O [DEVICE] -j MASQUERADE //eg. -A POSTROUTING -s 10.0.2.0/24 -o enp0s8 -j MASQUERADE  
            COMMIT  
            
- Routing Traffic
    - `ip route` command shows route info
        - eg. from DO Droplet:  
            default via 159.89.32.1 dev eth0 onlink  
            10.17.0.0/16 dev eth0  proto kernel  scope link  src 10.17.0.5  
            159.89.32.0/20 dev eth0  proto kernel  scope link  src 159.89.41.131  
        - default is the default route, line tells system to send traffic through the address using the `eth0` devive
    - create route (temporarily): ip route add [destination_address] via [route_address]
        - eg. `ip route add 10.0.3.0/24 via 10.0.2.6`
    - create route (permanent): add to `/etc/network/interfaces` for rule when the device comes up, like  
        - auto enp0s3...  
            up route add 10.0.3.0/24 via 10.0.2.6
    - create with NetworkManager
        - `nmcli connection modify [connection_name]`  
           `ipv4.routes "[destination_addr] [route_addr]`
    
    - dynamic routing
        - used on very large network where manual route changes are impractical
- Network Tunnels
    - est. connection between two devices through which traffic can be sent
    - three types: `IP-IP `(for ipv4 traffic), `SIT` (ipv6 traffic over ipv4 network), `GRE` (several traffic types over ipv4)
    - to set up, need:
        - both devices' IP address
        - create network device and assign an IP at each end
    - creating GRE tunnel in CLI
        - on router 1: `ip tunnel add [name] mode gre`, and give remote and local IP addresses
            - `ip link set [tunnel_name] up`
            - `ip address add [IP_address] dev [tunnel_name] to add address to newly reacted device
        - on router 2: do similar but reflecting locality of second router/network
    - creating GRE in `/etc/network/interfaces`
        - on both machines:
            - define interface  
                auto [tunnel_name]  
                iface [tunnel_name] inet static  
        - on router 1:
            - give address, add netmask, tell system to create tunnel at startup  
            address 10.1.0.1  
            netmask 255.255.255.0  
            pre-up ip tunnel add [tunnel_name] mode gre \  
            remote [IP] local [IP] ttl 255  
            post-down ip tunnel del[tunnel_name]
        - on router 2: same, but reflecting locality        

- Time Syncronization
    - systems typically get their time informatino from a time server on the internet using NTP (Network Time Protocol).
    - can set up time server on own network with `chrony` (`apt install chrony`)
        - cli command `chronyc`

- Monitoring Network Performance
    - `iftops` shows traffic per hose
    - `ifhogs` shows traffic per process
    