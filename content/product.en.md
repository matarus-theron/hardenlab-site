---
title: HardenLab Local Pack
description: A defined package of local security settings for small Windows 11 environments. Not yet available.
---

## What it helps you do

HardenLab Local Pack brings basic Windows security settings together in a locally deployable package. It saves you from assembling individual policies for antivirus protection, the firewall, administrator prompts and updates yourself.

It is designed for businesses and self-employed professionals with a small number of locally managed PCs. No central device management is required. Deployment needs administrator rights and experience with backups, recovery and functional testing.

**Status: in preparation.** The information below describes the planned scope. Sales, pre-orders and a public product download are not available yet.

## Planned core scope

| Area | Purpose |
|---|---|
| Microsoft Defender | Basic policies for built-in antivirus protection |
| Windows Firewall | A defined starting point for network protection |
| UAC / LSA | Settings for administrator prompts and sign-in protection |
| Windows Update | Policies for Windows updates |

The package does not replace backups or ongoing device maintenance and does not guarantee complete security or specific compliance outcomes.

## Intended environment

- **System:** Windows 11 Pro or Enterprise, with 26H2 as the primary target and 25H2 as an additional target.
- **Languages:** de-DE and en-US.
- **Devices:** locally managed PCs and laptops, standalone or in workgroups.
- **Deployment:** the official **HardenLab-Setup.exe** installer with local administrator rights.
- **Technology:** local Windows Group Policy; no Active Directory required. LGPO.exe is not bundled.

These targets reflect the current product documentation. Final release approval and known limitations will be documented at launch.

## An example deployment

A business with five locally managed PCs could use the planned **Team tier**. One PC is backed up and prepared as a pilot device. After applying the four core areas, business applications, printers, NAS and remote access are tested. Other devices follow only after a successful pilot.

**Example scope:** Defender + Firewall + UAC/LSA + Windows Update. This is an overview, not an executable installation command. [The intended workflow and recovery guidance](/en/get-started/) explains the preparation in more detail.

## Limits and known effects

Windows Home, Windows Server, Active Directory, Intune/MDM/Autopilot, Office/Adobe hardening and central automated rollout are outside the intended scope. Audit and browser hardening are not included in the core product; potential extensions will be announced separately.

Firewall policies can affect remote access and shares. The documented baseline restricts local firewall rules on the public network profile. RDP, file sharing and printer sharing must therefore be tested before wider deployment. Do not mark a public network as trusted merely to bypass this restriction.

## Delivery, updates and support

An installer and accompanying documentation are planned. Final deliverables, update periods and support scope have not yet been committed. The intended license tiers are for internal use within your own organization. Use on customer systems or resale requires a separate agreement.

[Planned pricing & availability](/en/buy/) · [Ask a question by email](mailto:info@hardenlab.ch)
