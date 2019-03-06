# Freifunk Kiel Services Maschine

## Dienste:
- grafana-server
- icinga2
  - icingaweb2
  - mysql
- mysqld
- apache2
- fastd
- postgres
- prometheus
  - prometheus-mysql
  - prometheus-node
- gitolite
- smokeping
- ddhcpd? bash  `-ddhcpd -D -s 0 -b 2 -B 300 -S -i br-ffki -N 10.116.160.0 19 -t 15`
- Maps
  - mesh.freifunk.in-kiel.de
    - hopglass (/opt/hopglass/server/hopglass-server.js)
  - map.freifunk.in-kiel.de
    - yanic (/opt/ffki-meshviewer-ffrgb)
- redmine (issues)
  - postgres: ffki_redmine
- opkg mirror
- mediawiki (/usr/share/mediawiki/)
  - /etc/mediawiki/LocalSettings.php
  - mysql
- phpmyadmin
- ffki website
  - startseite
  - blog
  - ff-node-monitor (/opt/ff-node-monitor)
    - postgres

## Cronjobs:
- ffapi
  - update node count
- backup
  - rsnapshot
  - db backup
    - ff-node-monitor
    - mediawiki
    - redmine
    - opkg mirror
  - maybe with automysqlbackup

daily:
- chrootkit
- etckeeper 
unsicher:
- collectd
