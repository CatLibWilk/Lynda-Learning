## Config

- Ubuntu config location: `/etc/apache2/apache2.conf` 
    - but also uses smaller config files per site and config (e.g. a plugin)
- where is config? `apachectl -V` will show
- directory-level config: `.htaccess` -- for security reasons, not recommended
## VirtualHosting
- server content for multiple domains from the same server
- 2 types
    - Name-based (routes requests based on domain name)
    - IP-based
    - in .conf file:
        - <VirtualHost [IP]:[PORT]> encloses vhost info
            - includes <Directory path/to/content> which contains some permissions settings
                - Order 
                - Allow: eg 'from all' access is allowed from all (could be a specific host name, IP, or env var)
                - Require: eg. 'all granted' = all users granted access unconditionally
            - also DocumentRoot directive which gives dir from where serving files
    - check new config is syntax-error free: `apachectl -t`
    - show VHOST details: `apachectl -t -D DUMP_VHOSTS`

## Modules
- httpd is system of plugins that add functionality
    - static mods are loaded every time apache started
    - shared mods added without recompilation
- modules have directives to config additional functionality
    - if config has directive for a missing mod, the server wont start
        - avoid by wrapping directive in `IfModule` block
            - eg. `<IfModule mod_ssl>`
- check running mods: `apachectl -t -D DUMP_MODULES`
- mod configsL: `/etc/apache/mods-available` 