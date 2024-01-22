## Postmortem

### Background Context

[![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/294/tWUPWmR.png)](https://youtu.be/rp5cVMNmbro)

Any software system will eventually fail, and that failure can come stem from a wide range of possible factors: bugs, traffic spikes, security issues, hardware failures, natural disasters, human error… Failing is normal and failing is actually a great opportunity to learn and improve. Any great Software Engineer must learn from his/her mistakes to make sure that they won’t happen again. Failing is fine, but failing twice because of the same issue is not.

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

- To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
- And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

### Resources

**Read or watch**:

- [Incident Report, also referred to as a Postmortem](https://sysadmincasts.com/episodes/20-how-to-write-an-incident-report-postmortem)
- [The importance of an incident postmortem process](https://www.atlassian.com/incident-management/postmortem)
- [What is an Incident Postmortem?](https://www.pagerduty.com/resources/learn/incident-postmortem/)

### Tasks:

<details>
<summary>0. My first postmortem</summary>

Compose a postmortem based on a web stack debugging project issue or an outage you've personally experienced. If you've never encountered an outage, feel free to use your imagination and create a hypothetical scenario :)

Guidelines:

- **Issue Summary** (typically read by executives) should include:
    - The outage's duration, including start and end times (with timezone)
    - The impact of the outage (Which service was down/slow? What were users experiencing? What percentage of users were affected?)
    - The root cause of the issue
- **Timeline** (presented as bullet points, format: `time` - `a brief 1 or 2 sentence description`) should detail:
    
    - The time the issue was detected
    - How the issue was detected (Was it a monitoring alert, an observation by an engineer, a customer complaint, etc.?)
    - The actions taken (Which parts of the system were investigated? What were the assumptions about the root cause of the issue?)
    - Any misleading paths taken during the investigation/debugging
    - Who the incident was escalated to (team/individuals)
    - How the incident was resolved
- **Root Cause and Resolution** should:
    
    - Provide a detailed explanation of what caused the issue
    - Explain in detail how the issue was resolved
- **Corrective and Preventive Measures** should outline:
    
    - Broad improvements or fixes that can be made
    - A specific list of tasks to address the issue (like a TODO list, e.g., patch Nginx server, add server memory monitoring, etc.)
- Keep your postmortem concise and to the point, aiming for between 400 to 600 words.

While the format of a postmortem can vary, adhere to this structure to ensure your peers can review your work effectively.

Remember, these blogs should be written in English to enhance your technical skills in various contexts.

</details>

<details>
<summary>1. Make people want to read your postmortem</summary>

In an era where we're continually bombarded with information, capturing people's attention can be challenging.

Enhance the appeal of your post-mortem by incorporating elements of humor, engaging diagrams, or any other attention-grabbing content.

Keep in mind, these blogs should be composed in English to bolster your technical proficiency in a range of environments.

</details>
