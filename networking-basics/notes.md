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
    - client server: all devices access res ources through a central server
        - network management controlled by central server, with security built around that server
        - the server allows or restricts access to network resources

- CSMA/CD and CSMA/CA: two common ways that devices access the physical network
    - both contention-based network access
    - CSMA/CD: Carrier Sensing Media Access/Collision Detection
        - method most commonly used by wired ethernet
        - each node listens for traffic, will release a packet if hear's nothing
        - if two packets released at same time, `collide`, data destroyed, power spike heard by all other devices on the network
            - when hear a collision, all nodes start internal clock set to random milliseconds
                - when this runs down all nodes can attempt to send new transmissions.

    - ` `/Collision Avoidance
        - most common used in wifi
        - device releases a warning packet, alerting other nodes about upcoming transmission
        - collision of warning packets handled same as CSMA/CD
    
    - Internet, Intranets, Extranet
        - internet != WWW (www = service running on top of internet)
        - intranet: Privately accessible of infrastructure
        - extranet: privately held WAN architecture, but may allow access for fee (e.g. AWS)

# Chpt. 2 Network Implementations
    - WANs and MANs
        - WAN: Wide-area Network (e.g. the internet)
            - can be smaller networks linked to a larger one
            - connected with routers and switches

        - MAN: Metropolitan-area Network
            - uses same tech as WAN, but covers much smaller area
            - term falling out of use, replaced with wider application of WAN 
    
    - LAN, WLAN, PAN
        - LAN: Local area network
            - limited in size (room up to a building generally)
            - usually use twisted-pair cable to connect devices
            - standards recognize hierarchical star topology 
        - WLAN: Wireless LAN

        - PAN: Personal Area Network
            - typically connected via bluetooth technology
            - limited range of ~30 feet

    -SCADA/ICS and Medianet technologies
        - SCADA/ICS: Supervisory Control and Data Acquisition / Industrial Control System
            - both refer to technologies used to control industrial application
            - SCADA: systems that span large geographical areas 
            - ICS: refers to smaller systems, e.g. control for a factory or sth,
        
        - Medianet: networks optimized for distributing large video applications or similiar tech
            - uses smart bandwidth detection to adjust for higher/lower bandwidth devices

# Chpt 3 OSI Model
    - OSI: Open Systems Interconnection Reference Model
    - 7 Layers: Application, Presentation, Session, Transport, Network, Data Link, Physical layers
        - "All People Seem To Need Data Processing" (pneumonic)
    
    - 1. Physical Layer
        - concerned with physical transmission of data across network
            - defines encoding methods for tranporting data, how bits are encoded on media
            - defines specifications for media usage (what kinds permitted for different devices)
            - defines how physical connections made between media
    
    - 2. Data Link Layer
        - provides error-free transmission from node to another over physical media
        - in charge of degree of traffic-control
        - responsible for frame acknowledgement
        - can detect and recover from errors in physical layer
        -responsible for frame delimiting (defining boundaries of the frame)
        - error checking: checks recieved frames for data integrity
        - determines when a node is allowed to use physical media
    
    - 3. Network Layer
        - controls operations of the subnetwork its located on
            - determines best physical path for data
                - uses network conditions and priority of service as metrics 
            - function provided
                - routing: routes frames along best paths
                - subnet traffic control: allows routers to send instructions to eachother
                - frame fragmentation: determines size of frame used by routers downstream, if necessary will break up data to  meet this size 
                - logical-physical address mapping
                - subnet usage accounting: tracks frames as they're forwarded by subnet-intermediate system
            - layer builds specialized headers used by network layer on other devices to route packets
                - these relieve higher OSI layers from needing to know transmission and switching data
            - network layer users protocols on lower layers to send data to destinations separated by intermediate nodes
                - data sent from intermediate node to next intermediate node 

    - 4. Transport Layer
        - ensures message delivery without loss or duplication
        - relieves higher protocols of concern for transfer of data 
        - Message segmentation: accepts messages from session layer above in entirety, splits into smaller units to be sent
            -  imposes message size limits on network layer protocols below
            - prepares header for each unit
                - contain start and end flags
                - contains sequence information
            - reassembles once its reached destination
        - other functions
            - message acknowledgement
            - message traffic control
            - session multiplexing: ability to break incoming data into different datastreams (sessions), so transport layer sorts messages to correct session
    
    - 5. Session Layer
        - responsible for establishing sessions between processes running on different computers.
            - to accomplish, responsible for:
                - session establishment, maintenence, termination
                    - allows processes to est. connection, use connection
                - session support
                    - provides security for connection
                    - provides name recognition to keep different sessions separate
    
    - 6. Presentation Layer                    
        - responsible for how data formatted to be presented to application layer
        - translator for network
        - translation functions
            - character-code translation
            - data conversion
        - responsible for data compression and encryption
    
    - 7. Application Layer
        - serves as window to access network services

    - Encapsulation/De-encapsulation
        - each OSI layer adds a header to data, and creates a unit of data called encapsulation unit
            - process of moving data down the model
            - process of moving data up the model (physical to application) is de-encapsulation
            - for Application to session layers, unit called data
            - transport layer converts data to segment
            - network layer converts segments to packets
            - data layer converts packets to frames 

