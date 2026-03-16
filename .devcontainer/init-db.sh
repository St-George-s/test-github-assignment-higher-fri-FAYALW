#!/usr/bin/env bash
set -euo pipefail

echo "[init-db] Installing MariaDB…"

sudo rm -f /etc/apt/sources.list.d/yarn.list

sudo apt-get update -y
sudo apt-get install -y mariadb-server mariadb-client

echo "[init-db] Preparing runtime dir…"
sudo mkdir -p /var/run/mysqld
sudo chown -R mysql:mysql /var/run/mysqld

echo "[init-db] Starting mysqld…"
sudo nohup mysqld --user=mysql --bind-address=0.0.0.0 >/tmp/mysqld.log 2>&1 &

echo -n "[init-db] Waiting for MariaDB"
for i in {1..60}; do
  if mysqladmin ping -h 127.0.0.1 --silent; then
    echo " ✓"
    break
  fi
  echo -n "."
  sleep 1
done

echo "[init-db] Create default DB and accounts…"
sudo mysql <<'SQL'
CREATE DATABASE IF NOT EXISTS school;

CREATE USER IF NOT EXISTS 'student'@'localhost' IDENTIFIED BY 'studentpw';
CREATE USER IF NOT EXISTS 'student'@'127.0.0.1' IDENTIFIED BY 'studentpw';
CREATE USER IF NOT EXISTS 'student'@'%' IDENTIFIED BY 'studentpw';

ALTER USER 'student'@'localhost' IDENTIFIED BY 'studentpw';
ALTER USER 'student'@'127.0.0.1' IDENTIFIED BY 'studentpw';
ALTER USER 'student'@'%' IDENTIFIED BY 'studentpw';

GRANT ALL PRIVILEGES ON *.* TO 'student'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'student'@'127.0.0.1';
GRANT ALL PRIVILEGES ON *.* TO 'student'@'%';
FLUSH PRIVILEGES;
SQL

if [[ -f /tmp/seed.sql ]]; then
  mysql --protocol=TCP -h 127.0.0.1 -ustudent -pstudentpw school < /tmp/seed.sql
fi

echo "[init-db] Done."