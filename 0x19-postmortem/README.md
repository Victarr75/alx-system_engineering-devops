# Postmortem: The Curious Case of the Missing PHP Module 🕵️‍♂️

## Issue Summary

- **Duration:**  
  *Start:* August 17, 2024, 10:00 AM EAT  
  *End:* August 17, 2024, 12:15 PM EAT  
  *(2 hours and 15 minutes)*

- **Impact:**  
  Our WordPress site was down, resulting in a 500 Internal Server Error for 95% of users attempting to access the site. Users were greeted with an error page instead of the home page, leaving them unable to interact with the website.

- **Root Cause:**  
  A missing PHP module (`php-mysql`) that is essential for WordPress to communicate with the MySQL database was not installed, leading to the 500 error.

---

## Timeline 📅

- **10:00 AM:** Issue detected through monitoring alerts that indicated a sharp drop in traffic and multiple reports of a 500 error from users.
- **10:05 AM:** The issue was confirmed by attempting to access the website and observing the 500 error.
- **10:10 AM:** Initial investigation focused on checking server logs for Apache and PHP errors.
- **10:20 AM:** Apache error logs revealed a PHP fatal error related to MySQL connectivity.
- **10:30 AM:** Assumptions were made about potential MySQL service failures, but further checks showed MySQL was running correctly.
- **10:45 AM:** The incident was escalated to the DevOps team.
- **11:00 AM:** A detailed inspection of the PHP configuration indicated the absence of the `php-mysql` module.
- **11:15 AM:** The missing module was installed, and Apache was restarted.
- **11:20 AM:** The website began responding correctly, showing a normal homepage.
- **11:30 AM:** Monitoring confirmed that traffic had returned to normal levels, and no further errors were reported.
- **12:15 PM:** The incident was officially closed after ensuring all services were stable.

---

## Root Cause and Resolution 🛠️

- **Root Cause:**  
  The `php-mysql` module, which allows PHP to interact with MySQL, was missing from the server. This omission occurred during a recent server update where the PHP environment was reconfigured. Without this module, WordPress could not connect to the database, resulting in a 500 Internal Server Error.

- **Resolution:**  
  The missing PHP module was installed using the following command:
  ```bash
  sudo apt-get install php-mysql
  ```
  After installing the module, the Apache server was restarted to apply the changes:
  ```bash
  sudo systemctl restart apache2
  ```
  This resolved the connectivity issue, and the WordPress site was restored to full functionality.

---

## Corrective and Preventative Measures 📋

- **Improvements Needed:**  
  - **Enhanced Monitoring:** Implement monitoring to detect missing PHP modules or misconfigurations before they cause outages.
  - **Automated Deployment:** Use configuration management tools like Puppet or Ansible to ensure all necessary packages are installed during server setups.
  - **Documentation:** Update the server setup documentation to include a checklist of required PHP modules for WordPress installations.

- **Action Items:**  
  1. **Patch Configuration Files:** Review and patch server configuration files to include all necessary PHP modules for WordPress.
  2. **Add Monitoring:** Integrate a new monitoring check to alert when critical PHP modules are missing.
  3. **Update Playbooks:** Update the server deployment playbooks to automatically install all necessary dependencies.
  4. **Training:** Conduct a training session for the DevOps team on the importance of verifying PHP configurations during updates.

---

![Outage Timeline](timeline-diagram.png)

*“The hardest part of debugging is realizing that the bug is in your own code.”*

---
