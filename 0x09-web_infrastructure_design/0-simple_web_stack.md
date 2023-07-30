# 0. Simple web stack

* Link to image (<https://imgur.com/a/1PIMQGF>)
* When a user types 'wwww.foobar.com' in the browser, the browser searches it's cache and the OS's cache to find the IP address of the server that is hosting the website.
If this fails, a request for the IP address of 'www.foobar.com' is made to the DNS server and then a GET request is sent to the server at 8.8.8.8

* What is a server: A server is a piece of computer hardware or software that provides functionality for other programs or devices. Servers are usually located at data centers
* What is the role of the domain name: The domain name provides a way for humans to identify the servers that host resources on the web without having to worry about the actual IP addresses. I serves as an alias for the IP address of the server
* What type of DNS record www is in <www.foobar.com>: An A (address) record which is the IP address of the server on which 'www.foobar.com' is located
* What is the role of the web server: The web server reponds to HTTP requests from the client with static web pages
* What is the role of the application server: The application server computes dynamic content.
* What is the role of the database: Stores the application data
* What is the server using to communicate with the computer of the user requesting the website: The server is communicating with the client via HTTP over the network
* The DNS server resolves the domain name into an IP address
* SPOF: The single point of failure is the server because there is no backup or redunduncy. Once the server goes down, the website is offline
* Downtime when maintenance needed (like deploying new code web server needs to be restarted): The server would be down whenever new code is deployed
* Cannot scale if too much incoming traffic: With only one server, the website would go down if overwhelmed with traffic.
