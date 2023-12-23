1Description
A simple web infrastructure that hosts a website that is reachable via (www.foobar.com.) There are no firewalls or SSL certificates for protecting the server's network. Each component (database, application server) has to share the resources (CPU, RAM, and SSD) provided by the server.

What a server is?
A server is a computer or system that provides resources, data, services, or programs to other computers, known as clients, over a network, which are usually referred to as clients.

The role of the domain name.
IP Address use to provide a human-friendly alias. one example, the domain name www.google.com is easier mo than remember the IP address such 198.102. 434.8. domain name alias is mapped in the Domain Name System (DNS)

The type of DNS record www is in www.foobar.com.
www.foobar.com uses an A record. This can be checked by Web server that is a computer that runs websites. www.foobar.com. An a record is used address mapping record changes and returned. (A Record) ,also known as a DNS host record, stores a hostname and its corresponding IPv4 address.

The role of the web server. 
A web server is a (soft-hard)ware that HTTP to respond accepts clinent requests via HTTP or secure HTTP (HTTPS) and resource or an error messsage for users.

The role of the application server.
Application servers are designed to install, operate and host applications and associated services for end users by Some IT services and organizations and facilitates the hosting and delivery of high-end consumer or business applications improved availability, supports complex database access, transaction support, and mail services.

The role of the database.
To maintain a collection of organized information that can easily be accessed, managed and updated

What the server uses to communicate with the computer of the user requesting the website (users).
TCP/IP protocol suite. TCP is a connection-oriented protocol to communicate between the (users) and the server occurs over the internet network through the TCP/IP protocol suite. connections until the end have finished exchanging messages.


Issues With This Infrastructure
There are multiple SPOF (Single Point Of Failure) in this infrastructure.aging or inadequate infrastructure, lack of maintenance, capacity constraints, and susceptibility to natural disasters or other disruptions.
For example, if the MySQL database server is down, the entire site would be down.

Downtime when maintenance needed.
Period during which an equipment or machine is not functional or cannot work. 
that need to run some maintenance checks on any component, we have to be put down or the server has to be turned off. Since there's only one server, the website would be experiencing a downtime.

Cannot scale if there's too much incoming traffic.
Scaling when it pertains to web performance essentially means the ability to support any traffic load.
It would be hard to scale this infrastructure becauses one server contains the required components. The server can quickly run out of resources or slow down when it starts receiving a lot of requests.

