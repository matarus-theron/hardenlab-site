---
title: Getting started & recovery
description: What to prepare before local Windows hardening and what to check afterwards.
---

**The product is not yet available.** This page describes the intended preparation and workflow. A product download will be offered only at launch.

## 1. Prepare

- Check for Windows 11 Pro or Enterprise. Planned targets are 26H2 and 25H2 in de-DE or en-US.
- Make sure the device is neither an AD domain member nor managed through Intune, MDM or Autopilot.
- Create a current, restorable backup. The local HardenLab snapshot does not replace a full backup.
- If BitLocker is enabled, store the recovery key securely and separately from the device.
- Define a recovery procedure and use a pilot device first.
- Test business apps, printers, NAS, network shares and remote access before making changes and record the results.

You need local administrator rights. If you are not familiar with backups or recovery, involve a qualified person before deployment.

## 2. Apply to a pilot device

The intended customer installation path is **HardenLab-Setup.exe** from the official product download. Internal PowerShell scripts are not an alternative standard customer workflow.

The installer applies the Defender, Firewall, UAC/LSA and Windows Update core areas locally. According to the product documentation, the affected policies and registry values are backed up before changes. Application is intended to stop if that backup cannot be created.

## 3. Verify before wider deployment

Follow any restart instructions and test the same functions you checked before making changes. Printers, shares, NAS, RDP and business-critical applications are particularly important.

The firewall baseline can restrict incoming connections on the public network profile. Test remote access while physically present at the pilot device to avoid locking yourself out of a remote system. Include other devices only after a successful pilot.

## If something stops working

The product documentation provides for local recovery through **HardenLab-Setup.exe -Rollback** or the bundled recovery tool. This restores the saved settings; it is not full Windows or file recovery. Final instructions will accompany the released package.

Stop deploying to other devices if problems occur. Ensure physical access, follow the recovery instructions and test functionality again. Data loss or an unbootable system requires the independent backup and recovery procedure you prepared beforehand.

[Product scope](/en/product/) · [Frequently asked questions](/en/faq/) · [Contact](mailto:info@hardenlab.ch)
