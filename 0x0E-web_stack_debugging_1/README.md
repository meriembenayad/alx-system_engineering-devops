## Web stack debugging 1

#### Concepts

_For this project, we expect you to look at these concepts:_

- [Network basics](../0x07-networking_basics/)
- [Web stack debugging](../0x0D-web_stack_debugging_0/web_stack_debugging.md)

![Debugging #1](debugging.jpg)

### Requirements

#### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file at the root of the folder of the project is mandatory
- All your Bash script files must be executable
- Your Bash scripts must pass `Shellcheck` without any error
- Your Bash scripts must run without error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- You are not allowed to use `wget`

### Tasks

<details>
<summary>0. Nginx likes port 80<summary>

>Debug your Ubuntu container's Nginx installation to identify the impediment preventing it from listening on port `80`. Utilize your debugging proficiency, install necessary tools, and manipulate containers as needed to troubleshoot the problem. Subsequently, devise a Bash script with the least number of commands to automate the resolution.

>***Specifications:***

>- Ensure Nginx is operational and listening on port `80` for all active IPv4 addresses on the server.
>- Develop a Bash script that configures the server to meet the specified requirements.

***
- File: `0-nginx_likes_port_80`
</details>

<details>
<summary>1. Make it sweet and short<summary>

Refine your solution for task #0, ensuring brevity and simplicity.

***Requirements:***

- The Bash script must consist of 5 lines or fewer.
- The file should end with a new line.
- Adhere to standard Bash script conventions.
- Avoid using semicolons (;).
- Avoid using double ampersands (&&).
- Exclude the use of wget.
- The script should not execute your previous answer file.
- The 'service' command (init) should genuinely report that Nginx is not running.
***
- File: `1-debugging_made_short`

</details>
