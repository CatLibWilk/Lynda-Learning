## Chpt. 1 Apache HTTP Server
- a web server needs a static IP address and domain name.
- Apache configuration
    - config files at `etc/apache2`
    - `apache2.conf` is main config file
    - on ubuntu, configuration is broken out into several files:  
        - main config = `apache2.conf`
        - individual site configs = `sites-available` folder
            -  use `a2ensite` and `a2dissite` to enable/disable sites