# Chpt. 4 TCP/IP Model
    - The TCP/IP Suite
        - group of protocols designed to work together to send data over the network
            - TCP (Transport Control Protocol)
            - IP (Internet Protocol)
    
    - TCP/IP Model
        - vs. OSI: is reduced version of TCP/IP
        - 4 Layers
            - Application
            - Transport
            - Internet
            - Network Interface
        
        - Application Layer
            - defines protocols, services and processes that allow programs and users to interface with the network 
            - define how programs interface with the transport layer services to use the network 
            - common protocols
                - HTTP
                    - used to transport webpages
                - telnet
                    - used to remote access other computers
                - FTP
                - TFTP: trivial file transfer protocol
                - SNMP
                    - Simple Node Management Protocol
                - DNS
                    - takes human-useable URLS and convert to IP addresses
                - SMTP
                    - used by email to transfer messages
        - Transport Layer
            - provides communication session management between computers
            - defines level of service and status of connections used when transporting data
            - common protocols: TCP, UDP (User datagram protocol), RTP (Realtime Protocol)
        
        - Internet Layer
            - responsible for converting data to IP datagram ("packet")
                - header contains source and destination information
            - uses header info to move packet across the network
            - common protocols: IP Protocol, ICMP (internet control message protocol), ARP (Address resolution)
        - Network Interface/Access Layer
            - specifies how data physically sent through network
            - specifies how bits are electronically signalled by hardware 
            - defines how hardware interaces with network medium
            - standards defined by network layer:
                - ethernet
                - FDDI (fiber optic standard for WAN)
                - RS232 (defines serial interfaces and comm ports)

# Chpt 5 Network Devices
    - NIC (Network Interface Controller)
        - allows computer to gain access to hardware of network
        - needs to match metdia technology
        - need to match speed used on network, architecture of network
    - Hubs
        - mostly falling out of favor in preference to switches
        - function as bus, 
    - Bridges
        - used to break up large network into smaller segments
        - forerunner to switch
        - works on layer 2 of OSI
        - reads frames coming into it, reducing traffic on network through division
    - switches
        - used to connect multiple computers together
            - work primarily on layer 2 of OSI
        - basic switch: essentially a multiport bridge
            - can segment a network into `collision domains`
                - uses ports to set up point-to-point connection between devices connection to affected ports
            - also used to convert media from one type to another (fiber in to switch, twisted pair going out)
    - routers
        - move data around large networks
            - work on layer 3, 4 of OSI
        - are programmable
            - must configure interfaces
            - have to be told what networks they're connected to
            - must define what is to be let through routers 
    - access points
        - devices allowing computers to gain access to larger network
        - can be wired or wireless (WAP - wireless access point)
