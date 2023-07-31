# 2. Secured and monitored web infrastructure

* Link (<https://imgur.com/a/7ynqDJ1>)
* For every additional element, why you are adding it:
  * Firewalls filter traffic to and from a device
  * Monitoring checks for anormalies. Could be hardware or software
* What are firewalls for: Firewalls prevent unauthorized access
* Why is the traffic served over HTTPS: To prevent interception by a third part
* What monitoring is used for: Checks the condition of server components
* How the monitoring tool is collecting data: A client collects the data and sends it to the monitoring software
* Explain what to do if you want to monitor your web server QPS:
  * Collect websever data
  * Set an alarm to be triggured whenever QPS gets out of control
* Why terminating SSL at the load balancer level is an issue: Traffic will not be secure in transit between the servers and the loadbalancer.
* Why having only one MySQL server capable of accepting writes is an issue: Writing will be disabled once the master goes down
Why having servers with all the same components (database, web server and application server) might be a problem:
  * When one component of the server is offline the whole server will be affected
  * Demand might not be equal for all three components at any time
