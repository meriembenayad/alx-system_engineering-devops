## Load balancer

#### Concepts

_For this project, we expect you to look at these concepts:_

- [Load balancer](load_balancer.md)
- [Web stack debugging](../0x0D-web_stack_debugging_0/web_stack_debugging.md)

![Load Balancer](load_balancer.png)

### Background Context

You have been given 2 additional servers:

- gc-\[STUDENT\_ID\]-web-02-XXXXXXXXXX
- gc-\[STUDENT\_ID\]-lb-01-XXXXXXXXXX

Let’s improve our web stack so that there is [redundancy](https://en.wikipedia.org/wiki/Redundancy_%28engineering%29) for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

### Resources

**Read or watch**:

- [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HTTP header](https://www.techopedia.com/definition/27178/http-header)
- [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)

### Requirements

#### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck` (version `0.3.7`) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

### Tasks

<details>
<summary>0. Double the number of webservers</summary>

In the initial step, your task is to replicate the configuration of ``web-02`` to mirror that of ``web-01``. Fortunately, a Bash script developed during your prior [web server project](../0x0C-web_server/") can now be conveniently employed to accomplish this configuration for ``web-02``. Always keep in mind the importance of automating your tasks for efficiency.

Given that our web servers are now positioned behind a load balancer in this project, the objective is to incorporate a custom Nginx response header. This header, designated as ``X-Served-By``, serves the purpose of identifying which web server is handling our HTTP requests. The intention is to gain insights into the functionality of the load balancer. Further details on this will be provided in subsequent tasks.

***Key Requirements:***

- Configure Nginx on both web-01 and web-02 to include a custom HTTP header in its response.
- The custom HTTP header should bear the name X-Served-By.
- The value of this custom HTTP header must correspond to the hostname of the Nginx server.
- Develop a script named 0-custom_http_response_header to configure a completely new Ubuntu machine in accordance with the specified task requirements.
- Disregard SC2154 in shellcheck.

Example:

```shell
sylvain@ubuntu$ curl -sI 34.198.248.145 | grep X-Served-By
X-Served-By: 03-web-01
sylvain@ubuntu$ curl -sI 54.89.38.100 | grep X-Served-By
X-Served-By: 03-web-02
sylvain@ubuntu$
```

If your server’s hostnames are not properly configured (`[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`.), follow this [tutorial](https://repost.aws/knowledge-center/linux-static-hostname).

***
**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0F-load_balancer`
- File: `0-custom_http_response_header`

</details>

<details>
<summary>1. Install your load balancer</summary>

Set up and customize HAproxy on your `lb-01` server with the following specifications:

- Installation and Configuration:
	- Install HAproxy on the `lb-01` server.
- HAproxy Configuration:
	- Tailor HAproxy to direct incoming traffic to both `web-01` and `web-02` servers.
- Load Balancing:
	- Implement a round-robin algorithm to evenly distribute incoming requests between `web-01` and `web-02`.
- Init Script Management:
	- Confirm the operability of HAproxy management through an init script.
- Hostname Verification:
	- Ensure that the servers are appropriately configured with the designated hostnames, namely `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`. If adjustments are needed, refer to the provided [tutorial](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-hostname.html).

Compose a Bash script in your answer file capable of configuring a new Ubuntu machine to adhere to the aforementioned requirements.

***Example:***

```shell
sylvain@ubuntu$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:17 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

sylvain@ubuntu$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:19 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: "5315bd25-264"
X-Served-By: 03-web-02
Accept-Ranges: bytes

sylvain@ubuntu$
```

***
**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0F-load_balancer`
- File: `1-install_load_balancer`
</details>

<details>
<summary>2. Add a custom HTTP header with Puppet</summary>

Automate the process of generating a custom HTTP header response, this time using Puppet.

***Requirements:***

The custom HTTP header should be named `X-Served-By`.
The value of this custom HTTP header must reflect the hostname of the server where Nginx is operating.
Create a Puppet script named ``2-puppet_custom_http_response_header.pp`` that sets up a new Ubuntu machine according to the specified task requirements.

***
**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0F-load_balancer`
- File: `2-puppet_custom_http_response_header.pp`
</details>
