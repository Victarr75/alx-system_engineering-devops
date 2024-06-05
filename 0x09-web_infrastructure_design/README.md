# Web Infrastructure Design

This repository contains the design of various web infrastructures, ranging from a simple one-server setup to a more complex secured and monitored multi-server architecture. Each design aims to address specific needs, such as scalability, security, and reliability. Below are the details for each infrastructure design, including explanations of key components and potential issues.

## 0. Simple Web Stack

### Design Overview
This is a basic web infrastructure consisting of a single server to host the website `www.foobar.com`.

### Components
- **1 Server**
- **1 Web Server (Nginx)**
- **1 Application Server**
- **1 Code Base (Application Files)**
- **1 Database (MySQL)**
- **Domain Name:** `foobar.com` with a `www` record pointing to IP `8.8.8.8`

### How It Works
1. **User Request:** A user wants to access `www.foobar.com`.
2. **DNS Resolution:** The domain name `www.foobar.com` is resolved to the IP address `8.8.8.8`.
3. **Web Server:** Nginx receives the request and forwards it to the application server.
4. **Application Server:** Processes the request using the application code.
5. **Database:** If needed, the application server queries the MySQL database.
6. **Response:** The application server sends the response back through the web server to the user's browser.

### Key Concepts
- **Server:** A computer that provides data to other computers.
- **Domain Name:** Human-readable address of a website.
- **DNS Record:** `www` is a CNAME (Canonical Name) record that maps `www.foobar.com` to `foobar.com`.
- **Web Server:** Handles HTTP requests from clients.
- **Application Server:** Runs the application code and processes business logic.
- **Database:** Stores and retrieves data.
- **Communication:** HTTP/HTTPS is used for communication between the server and the user's computer.

### Issues
- **Single Point of Failure (SPOF):** If the server fails, the website becomes unavailable.
- **Maintenance Downtime:** Deploying new code or restarting the web server causes downtime.
- **Scalability:** Limited by the capacity of a single server.

### Repository
- **GitHub Repository:** `alx-system_engineering-devops`
- **Directory:** `0x09-web_infrastructure_design`
- **File:** `0-simple_web_stack`

## 1. Distributed Web Infrastructure

### Design Overview
This infrastructure improves upon the simple web stack by adding redundancy and load balancing.

### Components
- **2 Servers**
- **1 Web Server (Nginx)**
- **1 Application Server**
- **1 Load Balancer (HAProxy)**
- **1 Code Base (Application Files)**
- **1 Database (MySQL)**

### How It Works
1. **Load Balancer:** Distributes incoming traffic across multiple servers.
2. **Active-Active Setup:** Both servers are active and handle requests.
3. **Database Cluster:** Primary-Replica setup where the Primary node handles writes, and Replica nodes handle reads.

### Key Concepts
- **Load Balancer:** Distributes traffic to multiple servers to ensure no single server is overwhelmed.
- **Distribution Algorithm:** Round-robin, least connections, etc., determine how traffic is distributed.
- **Active-Active vs. Active-Passive:** Active-Active means all servers handle traffic; Active-Passive means one is on standby.
- **Primary-Replica Cluster:** Ensures data redundancy and improves read performance.

### Issues
- **SPOF:** Load balancer can be a single point of failure.
- **Security Issues:** No firewalls, no HTTPS.
- **No Monitoring:** Lack of system performance tracking.

### Repository
- **GitHub Repository:** `alx-system_engineering-devops`
- **Directory:** `0x09-web_infrastructure_design`
- **File:** `1-distributed_web_infrastructure`

## 2. Secured and Monitored Web Infrastructure

### Design Overview
This design adds security and monitoring to the distributed infrastructure.

### Components
- **3 Servers**
- **1 Web Server (Nginx)**
- **1 Application Server**
- **1 Load Balancer (HAProxy)**
- **1 SSL Certificate**
- **3 Firewalls**
- **3 Monitoring Clients (e.g., Sumologic)**

### How It Works
1. **Firewalls:** Protect each server from unauthorized access.
2. **HTTPS:** Encrypts traffic between users and the website.
3. **Monitoring:** Tracks system performance and alerts administrators of issues.

### Key Concepts
- **Firewalls:** Control incoming and outgoing network traffic based on security rules.
- **HTTPS:** Ensures secure communication over the internet.
- **Monitoring:** Collects data on server performance and health.

### Issues
- **SSL Termination at Load Balancer:** Can be a security concern as traffic between load balancer and servers is unencrypted.
- **Single MySQL Server for Writes:** Can be a bottleneck.
- **Homogeneous Server Setup:** All servers having the same components can lead to inefficiencies.

### Repository
- **GitHub Repository:** `alx-system_engineering-devops`
- **Directory:** `0x09-web_infrastructure_design`
- **File:** `2-secured_and_monitored_web_infrastructure`

## 3. Scale Up

### Design Overview
This infrastructure scales up the previous designs by splitting components across dedicated servers and enhancing load balancing.

### Components
- **1 Additional Server**
- **1 Load Balancer (HAProxy) in Cluster**
- **Dedicated Servers for Web Server, Application Server, and Database**

### How It Works
1. **Component Segregation:** Each component (web server, application server, database) runs on its own server, enhancing performance and manageability.
2. **Clustered Load Balancer:** Ensures high availability and fault tolerance.

### Key Concepts
- **Dedicated Servers:** Improve performance by isolating different services.
- **Clustered Load Balancer:** Enhances reliability by using multiple load balancers in a cluster.

### Repository
- **GitHub Repository:** `alx-system_engineering-devops`
- **Directory:** `0x09-web_infrastructure_design`
- **File:** `3-scale_up`

---

Each design builds upon the previous, addressing limitations and adding features to improve reliability, security, and scalability. For detailed implementation, refer to the respective directories and files in the GitHub repository.
