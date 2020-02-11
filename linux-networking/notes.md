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