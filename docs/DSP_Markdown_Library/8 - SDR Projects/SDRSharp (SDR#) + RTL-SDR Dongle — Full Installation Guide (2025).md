**Step-by-Step installation guide for SDR# (SDRSharp) with RTL-SDR dongle**, including the correct `.NET` version clarification:
---
## ✅ SDRSharp (SDR#) + RTL-SDR Dongle — Full Installation Guide (2025)

### 📦 Prerequisites

1. **Windows 10 or later (64-bit recommended)**
2. **.NET 8 Runtime** (or .NET 9 if using the latest SDRSharp releases)
3. **Admin rights to install drivers**

---

### 🔧 Step-by-Step Setup

#### 1. **Download SDRSharp (SDR#)**

* Visit: [https://airspy.com/download/](https://airspy.com/download/)
* Download: `sdrsharp-x86.zip` *(latest version)*

#### 2. **Extract the ZIP**

* Extract to: `C:\SDRSharp` (or your preferred folder)

#### 3. **Install RTL-SDR USB Driver via Zadig**

* Run `zadig.exe` from the SDRSharp folder (or download from [https://zadig.akeo.ie/](https://zadig.akeo.ie/))
* Choose:

  * Device: `Bulk-In, Interface 0` *(NOT 1 or 2)*
  * Driver: Replace with **WinUSB**
* Click **Install Driver**

✅ After success, Device Manager should list:

```
Bulk-In, Interface 0 — WinUSB (working)
```

---

### ⚙️ Runtime Check: .NET

* **SDRSharp.exe** requires: `.NET Framework 4.8`
* **SDRSharp.dotnet8.exe** requires: **.NET 8 Runtime**

🟢 You successfully used:
👉 **`SDRSharp.dotnet8.exe`**
which works on modern systems and should be your default going forward.

---

### 🔌 Verify RTL-SDR is Working

Run:

```shell
rtl_test.exe
```

Expected output:

```
Found 1 device(s):
  0: Realtek, RTL2838UHIDIR, SN: 00000001
Using device 0: Generic RTL2832U OEM
Found Rafael Micro R820T tuner
...
```

---

### 🚀 Launch SDRSharp

Run:

```shell
SDRSharp.dotnet8.exe
```

✅ Now select:

* **Source**: `RTL-SDR (USB)`
* Start the receiver and tune!

---

### 📁 Optional: Save Setup for Posterity

You may copy this **clean working folder** to your GitHub repo (private or public) as a known good baseline. Do not include `.exe` binaries publicly if license-sensitive.
---

