# Chpt.1 Network Topologies
- physical vs logical topologies
    - the "shape" of the network (physical: how the actual wires laid out, logical: the data 'flow' through the network)
    - one physical topo can have several logical topos

- full mesh topology
    - all devices connected to all others
    - full redundancy, but most expensive
    - most likely found in WAN (wide area network) than LAN (Local area network)

- partial mesh
    - all devices connected to at least two others in network

- Bus
    - all nodes connected to single main cable ("bus")
    - only one device can send signal at one time
        - determined by 'contention'
    - generally recommended for networks with <30 nodes
- Ring
    - like bus but connected in circle
    - packets of data move around the circle, each node has opportunity to send signal 
    - heavy traffic will slow network, and one damaged node can bring down the network

- Hierarchical star topology
    - most common LAN topology
    - all nodes connect to central hub/switch
    - one damaged node doesn't bring down system
    - can be effected by single point of failure, but only in central device, so troubleshooting simplified

- Hybrid Star topology
    - combines star topology with another
    - `physical-hybrid topology`: network with 2/+ phyical topologies
        - eg. switches linked as bus, nodes connected as star 
    - `physical-logical hybrid`: physically laid out in one topology, but functions in different logical pattern

- Point-to-Point/Multi-point topologies
    - point-to-point: two devices connected directly without intervention
        - used to connect two ends of a WAN connection, or a computer to a switch
    - point-to-multipoint: one device connected to several

- Connections (peer-to-peer vs client-server)
    - p2p: computer responsible for own security, each computer managed as separate device
        - typically only on very small networks
    - client server: all devices access resources through a central server
        - network management controlled by central server, with security built around that server
        - the server allows or restricts access to network resources