Distributed Web Infrastructure
Description
This is a distributed web infrastructure can improve performance and reliability of a website rather than hosting everything on a single server. by distributing some of the load to a replica server with the aid of a server responsible for balancing the load between the two servers (primary and replica).

Round robin selection: Servers in this algorithm are selected sequentially.  When using this algorithm, the load distributor directs the first request to the first server in its list, then when the second request arrives, it directs it to the next server, and so on until it reaches the last server in the list and returns to the first.

 Least connections: This algorithm is recommended when connection sessions take a long time.  In this case, the distributor chooses the server with the fewest active connections.

 According to the source: When using this algorithm, the load distributor chooses the server that will answer the request based on the source IP address, for example;  Visitor's IP address.  Using this algorithm means that requests from a particular visitor will always be directed to the same server. For example, if the Primary MySQL database server is down, the entire site would be unable to make changes to the site (including adding or removing users). The server containing the load balancer and the application server connecting to the primary database server are also SPOFs.
Security issues.
The data transmitted over the network isn't encrypted using an SSL certificate so hackers can spy on the network. There is no way of blocking unauthorized IPs since there's no firewall installed on any server.
No monitoring.
We have no way of knowing the status of each server since they're not being monitored.
