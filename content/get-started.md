---
title: Einstieg & Wiederherstellung
description: Was du vor einer lokalen Windows-Härtung vorbereiten und danach prüfen solltest.
---

**Das Produkt ist noch nicht erhältlich.** Diese Seite beschreibt den vorgesehenen Ablauf zur Vorbereitung. Ein Produktdownload wird erst zum Verkaufsstart angeboten.

## 1. Vorbereiten

- Windows 11 Pro oder Enterprise prüfen. Geplante Zielstände sind 26H2 und 25H2 in de-DE oder en-US.
- Sicherstellen, dass das Gerät weder Mitglied einer AD-Domäne noch durch Intune, MDM oder Autopilot verwaltet wird.
- Ein aktuelles, wiederherstellbares Backup erstellen. Der lokale HardenLab-Snapshot ersetzt keine vollständige Datensicherung.
- Bei BitLocker den Wiederherstellungsschlüssel unabhängig vom Gerät sicher aufbewahren.
- Einen Rückweg festlegen und zuerst ein Pilotgerät verwenden.
- Fachanwendungen, Drucker, NAS, Netzlaufwerke und Fernzugriff vor der Änderung testen und die Ergebnisse festhalten.

Du brauchst lokale Administratorrechte. Wenn dir Backup oder Wiederherstellung nicht vertraut sind, ziehe vor der Anwendung eine fachkundige Person hinzu.

## 2. Auf einem Pilotgerät anwenden

Der vorgesehene Kundenweg ist **HardenLab-Setup.exe** aus dem offiziellen Produktdownload. Interne PowerShell-Skripte sind kein alternativer Standardablauf für Kunden.

Der Installer wendet die Kernbereiche Defender, Firewall, UAC/LSA und Windows Update lokal an. Vor einem Eingriff ist laut Produktdokumentation eine Sicherung der betroffenen Richtlinien und Registry-Werte vorgesehen. Kann sie nicht erstellt werden, soll die Anwendung abbrechen.

## 3. Prüfen und erst dann ausweiten

Nach der Anwendung die Hinweise zu einem Neustart beachten und dieselben Funktionen wie vor der Änderung testen. Besonders wichtig sind Drucker, Freigaben, NAS, RDP und geschäftskritische Anwendungen.

Die Firewall-Baseline kann eingehende Verbindungen im öffentlichen Netzwerkprofil einschränken. Prüfe Fernzugriff vor Ort am Pilotgerät, damit du dich nicht aus einem entfernten System aussperrst. Erst nach einem erfolgreichen Test weitere Geräte einbeziehen.

## Wenn etwas nicht funktioniert

Die Produktdokumentation sieht einen lokalen Rückweg über **HardenLab-Setup.exe -Rollback** beziehungsweise das mitgelieferte Rückweg-Werkzeug vor. Er stellt die gesicherten Einstellungen wieder her; er ist keine vollständige Windows- oder Dateiwiederherstellung. Die endgültige Anleitung wird mit dem freigegebenen Paket geliefert.

Bei Problemen keine weiteren Geräte verändern. Zugriff vor Ort sicherstellen, Wiederherstellungsanleitung befolgen und anschließend die Funktionen erneut prüfen. Für Datenverlust oder ein nicht mehr startendes System brauchst du deinen unabhängig vorbereiteten Backup- und Wiederherstellungsweg.

[Produktumfang](/product/) · [Häufige Fragen](/faq/) · [Kontakt](mailto:info@hardenlab.ch)
