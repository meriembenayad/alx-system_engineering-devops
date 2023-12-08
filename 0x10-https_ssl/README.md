## HTTPS SSL

#### Concepts

_For this project, we expect you to look at these concepts:_

- [DNS](DNS.md)
- [Web stack debugging](../0x0D-web_stack_debugging_0/web_stack_debugging.md)

![HTTPS](HTTPS.png)

### Background Context

#### What happens when you don’t secure your website traffic?

![What happen?](not_secure.gif)

### Resources

**Read or watch**:

- [What is HTTPS?](https://www.instantssl.com/http-vs-https)
- [What are the 2 main elements that SSL is providing](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)
- [HAProxy SSL termination on Ubuntu16.04](https://docs.ionos.com/cloud/)
- [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)
- [Bash function](https://tldp.org/LDP/abs/html/complexfunct.html)

**man or help**:

- `awk`
- `dig`

### Tasks

<details>
<summary>0. World wide web</summary>

Set up your domain zone so that the subdomain www directs to your load-balancer `IP (lb-01)`. For convenience, let's also include additional subdomains and create a Bash script that will present subdomain information.

***Prerequisites:***

1. Incorporate the subdomain www into your domain and direct it to your `lb-01 IP` (you may remove any default subdomains configured with your domain name).
2. Include the subdomain `lb-01` in your domain and direct it to your `lb-01 IP`.
3. Include the subdomain `web-01` in your domain and direct it to your `web-01 IP`.
4. Include the subdomain `web-02` in your domain and direct it to your `web-02 IP`.

Your Bash script should accept two arguments:
- `domain`:
  - type: string
  - purpose: domain name to audit
  - required: yes
- `subdomain`:
  - type: string
  - purpose: specific subdomain to audit
  - required: no

Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`

When only the `domain` parameter is provided, display information for its subdomains `www`, `lb-01`, `web-01`, and `web-02`, in this specific order. When both domain and subdomain parameters are provided, display information for the specified `subdomain`. Ignore `shellcheck` case `SC2086`.

The script must use ``awk`` and at least one Bash function. You don't need to handle edge cases such as empty parameters, non-existent domain names, or non-existent subdomains.

```shell
sylvain@ubuntu$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
www.holberton.online.   87  IN  A   54.210.47.110
sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.holberton.online. 101 IN  A   54.210.47.110
sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.holberton.online. 212    IN  A   34.198.248.145
sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-02.holberton.online. 298    IN  A   54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
```
***
**Repo:**
- File: `0-world_wide_web`
</details>

<details>
<summary>1. HAproxy SSL termination</summary>

"SSL termination on HAproxy" implies that `HAproxy` is set up to manage encrypted traffic, decrypt it, and forward it to its intended destination.

You need to generate a certificate using `certbot` and set up `HAproxy` to handle encrypted traffic for your subdomain `www.`.

***Prerequisites:***

- HAproxy should be set to listen on TCP port 443
- HAproxy should be configured to handle SSL traffic
- HAproxy should be set up to serve encrypted traffic that will return the root `/` of your web server
- When you access the root of your domain name, the returned page should contain `Holberton School`
- Share your HAproxy configuration as an answer file (`/etc/haproxy/haproxy.cfg`)

The file named `1-haproxy_ssl_termination` should be your HAproxy configuration file

Please ensure that you have installed HAproxy 1.5 or a later version, as [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy) is not supported in versions earlier than 1.5.

```shell
sylvain@ubuntu$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes
sylvain@ubuntu$
sylvain@ubuntu$ curl https://www.holberton.online
Holberton School for the win!
sylvain@ubuntu$
```

***
**Repo:**
- File: `1-haproxy_ssl_termination`
</details>

<details>
<summary>2. No loophole in your website traffic</summary>

It's a good practice to mandate HTTPS traffic, thereby eliminating the possibility of unencrypted traffic. Set up HAproxy to automatically reroute HTTP traffic to HTTPS.

***Prerequisites:***

- The process should be seamless for the user
- HAproxy should return a 301 status code
- HAproxy should redirect HTTP traffic to HTTPS
- Share your HAproxy configuration as an answer file (`/etc/haproxy/haproxy.cfg`)

The file named `100-redirect_http_to_https` should serve as your HAproxy configuration file

***
**Repo:**
- File: `100-redirect_http_to_https`
</details>
