<div align="center">

# ☠️ Fake Virus Prank Simulator (Apex Threat Edition) 🎭

**A hyper-realistic, safe desktop prank simulator designed for friendly trolling.**

[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Safety](https://img.shields.io/badge/Safety-100%25%20Harmless-brightgreen?style=for-the-badge)]()

<p align="center">
  <i>Starts directly over the victim's real Windows desktop, escalates into a Hollywood-grade cyber ransomware lockdown, and culminates in the ultimate comedic reveal: <b>"You become fool! 🤡😂"</b></i>
</p>

</div>

---

## ⚠️ Important Safety & Ethical Disclaimer
> **FOR ENTERTAINMENT & EDUCATIONAL PURPOSES ONLY.**  
> This project is a **100% harmless simulation**:
> - **ZERO files are opened, modified, encrypted, or deleted.** (It only reads file *path names* to display on screen).
> - **ZERO changes are made to the Windows Registry, startup items, or system files.**
> - **Immediate Emergency Escape:** Pressing <kbd>ESC</kbd> or <kbd>Alt</kbd>+<kbd>F4</kbd> closes the program instantly at any millisecond.
> - Do not use this software maliciously or without the intent of a harmless prank between friends.

---

## 🎬 How The Prank Works

```
[Double Click run_prank.bat]
           │
           ▼
[Stage 1: Real Desktop Hijack] ──► Authentic Windows Defender Warning pops up directly over desktop
           │
           ▼
[Stage 2: Cascading Errors]    ──► Realistic system error dialogs cascade across the screen
           │
           ▼
[Stage 3: Fullscreen Lockdown] ──► Screen locked into LockBit / WannaCry Ransomware interface
                                   ├─ Robotic SAPI Voice warning through speakers
                                   ├─ Real Personal File Shredder (scans actual filenames)
                                   ├─ Low-level Hex MBR zero-fill disassembly terminal
                                   ├─ Elevated cmd.exe execution simulation
                                   ├─ Ghost RAT targeting cursor navigating files
                                   ├─ Live CPU temp (102°C) & Webcam exfiltration HUD
                                   └─ Oscillating alarm siren & Windows error wavs
           │
           ▼
[Stage 4: Glitch & Silence]    ──► Graphic glitch strobe & 1-second suspense blackout
           │
           ▼
[Stage 5: Grand Reveal 🎉]     ──► Confetti shower + fireworks + laughing voice + editable message
```

---

## ⚡ Key Features

- **🔊 Authentic Windows SFX Engine:** Uses genuine Windows audio files (`Windows User Account Control.wav`, `Windows Critical Stop.wav`, `Windows Hardware Remove.wav`, `Alarm01.wav`, `tada.wav`).
- **🗣️ Multi-Stage Robotic Windows Voice (TTS):** Speaks out loud via Windows SAPI during launch, midway, and the final 5-second countdown.
- **📂 Real Personal Filename Streaming:** Safely reads actual filenames from `Desktop`, `Downloads`, and `Documents` (read-only) and flashes them as `[ENCRYPTING] ... SHA-256 [LOCKED]`.
- **💻 Simulated Elevated `cmd.exe`:** Embedded Command Prompt executing `vssadmin delete shadows`, `cipher /w:`, and `bcdedit`.
- **🔴 Low-Level Hex Sector Disassembly:** Live memory hex feed overwriting sector addresses with `00 00 00 00 [ZERO-FILLED]`.
- **🎯 Ghost RAT Hacker Cursor:** Animated targeting cursor sweeping across screen elements.
- **🎨 3 Switchable Themes:**
  - `ransomware`: LockBit / WannaCry dark red split layout (Default).
  - `hacker`: Cyber Matrix green penetration terminal with falling code.
  - `bsod`: Hyper-realistic Windows 11 Blue Screen of Death crash with percentage counter.
- **🎉 Customizable Grand Reveal:**
  - 140 animated falling colorful confetti particles.
  - Bouncing meme emojis (`🤡 🤣 🥳 🎉 😆 💀 🎭`).
  - **"Rave Party 🌈"** button to shift party colors.
  - **"Copy Prank Joke 📋"** button (copies brag text to clipboard).
  - **"Prank Again 🔄"** replay button.

---

## 🚀 Quick Start

### Option 1: 1-Click Launch (Recommended)
Simply double-click:
```bat
run_prank.bat
```
*(Uses `pyw` to launch instantly with zero background console window).*

### Option 2: Run via Terminal
```bash
# Clone the repository
git clone https://github.com/your-username/fake-virus-prank.git
cd fake-virus-prank

# Optional: install pywin32 for enhanced voice/audio support
pip install -r requirements.txt

# Run
python fake_virus.py
```

---

## ✏️ Customization (`config.json`)

All texts, timers, and toggles can be customized without touching any code inside `config.json`:

```json
{
  "theme": "ransomware",
  "victim_name": "auto",
  "countdown_seconds": 15,
  "scary_title": "CRITICAL THREAT: RANSOMWARE.LOCKBIT.BLACK KERNEL OVERRIDE",
  "popup_title": "🎉 GOTCHA! PRANK ALERT! 😂",
  "popup_message": "You become fool! 🤡😂\n\nChill out, bro! It's just a prank!\nNO files were touched, deleted, or harmed.\nYour PC is 100% safe and sound! ❤️",
  "button_text": "Close Prank & Forgive Me 😆",
  "replay_button_text": "Prank Someone Else 🔄",
  "enable_authentic_sfx": true,
  "enable_voice_speech": true,
  "enable_alarm_siren": true,
  "enable_screen_shake": true,
  "enable_cascading_popups": true,
  "scan_real_filenames": true,
  "enable_webcam_spoof": true,
  "enable_hardware_telemetry": true,
  "enable_hex_sector_wipe": true,
  "enable_ghost_cursor": true,
  "enable_cmd_simulation": true
}
```

| Setting | Type | Description |
| :--- | :---: | :--- |
| `popup_message` | string | The message shown to your friend when the prank is revealed. |
| `countdown_seconds` | int | Length of the countdown timer before reveal (default: `15`). |
| `theme` | string | Visual theme: `"ransomware"`, `"hacker"`, or `"bsod"`. |
| `victim_name` | string | `"auto"` automatically pulls their Windows username, or enter a nickname. |
| `enable_authentic_sfx` | bool | Plays genuine Windows `.wav` sounds from `C:\Windows\Media`. |
| `enable_voice_speech` | bool | Enables spoken robotic voice announcements via Windows SAPI. |
| `scan_real_filenames` | bool | Streams real filenames from Desktop/Downloads (read-only). |

---

## 🛡️ Secret Emergency Hotkey (For The Prankster)

If you ever need to abort or close the prank at any second:
- Press <kbd>Escape</kbd> or <kbd>Alt</kbd>+<kbd>F4</kbd>
- The program cleanly terminates all threads, sounds, and windows immediately.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
