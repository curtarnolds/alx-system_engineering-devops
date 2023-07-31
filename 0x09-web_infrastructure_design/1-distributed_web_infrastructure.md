# 1. Distributed web infrastructure

* Image (<https://imgur.com/a/R9UL67Z>)
* For every additional element, why you are adding it:
  * Load balancer
    * Distributes the traffic between the two servers so neither is overloaded. It also ensures availability in case one server is offline
    * Masks the actual IP address of the servers. This provides a form of security
* What distribution algorithm your load balancer is configured with and how it works: It distributes traffic between the two servers
* Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both: Load balancer is enabling an active-active setup. With active-active, the two servers are online and in use simultaneous while only one server will be in use with the other on standby in the case of the active-passive setup
* How a database Primary-Replica (Master-Slave) cluster works: The primary database allows read and write while the replica sychronizes the data from the primary cluster and only allows read.
* What is the difference between the Primary node and the Replica node in regard to the application: Primary node allows read and write but  the replica node only allows read.
* Where are SPOF: SPOF can be found on the load balancer
* Security issues (no firewall, no HTTPS): There is no firewall on the load balancer and servers
* No monitoring: There is no monitoring
