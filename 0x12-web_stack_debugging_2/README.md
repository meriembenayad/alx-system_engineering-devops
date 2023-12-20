## Web stack debugging #2

![debugging](debugging.jpg)

## Tasks

<details>
<summary>0. Run software as another user</summary>

In Linux, the `root` user is like a boss who can do anything they want. This can be good and bad. It's bad if you accidentally run a dangerous command like `rm -rf /`, which can't be undone. So, it's better to use a special user who can do `root` tasks when needed, using a specific command.

In this project, you're given containers where everything runs under the `root` user. This `root` user can also run anything as another user.

You're asked to:
- Create a Bash script that takes one input
- This script should run the `whoami` command as the user you input
- Test your script with different users

_Example:_

```shell
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#
```

In this example, the `root` user runs a script that makes them act as the `www-data` user just for the `whoami` command. After that, they go back to being the `root` user.

***
**File:**
- File: `0-iamsomeoneelse`
</details>


<details>
<summary>1. Run Nginx as Nginx</summary>

The `root` user in Unix is like the boss who can do anything. For safety, you should try to stop anyone from logging in as `root`. It's better not to run your web servers as `root` (which is usually the default) but as the `nginx` user instead. This way, if a hacker breaks into your server, they can only do what the `nginx` user can do.

You need to change this container so that Nginx runs as the `nginx` user.

_Here's what you need to do:_

- Make sure `nginx` is running as the `nginx` user
- Make sure `nginx` is listening on all active IPs on port `8080`
- You can't use `apt-get remove`
- Write a Bash script that sets up the container to meet these requirements

After you've fixed it, it should look like this:

```shell
root@ab6f4542747e:~# ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
nginx      886  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      887  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      888  0.0  0.0  77712  3208 ?        S    19:16   0:00  \_ nginx: worker process
root@ab6f4542747e:~#
root@ab6f4542747e:~# nc -z 0 8080 ; echo $?
0
root@ab6f4542747e:~#
```

In this example, `nginx` is running as the `nginx` user and is listening on port `8080`.

***
**File:**
- File: `1-run_nginx_as_nginx`
</details>


<details>
<summary>2. 7 lines or less</summary>

You need to make a shorter version of the script you made in task #1. Here are the rules:

- Your Bash script can't be more than 7 lines long
- There needs to be a new line at the end of the file
- You have to follow the rules for Bash scripts
- You can't use `;`
- You can't use `&&`
- You can't use `wget`
- You can't run the script you made in the previous task (Don't include the name of the previous script in this one)

So, you need to find a way to do the same thing but in a shorter and simpler way. Good luck!
***
**File:**
- File: `100-fix_in_7_lines_or_less`
</details>
