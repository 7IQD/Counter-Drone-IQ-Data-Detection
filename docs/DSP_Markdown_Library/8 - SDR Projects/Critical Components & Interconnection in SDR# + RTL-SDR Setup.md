## 📘 Chapter: **Critical Components & Interconnection in SDR# + RTL-SDR Setup**

This section explains the *purpose*, *interdependency*, and *function* of key files used in installing and running SDRSharp with RTL-SDR dongles.

---

### 🔹 1. **Core Executables**

| **File**               | **Purpose**                                   | **Remarks**                                            |
| ---------------------- | --------------------------------------------- | ------------------------------------------------------ |
| `SDRSharp.exe`         | Main SDR# GUI application (classic version)   | Requires .NET Framework 4.8                            |
| `SDRSharp.dotnet8.exe` | Modern SDR# GUI executable                    | Requires .NET 8 Runtime; runs on newer Windows 10/11   |
| `rtl_test.exe`         | CLI tool to test if RTL-SDR dongle is working | Used for device check and sample streaming diagnostics |

---

### 🔹 2. **Drivers & DLLs**

| **File**         | **Purpose**                                                          | **Remarks**                                                        |
| ---------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `rtlsdr.dll`     | Core driver library that enables communication with RTL-SDR hardware | Must match architecture (x86 or x64) of SDR# you're running        |
| `libusb-1.0.dll` | USB backend for `rtlsdr.dll`, handles USB transport layer            | Also architecture-dependent                                        |
| `WinUSB`         | Windows USB driver installed via **Zadig**                           | Essential to replace default DVB driver with SDR-compatible driver |

🔸 Without `rtlsdr.dll`, SDRSharp cannot detect or interact with RTL-SDR dongle.
🔸 Without `libusb`, `rtlsdr.dll` will fail.

---

### 🔹 3. **Install Scripts & Helper Tools**

| **File / Script**    | **Purpose**                                    | **Details**                                                  |
| -------------------- | ---------------------------------------------- | ------------------------------------------------------------ |
| `httpget.exe`        | A small CLI downloader used in automated setup | Downloads `.zip` files for SDR# and drivers                  |
| `install-rtlsdr.bat` | Batch script to automate download + setup      | Uses `httpget.exe`, extracts files, and prompts for Zadig    |
| `zadig.exe`          | USB driver installer                           | Converts Bulk-In device to `WinUSB` required by `rtlsdr.dll` |

---

### 🔹 4. **Workflow: File Interconnection Map**

```plaintext
      ┌────────────┐
      │ SDRSharp   │  ←─┐
      └────┬───────┘    │
           │            │
           ▼            │
  ┌───────────────────────┐
  │ rtlsdr.dll (API Layer)│
  └────────┬──────────────┘
           │
   ┌───────▼────────┐
   │ libusb-1.0.dll │ ←─ WinUSB driver (Zadig-installed)
   └────────────────┘
           │
   ┌───────▼─────────────┐
   │ RTL-SDR USB Dongle  │
   └─────────────────────┘
```

---

### 🔹 5. **Architecture Consistency is Key**

* `SDRSharp.dotnet8.exe` → needs `rtlsdr.dll` and `libusb-1.0.dll` from **x64**
* `SDRSharp.exe` (older .NET) → needs matching **x86** DLLs

Mixing x86 and x64 files causes silent failures or errors.

---

### 🔹 6. **Setup Process Recap**

| **Step** | **Action**                        | **Tool/File**          |
| -------- | --------------------------------- | ---------------------- |
| 1        | Extract SDR# zip                  | `sdrsharp-x86.zip`     |
| 2        | Install WinUSB driver             | `zadig.exe`            |
| 3        | Confirm device is detected        | `rtl_test.exe`         |
| 4        | Launch GUI                        | `SDRSharp.dotnet8.exe` |
| 5        | Select Source and start listening | GUI                    |

---

### 📌 Tip for GitHub Archiving

Store:

* `install notes.md` (this chapter)
* Clean `C:\SDRSharp\` minus EXEs (optional)
* Include links to source of DLLs and drivers
* Mention .NET version used

---