## SIMPLE WEB STACK ##

![](https://github.com/meriembenayad/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack.png)

### Issues with this infrastructure ###
#### Single Point of Failure (SPOF): ####
This infrastructure has a single server, so if it fails or experiences issues, the entire website becomes inaccessible.
A failure could be mitigated by adding redundancy, failover, or load balancing.

#### Downtime During Maintenance: ####
When maintenance is required, such as deploying new code, the web server (Nginx) may need to be restarted. This can cause temporary downtime. Strategies like rolling updates or hot-swappable components can minimize downtime.

#### Scalability: ####
This infrastructure may struggle to handle high traffic loads. To scale, you would need to consider load balancing, adding more servers, and optimizing the database to handle increased traffic efficiently.
