# 7 Das Firmennetzwerk

## 7.1

Firmennetzwerk:

* gesichert:
  * Clients für Mitarbeiter
  * Firmensmartphones
* ungesichert:
  * VPN-Server
  * WLAN- für private Geräte der Mitarbeiter
* erweitert:
  * Backup-Server
  * Production-Server

Router:

* Firewall-Server/Router
* Haupt-Router

## 7.2

Anlage _: IP-Adresstabelle


| Name                   | IP-Adresse                         | Netzmaske                     | Gateway           |
| ------------------------ | ------------------------------------ | ------------------------------- | ------------------- |
| Luna's Laptop          | 138.7.0.50                         | 255.255.255.0                 | 138.7.0.1         |
| Anton's Laptop         | 138.7.0.51                         | 255.255.255.0                 | 138.7.0.1         |
| Sebastian's Laptop     | 138.7.0.52                         | 255.255.255.0                 | 138.7.0.1         |
| Alexandra's Laptop     | 138.7.0.53                         | 255.255.255.0                 | 138.7.0.1         |
| Luna's Smartphone      | 138.7.0.100                        | 255.255.255.0                 | 138.7.0.1         |
| Anton's Smartphone     | 138.7.0.101                        | 255.255.255.0                 | 138.7.0.1         |
| Sebastian's Smartphone | 138.7.0.102                        | 255.255.255.0                 | 138.7.0.1         |
| Alexandra's Smartphone | 138.7.0.103                        | 255.255.255.0                 | 138.7.0.1         |
| WLAN-Switch mit DHCP   | vergibt 222.0.0.10 bis 222.0.0.255 | jeweils 255.255.255.0         | jeweils 222.0.0.1 |
| VPN-Server             | 222.0.0.10                         | 255.255.255.0                 | 222.0.0.1         |
| Firewall               | 222.0.0.2 / 138.7.0.1              | 255.255.255.0 / 255.255.255.0 | 222.0.0.1 / -     |
| Firmen-Router          | 222.0.0.1                          | 255.255.255.0                 | -                 |
| Production-Server      | 138.7.0.2 / 60.182.24.214          | 255.255.255.0 / 255.255.255.0 | 138.7.0.1 / ?    |
| Backup-Server          | 138.7.0.3 / 61.96.196.72           | 255.255.255.0 / 255.255.255.0 | 138.7.0.1 / ?    |

Anlage _: Routing-Tabelle "Firmen-Router"


| Ziel | Natzmaske | Nächstes Gateway | Über Schnittstelle |
| ------ | ----------- | ------------------- | --------------------- |
|      |           |                   |                     |

Anlage _: Firewall-Regeln des Firewall-Servers


| Quell-IP   | Netzmaske       | Ziel-IP   | Netzmaske     | Protokoll | Port | Aktion      |
| ------------ | ----------------- | ----------- | --------------- | ----------- | ------ | ------------- |
| 222.0.0.10 | 255.255.255.255 | 138.7.0.0 | 255.255.255.0 | *         | * | akzeptieren |
| 0.0.0.0    | 0.0.0.0         | 0.0.0.0   | 0.0.0.0       | *         | * | verwerfen   |

## 7.3

Leistungskriterien: überall 1G

## Text

* Die Abb. _: Netzwerkplan wurde mit Hilfe des Netzwerksimulationsprogrammes "Filius" erstellt. Das Firmennetzwerk besteht aus einem gesicherten (in der Abbildung grün dargestellten) und einem ungesicherten (in der Abbildung lila dargestellten) Teilnetz.  Die beiden Teilnetze werden durch einen Firewall-Server getrennt und das gesicherte Teilnetz ist nur über den Firewall-Server erreichbar. In diesem Teilnetz befinden sich die Arbeitsrechner und Firmensmartphones der Mitarbeiter sowie ein Netzwerk-Drucker. Im ungesicherten Teilnetz gibt es einen VPN-Server, der eine Verbindung zu dem gesicherten Teilnetz aufbauen kann.
* VPN steht für "virtual private network" (dt.: virtuelles, privates Netzwerk) und ermöglicht die Verbindung von zwei oder mehreren, physisch und logisch getrennten Netzen zu einem logischen Netzwerk. Zwischen den Teilnetzen existieren meist ein oder mehrere Netze.
* Zusätzlich besteht die Möglichkeit, dass Mitarbeiter über das nicht-interne WLAN ihre Mobilgeräte mit dem Internet verbinden können.
* Die Production- und Backup-Server befinden sich physisch außerhalb des Unternehmens und werden in einem Datacenter, wie z.B. bei Hetzner, gemietet. Diese sind ebenfalls durch VPN mit dem gesicherten Firmennetzwerk eingebunden.
* Durch den VPN-Server wird auch die Arbeit von zu Hause ermöglicht. In der Abbildung wird der Fall dargestellt, dass die Mitarbeiterin Alexandra ihren Firmenlaptop sowie Firmen-Smartphone in ihrem Heimnetzwerk (in der Abbildung gelb dargestellt) verbunden hat. Alexandra's Laptop und Smartphone erlangen Zugriff auf das gesicherte Firmennetzwerk, indem eine VPN-Verbindung mit dem VPN-Server hergestellt wird.
* Im Netzwerk kommen zwei IP-Adressbereiche zum Einsatz. Das interne, gesicherte Teilnetz wird festgelegt auf das Netz 138.7.0.0 und das ungesicherte Teilnetz auf 222.0.0.0. Beide Netze haben die Netzmaske 255.255.255.0. Der Switch "Switch / WLAN" des ungesicherten Netzes vergibt dynamisch IP-Adressen mittels DHCP an kabellos verbundene Geräte, z.B. ein privates Smartphone oder Tablet. Die Production- und Backup-Server haben jeweils zwei IP-Adressen: eine des gesicherten Firmennetzwerks und eine öffentliche Adresse, die vom Datacenter zugewiesen wurde. Die genauen IP-Adressen von jedem Gerät mit Netzmaske und Gateway sind in der Anlage _: IP-Adresstabelle eingetragen. 
* Um die Sicherheit im Firmennetzwerk zu gewährleisten, werden vertrauliche und interne Firmendaten von einer Firewall geschützt. Die einzige Möglichkeit das Netzwerk zu verlassen oder in das Netzwerk hinein zu kommen ist, den Weg über den VPN-Server zu gehen. Die Firewall-Regeln sind in der Tabelle in der Anlage _: Firewall-Regeln des Firewall-Servers eingetragen. Desweiteren werden im gesicherten Firmennetzwerk nur verifizierte, bestimmte Geräte zugelassen. Dazu zählen die Mitarbeiterlaptops und -Smartphones sowie Drucker, Production- und Backup-Server. 
* Der Vermittlungsrechner mit dem Namen "WAN" in der Abbildung steht vertretend für alle Router, die zwischen dem Firmen-Router, dem Datacenter-Router und Alexandra's Heimrouter vermitteln.
* Die Leistungskriterien für alle Firmennetzwerkkomponenten sind 1 GBit/s.
