**Please make sure that you have all these packages installed:**

Package            Version
------------------ --------
blinker            1.7.0

certifi            2024.2.2

charset-normalizer 3.3.2

click              8.1.7

colorama           0.4.6

Flask              3.0.3

Flask-Mail         0.9.1

idna               3.6

itsdangerous       2.2.0

Jinja2             3.1.3

MarkupSafe         2.1.5

pip                24.0

python-dotenv      1.0.1

requests           2.31.0

urllib3            2.2.1

Werkzeug           3.0.2


In order to see what packages you've installed run this command: pip list


**Afterwards run your python file and visist this port: http://127.0.0.1:5501/**

**Also make sure to change the data according to you in the .env file**

*Note that the email unction only works with an gmail account. I made another gmail for this project.*

Now you should be able to see the current bitcoin price and the top currencies.

Crontab Dokumentation:
To open the crontab editor run this command in Ubuntu: conrtab -e

**Testprotokoll**

Man kriegt die API Daten als JSON format und kann sie in der Konsole ausgeben: OK
Man kann die spezifische Daten einer Währung speichern(z.B Preis oder Kürzel): OK
Man kann die Top Kryptowährungen nach Markt Kapitalisierung darstellen und einen Limit festlegen(z.B 10): OK
Man kann alle Daten in index.html benutzen und auf einer Webseite darstellen lassen: OK
Beim reloaden der Webseite wird ein Email mit den entsprechenden Daten geschickt: OK
Skript wird im 10 minuten Takt ausgeführt: OK
Logging-Daten werden in einer Text datei geschrieben: OK

Bemerkung: Das Programm funktioniert hauptsächlich einwandfrei. Beim Cronjob kommt es jedoch manchmal zu einer Koflikt, weil der gleiche Port vom Server mehrmals benutzt wird.
