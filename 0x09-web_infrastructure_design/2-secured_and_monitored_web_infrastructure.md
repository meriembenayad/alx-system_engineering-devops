##SECURED AND MONITORED WEB INFRASTRUCTURE##

![](https://github.com/meriembenayad/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.png)

###Issues with this infrastructure###
####SSL Termination at Load Balancer:####
SSL termination at the load balancer can be an issue because it could potentially expose unencrypted traffic within your internal network. If an attacker gains access to your internal network, they could eavesdrop on this unencrypted traffic.

####Single MySQL Server for Writes:####
Having only one MySQL server capable of accepting writes is a single point of failure. If this server goes down, your entire application could become unavailable.

####Same Components on All Servers:####
Having servers with all the same components (database, web server and application server) might be a problem because it does not allow for horizontal scaling. If one component of your application needs more resources (e.g., the database), you can’t just add more of that type of server.
