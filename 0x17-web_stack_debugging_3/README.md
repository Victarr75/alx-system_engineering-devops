# WordPress LAMP Stack Debugging

## Project Overview

This project involves debugging a WordPress website running on a LAMP (Linux, Apache, MySQL, PHP) stack. The main objective is to identify the cause of a `500 Internal Server Error` using `strace` and to implement a fix using Puppet. The fix should be automated with a Puppet manifest, ensuring that the WordPress site runs smoothly without any errors.

## Requirements

- **Operating System:** Ubuntu 14.04 LTS
- **Web Server:** Apache 2.4
- **Database:** MySQL
- **Server-Side Scripting:** PHP 5.5.9
- **Configuration Management:** Puppet v3.4

## Project Structure

- **`0-strace_is_your_friend.pp`**: Puppet manifest that contains the fix for the `500 Internal Server Error`.
- **`README.md`**: This file, providing an overview of the project and instructions.

## Installation and Setup

1. **Install Apache:**

   ```bash
   sudo apt-get install apache2 -y
   ```

2. **Install MySQL:**

   ```bash
   sudo apt-get install mysql-server -y
   ```

3. **Install PHP:**

   ```bash
   sudo apt-get install php libapache2-mod-php php-mysql -y
   ```

4. **Install Puppet:**

   ```bash
   sudo apt-get install puppet -y
   ```

5. **Install Puppet-Lint:**

   ```bash
   sudo gem install puppet-lint -v 2.1.1
   ```

## Debugging Process

1. **Use `strace` to Identify the Issue:**

   Use `strace` to trace system calls and signals and identify why Apache is returning a `500 Internal Server Error`.

2. **Automate the Fix with Puppet:**

   Create a Puppet manifest (`0-strace_is_your_friend.pp`) that automates the necessary fix. This may involve installing missing packages, correcting file permissions, or fixing configuration issues.

3. **Apply the Puppet Manifest:**

   ```bash
   sudo puppet apply 0-strace_is_your_friend.pp
   ```

4. **Verify the Fix:**

   Ensure that the `500` error is resolved and that the WordPress site is functioning correctly.

## Example

Before applying the fix:

```bash
curl -sI http://127.0.0.1
```

After applying the fix using Puppet:

```bash
sudo puppet apply 0-strace_is_your_friend.pp
curl -sI http://127.0.0.1
```

## License

This project is for educational purposes and does not have a specific license.

---

This README provides an overview of the project, the steps needed to set up the environment, and a guide on how to identify and fix the issue using `strace` and Puppet.
