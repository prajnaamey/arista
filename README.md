# Exploring Arista's vEOS and eAPI

## Getting Started

### Setting up Arista vEOS 4.20

1. Get the Arista's vEOS, Aboot disk image from Arista's Software Downloads. Setup your Virtual Machine. <br>
Follow: https://itmug.wordpress.com/network/arista-networks/install-arista-eos-in-a-vm/

2. Setup the Switch <br>
Follow: https://www.arista.com/assets/data/pdf/user-manual/um-eos/Chapters/Initial%20Configuration%20and%20Recovery.pdf <br>
Follow: https://eos.arista.com/building-a-virtual-lab-with-arista-veos-and-virtualbox/

3. Setup eAPI on the Arista Switch <br>
Follow: http://packetpushers.net/arista-eapi/ <br>

## Basic Topology:

1. Setup a Ubuntu Server 
+ Setup a Host-Only Network (Private)
+ Setup a NAT (to connect to the Internet)

2. Setup a Arista Switch 
+ Setup a Host-Only Management Interface

```

Apple MacBook
-----------------------------------------------------------------------------------------------
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|       VM                                               VM                                   |
| ________________                                  _____________  ens33                      |
| | Arista eVOS-1 |                                 | Ubuntu     | 172.16.129.130/24          |
| ________________                                  | 16.04      |---------------- NAT -------|----- Internet 
|        |                                          |____________|                            |
|        | Management                                    |                                    |
|        | 10.10.10.11/24                                | ens38                              |
|        |                                               | 10.10.10.10/24                     |
|        |                                               |                                    |
| _____________________________________________________________________________               |
|                    Host-Only Virtual Private Network                                        |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
-----------------------------------------------------------------------------------------------
```

