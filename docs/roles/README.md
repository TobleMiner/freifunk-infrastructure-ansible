Role documentation
==================

This document provides a rough overview of all the roles available for deployment.

# apt_upgrade
This role ensures all packages that can be safely upgraded are up to date and reboots the system in case of kernel version changes.

# batman_adv_dkms
This role ensures that the correct version of the B.A.T.M.A.N. kernel module and user space tools are installed and the batman_adv kernel module is loaded.

# bgp4
This roles sets up IPv4 BGP. The setup includes automatic peering with all devices in the bgp4 group.

# bgp6
This roles sets up IPv6 BGP. The setup includes automatic peering with all devices in the bgp6 group.

# ffnw
This role is a meta role that sets up common requirements for ffnw4 and ffnw6.

# ffnw4
This role sets up an IPv4 peering with ffnw including IPv4 exit setup with NAT.

# ffnw6
This role sets up an IPv6 peering with ffnw including IPv6 exit.

# gateway
This role is the base role for setting up a gateway. It combines setup of required network interfaces, services and deployment of firewall rules.

# gateway_mss_clamp
This role is a hack that clamps the mss of tcp connections on the mesh interface as a fix for broken path MTU discovery.

# mesh_vpn
This role sets up a fastd mesh vpn endpoint.

# mesh_vpn_ci_access
This role sets up a user for automated deployment of mesh vpn peer keys and allows the ci system to push repo updates via a preconfigured ssh key.

# noc_keys
This role retieves a set of ssh public keys from a git repo and creates users with administrative priviliges that can be accessed by those keys.
