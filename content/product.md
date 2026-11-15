---
title: HardenLab Local Pack
description: Ein definiertes Paket lokaler Sicherheitseinstellungen für kleine Windows-11-Umgebungen. Noch nicht erhältlich.
---

## Was du damit erreichen kannst

HardenLab Local Pack bündelt grundlegende Windows-Sicherheitseinstellungen in einem lokal anwendbaren Paket. Dadurch musst du die Richtlinien für Virenschutz, Firewall, Administratorabfragen und Updates nicht einzeln zusammensuchen.

Gedacht ist es für Unternehmen und Selbständige mit wenigen, lokal verwalteten PCs. Eine zentrale Geräteverwaltung ist nicht erforderlich. Für die Anwendung brauchst du Administratorrechte und Erfahrung mit Backup, Wiederherstellung und Funktionstests.

**Status: in Vorbereitung.** Die folgenden Angaben beschreiben den geplanten Umfang. Es gibt noch keinen Verkauf, keine Vorbestellung und keinen öffentlich bereitgestellten Produktdownload.

## Geplanter Kernumfang

| Bereich | Zweck |
|---|---|
| Microsoft Defender | Grundlegende Richtlinien für den integrierten Virenschutz |
| Windows-Firewall | Eine definierte Basis für die Netzwerkabsicherung |
| UAC / LSA | Einstellungen für Administratorabfragen und den Schutz der Anmeldung |
| Windows Update | Richtlinien für Windows-Updates |

Das Paket ersetzt weder Backups noch die laufende Pflege der Geräte und garantiert keine vollständige Sicherheit oder bestimmte Compliance-Ergebnisse.

## Vorgesehene Umgebung

- **System:** Windows 11 Pro oder Enterprise, 26H2 als primärer Zielstand und 25H2 als weiterer Zielstand.
- **Sprachen:** de-DE und en-US.
- **Geräte:** lokal verwaltete PCs und Notebooks, einzeln oder in Arbeitsgruppen.
- **Anwendung:** über den offiziellen Installer **HardenLab-Setup.exe** mit lokalen Administratorrechten.
- **Technik:** lokale Windows-Gruppenrichtlinien; kein Active Directory erforderlich. LGPO.exe wird nicht mitgeliefert.

Diese Zielstände entsprechen der aktuellen Produktdokumentation. Die endgültige Freigabe und bekannte Einschränkungen werden zum Verkaufsstart dokumentiert.

## So sieht ein Einsatz aus

Ein Unternehmen mit fünf lokal verwalteten PCs könnte die geplante **Team-Variante** nutzen. Zuerst wird ein PC gesichert und als Pilotgerät vorbereitet. Nach Anwendung der vier Kernbereiche werden Fachanwendungen, Drucker, NAS und Fernzugriff geprüft. Erst bei einem erfolgreichen Test folgen die weiteren Geräte.

**Beispiel für den Umfang:** Defender + Firewall + UAC/LSA + Windows Update. Das ist eine Übersicht, kein ausführbarer Installationsbefehl. [Der vorgesehene Ablauf und Rückweg](/get-started/) erklärt die Vorbereitung genauer.

## Grenzen und bekannte Auswirkungen

Nicht vorgesehen sind Windows Home, Windows Server, Active Directory, Intune/MDM/Autopilot, Office-/Adobe-Härtung und ein zentraler automatischer Rollout. Audit und Browser-Härtung sind nicht Teil des Kernumfangs; mögliche Erweiterungen werden separat angekündigt.

Firewallrichtlinien können Fernzugriff und Freigaben beeinflussen. Die dokumentierte Baseline schränkt lokale Firewallregeln im öffentlichen Netzwerkprofil ein. RDP sowie Datei- und Druckerfreigaben müssen deshalb vor dem breiten Einsatz geprüft werden. Ein öffentliches Netz darf nicht allein zur Umgehung dieser Einschränkung als vertrauenswürdig eingestuft werden.

## Lieferung, Updates und Support

Geplant sind Installer und begleitende Dokumentation. Ein endgültiger Lieferumfang, Updatezeitraum oder Supportumfang ist noch nicht zugesagt. Die vorgesehenen Lizenzvarianten dienen der internen Nutzung in der eigenen Organisation. Einsätze bei Kunden oder Weiterverkauf benötigen eine gesonderte Vereinbarung.

[Geplante Preise & Verfügbarkeit](/buy/) · [Frage per E-Mail stellen](mailto:info@hardenlab.ch)
