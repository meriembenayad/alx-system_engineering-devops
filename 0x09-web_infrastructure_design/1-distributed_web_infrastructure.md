## DISTRIBUTED WEB INFRASTRUCTURE ##

![](https://github.com/meriembenayad/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure.png)

### Issues with this infrastructure ###
#### Single Point of Failure (SPOF): ####
The Load Balancer is a potential SPOF. If it fails, traffic cannot be distributed. To mitigate this, you can consider setting up a secondary load balancer with failover mechanisms.

#### Security Issues: ####
This infrastructure lacks key security measures. To address this:
* Implement a firewall to control incoming traffic.
* Enable HTTPS to secure data in transit using SSL/TLS certificates.

#### No Monitoring: ####
Without monitoring, it's challenging to detect and respond to issues. Implement monitoring solutions to track server health, performance, and security, and set up alerting mechanisms for rapid issue resolution.
