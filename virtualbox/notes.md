## Chpt. 1 VirtualBox Software
- fixed vs. dynamic disk: dynamic only takes up space on host as needed, fixed takes up a set amount from outset

## Installing Linux VM
 - guest additions
    - check where guest additions disk is mounted with `mount` command, looking for `VBOXADDITIONS`
    - cd to that location, and run the `autorun.sh` script

## Networking Modes
- NAT (Default): allows guest machine to reach internet, but cant connect with other VMs, host, or other machines on network
- NAT Network: creates virtual network for guests to share
- Bridged: connects guest machine to same network as host
- Internal: guests can communicate with eachother but not with host or internet
- Host only: like internal, but including the host machine

## Port Forwarding
- mapping port from guest to port from host (in NAT mode)
- Port forwarding settings are under `Network Settings`
- host port needs to be above 1024 on linux hosts, anything on windows

## Command-line options for VMBox
- `VBoxManage` is main one

## Modifying Disks and Memory
- can add memory to existing VM through settings (limited by host resources)
- adding storage space
    -  in Settings>storage, can add additional drives to SATA bus by clicking plus-disc icon
    - new disc wont initially have a file system on it, so wont appear in directory on machine, so need to create
        - find new disc with `fdisk -l` command
        - when you find the new disc (eg. `/dev/sdb`), use `fdisk` again to create a partition
            - `sudo fdisk /dev/sdb` , enter `n` when prompted to create new partition, and follow prompts to create, ending with `w` command entered to write changes to disk.
        - finally, create a filesystem in new partition
            - `sudo mkfs.ext4 path/to/partition`
                - eg. `sudo mkfs.ext4 /dev/sdb1`

    - to modify an existing disk/partition, need to use vbox command line interface outside of the VM (ie. with machine shut down, through host terminal)
        - with `modifyhd` command
        - then in machine, unmount the partition: `sudo unmount /dev/sbd1`
        - use `parted` tool to modify partition: `sudo parted /dev/sdb`
        - in the parted tool, use command `resizepart [partition no.]` eg. `resizepart 1`
        - extend filesystem:
            - `e2fsck -f /dev/sbd1`
            - `resize2fs /dev/sbd1`