#!/usr/bin/env python3
"""
Hyper-Realistic Safe Fake Virus Simulator v7.0 (Authentic SFX & VFX Master Edition)
100% Harmless - No files, registry keys, or settings are ever modified.
Zero giveaways during the attack phase.
Press ESC at any moment to immediately close.
"""

import sys
import os
import json
import time
import math
import random
import socket
import platform
import threading
import tkinter as tk
from tkinter import font

# Try importing winsound for authentic Windows audio
try:
    import winsound
    HAS_WINSOUND = True
except ImportError:
    HAS_WINSOUND = False

# Try importing COM for Windows SAPI robotic text-to-speech voice
try:
    import pythoncom
    import win32com.client
    HAS_TTS = True
except ImportError:
    HAS_TTS = False

DEFAULT_CONFIG = {
  "theme": "ransomware",
  "victim_name": "auto",
  "countdown_seconds": 15,
  "scary_title": "CRITICAL THREAT: RANSOMWARE.LOCKBIT.BLACK KERNEL OVERRIDE",
  "popup_title": "🎉 GOTCHA! PRANK ALERT! 😂",
  "popup_message": "You become fool! 🤡😂\n\nChill out, bro! It's just a prank!\nNO files were touched, deleted, or harmed.\nYour PC is 100% safe and sound! ❤️",
  "button_text": "Close Prank & Forgive Me 😆",
  "replay_button_text": "Prank Someone Else 🔄",
  "enable_authentic_sfx": True,
  "enable_voice_speech": True,
  "enable_sound": True,
  "enable_alarm_siren": True,
  "enable_screen_shake": True,
  "enable_cascading_popups": True,
  "scan_real_filenames": True,
  "enable_webcam_spoof": True,
  "enable_hardware_telemetry": True,
  "enable_hex_sector_wipe": True,
  "enable_ghost_cursor": True,
  "enable_matrix_rain": True,
  "enable_cmd_simulation": True,
  "speech_on_start": "Warning! Severe rootkit breach detected. Master Boot Record corrupted. File destruction sequence initiated.",
  "speech_on_midway": "Hardware failure imminent. Exfiltrating personal documents and passwords to darknet server.",
  "speech_on_countdown_5": "Permanent system zero-fill in five seconds. Four. Three. Two. One.",
  "speech_on_reveal": "Ha ha ha! You have been pranked! You become fool!",
  "fake_logs": [
    "[KERNEL_PANIC] Ring-0 memory hook established at 0x7FFE0000",
    "[SECURITY_BYPASS] Windows Defender Antivirus service terminated (PID 3044)",
    "[SHADOW_COPIES] Purging volume shadow storage: vssadmin delete shadows /all /quiet",
    "[BCDEdit] Recovery environment disabled: bcdedit /set {default} bootstatuspolicy ignoreallfailures",
    "[TPM_INVALIDATE] Physical TPM security module locked out",
    "[ENCRYPTION_ENGINE] Spawning 16 worker threads with AES-256 + RSA-4096 asymmetric cipher",
    "[DATA_EXFILTRATION] Establishing encrypted TLS tunnel to C2 server 185.220.101.4:443",
    "[MBR_DESTROY] Zero-filling Master Boot Record partition tables on Drive 0",
    "[PROCESS_TERMINATION] Terminated taskmgr.exe, procexp.exe, perfmon.exe, cmd.exe",
    "[NETWORK_ISOLATION] Overwriting DNS routing tables and disabling network adapters"
  ]
}


def load_config():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                merged = DEFAULT_CONFIG.copy()
                merged.update(data)
                return merged
        except Exception:
            pass
    return DEFAULT_CONFIG.copy()


def get_system_telemetry(config):
    """Gathers real system info to make the threat look 100% genuine."""
    try:
        user = config.get("victim_name", "auto")
        if not user or user == "auto":
            user = os.getlogin()
    except Exception:
        user = "Administrator"

    try:
        host = platform.node() or "WORKSTATION-01"
    except Exception:
        host = "WORKSTATION-01"

    try:
        os_info = f"{platform.system()} {platform.release()} (Build {platform.version().split('.')[-1]})"
    except Exception:
        os_info = "Windows 11 Pro x64"

    try:
        ip = socket.gethostbyname(socket.gethostname())
    except Exception:
        ip = "192.168.1.105"

    return {
        "user": user,
        "host": host,
        "os": os_info,
        "ip": ip
    }


def get_sample_files(max_files=80):
    """
    Safely reads ONLY file path names from user's Desktop/Downloads/Documents
    so the virus displays real personal filenames being 'encrypted'.
    ZERO files are opened, modified, or deleted.
    """
    user_home = os.path.expanduser("~")
    search_dirs = [
        os.path.join(user_home, "Desktop"),
        os.path.join(user_home, "Downloads"),
        os.path.join(user_home, "Documents"),
        os.path.join(user_home, "Pictures")
    ]
    files = []
    for d in search_dirs:
        if os.path.exists(d):
            try:
                for entry in os.scandir(d):
                    if entry.is_file() and not entry.name.startswith("."):
                        files.append(entry.path)
                        if len(files) >= max_files:
                            break
            except Exception:
                pass
        if len(files) >= max_files:
            break

    if not files:
        username = os.getlogin() if hasattr(os, "getlogin") else "User"
        files = [
            f"C:\\Users\\{username}\\Desktop\\Private_Keys.dat",
            f"C:\\Users\\{username}\\Documents\\Financial_Tax_Records_2026.xlsx",
            f"C:\\Users\\{username}\\Downloads\\Chrome_Setup.exe",
            f"C:\\Users\\{username}\\Pictures\\Personal_Vault.zip",
            f"C:\\Windows\\System32\\ntoskrnl.exe",
            f"C:\\Windows\\System32\\config\\SAM",
            f"C:\\Windows\\System32\\drivers\\etc\\hosts"
        ]
    random.shuffle(files)
    return files


class SFXEngine:
    """High-fidelity authentic Windows sound engine using genuine WAV files."""
    def __init__(self, enabled=True):
        self.enabled = enabled
        self.media_dir = r"C:\Windows\Media"

    def play_wav(self, filename, fallback_type="hand"):
        if not self.enabled or not HAS_WINSOUND:
            return
        def _play():
            try:
                wav_path = os.path.join(self.media_dir, filename)
                if os.path.exists(wav_path):
                    winsound.PlaySound(wav_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
                else:
                    self._play_fallback(fallback_type)
            except Exception:
                self._play_fallback(fallback_type)
        threading.Thread(target=_play, daemon=True).start()

    def _play_fallback(self, fallback_type):
        try:
            if fallback_type == "hand":
                winsound.MessageBeep(winsound.MB_ICONHAND)
            elif fallback_type == "exclamation":
                winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
            elif fallback_type == "asterisk":
                winsound.MessageBeep(winsound.MB_ICONASTERISK)
        except Exception:
            pass

    def play_uac(self):
        self.play_wav("Windows User Account Control.wav", "exclamation")

    def play_critical_stop(self):
        self.play_wav("Windows Critical Stop.wav", "hand")

    def play_hardware_disconnect(self):
        self.play_wav("Windows Hardware Remove.wav", "hand")

    def play_alarm(self):
        self.play_wav("Alarm01.wav", "exclamation")

    def play_victory(self):
        self.play_wav("tada.wav", "asterisk")


class MasterFakeVirus:
    def __init__(self, root):
        self.root = root
        self.config = load_config()
        self.telemetry = get_system_telemetry(self.config)
        self.sfx = SFXEngine(enabled=self.config.get("enable_authentic_sfx", True))
        self.is_running = True
        self.revealed = False
        self.siren_active = False

        if self.config.get("scan_real_filenames", True):
            self.sample_files = get_sample_files()
        else:
            self.sample_files = []

        self.fake_logs = list(self.config.get("fake_logs", DEFAULT_CONFIG["fake_logs"]))

        # Window settings
        self.root.title("Windows Host Process (Rundll32)")
        self.root.configure(bg="#000000")

        # Global emergency escape bindings (INVISIBLE TO VICTIM)
        for key in ["<Escape>", "<Alt-F4>", "<Control-q>", "<Control-c>"]:
            self.root.bind(key, self.emergency_exit)

        # Countdown parameters
        self.total_seconds = max(4, int(self.config.get("countdown_seconds", 15)))
        self.remaining_seconds = self.total_seconds
        self.said_midway = False
        self.said_countdown_5 = False

        self.popups = []

        # Ghost Cursor State
        self.ghost_x = 420
        self.ghost_y = 360
        self.ghost_tx = 720
        self.ghost_ty = 480
        self.ghost_lbl = None

        # Simulated CMD execution lines
        self.cmd_scripts = [
            ("C:\\Windows\\System32> vssadmin.exe delete shadows /all /quiet", "#ffffff"),
            ("Successfully deleted 4 volume shadow copies from drive C:\\", "#38bdf8"),
            ("C:\\Windows\\System32> bcdedit /set {default} bootstatuspolicy ignoreallfailures", "#ffffff"),
            ("The operation completed successfully.", "#22c55e"),
            ("C:\\Windows\\System32> cipher.exe /w:C:\\Users\\", "#ffffff"),
            ("Writing zero-byte clusters to user directory partition...", "#f59e0b"),
            ("C:\\Windows\\System32> net stop WinDefend /y", "#ffffff"),
            ("The Windows Defender Antivirus Service service was stopped successfully.", "#ef4444"),
            ("C:\\Windows\\System32> format \\\\?\\Volume{8c142b} /fs:NTFS /q /y", "#ffffff"),
            ("Formatting raw sector table... MBR checksum invalid.", "#dc2626")
        ]

        # Start sequence: Stage 1 (Fake Windows Alert on desktop) or direct virus screen
        if self.config.get("enable_cascading_popups", True):
            self.root.withdraw()
            self.start_fake_defender_alert()
        else:
            self.start_main_virus_screen()

    # ==========================================
    # AUDIO & ROBOTIC TTS VOICE ENGINE
    # ==========================================
    def speak_async(self, text):
        if not HAS_TTS or not self.config.get("enable_voice_speech", True) or not text:
            return
        def _tts():
            try:
                pythoncom.CoInitialize()
                try:
                    speaker = win32com.client.Dispatch("SAPI.SpVoice")
                    speaker.Rate = 1
                    speaker.Volume = 100
                    speaker.Speak(text)
                finally:
                    pythoncom.CoUninitialize()
            except Exception:
                pass
        threading.Thread(target=_tts, daemon=True).start()

    def play_countdown_beep(self, ratio):
        if not HAS_WINSOUND or not self.config.get("enable_sound", True):
            return
        freq = int(700 + (ratio * 1500))
        dur = max(40, int(120 - (ratio * 75)))
        def _b():
            try:
                winsound.Beep(freq, dur)
            except Exception:
                pass
        threading.Thread(target=_b, daemon=True).start()

    def start_alarm_siren(self):
        if not HAS_WINSOUND or not self.config.get("enable_alarm_siren", True) or self.siren_active:
            return
        self.siren_active = True
        def _siren():
            # Play real Windows alarm wav if available or oscillate frequency
            media_alarm = r"C:\Windows\Media\Alarm01.wav"
            if os.path.exists(media_alarm):
                try:
                    winsound.PlaySound(media_alarm, winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
                    return
                except Exception:
                    pass
            while self.is_running and not self.revealed:
                for f in range(800, 1250, 75):
                    if not self.is_running or self.revealed:
                        return
                    try:
                        winsound.Beep(f, 32)
                    except Exception:
                        pass
                for f in range(1250, 800, -75):
                    if not self.is_running or self.revealed:
                        return
                    try:
                        winsound.Beep(f, 32)
                    except Exception:
                        pass
                time.sleep(0.25)
        threading.Thread(target=_siren, daemon=True).start()

    def stop_alarm_siren(self):
        self.siren_active = False
        if HAS_WINSOUND:
            try:
                winsound.PlaySound(None, winsound.SND_PURGE)
            except Exception:
                pass

    # ==========================================
    # EMERGENCY EXIT (SECRET SHORTCUT)
    # ==========================================
    def emergency_exit(self, event=None):
        self.is_running = False
        self.stop_alarm_siren()
        for p in self.popups:
            try:
                p.destroy()
            except Exception:
                pass
        try:
            self.root.destroy()
        except Exception:
            pass
        sys.exit(0)

    # ==========================================
    # STAGE 1: AUTHENTIC WINDOWS DEFENDER ALERT
    # Appears natively on the user's real desktop
    # ==========================================
    def start_fake_defender_alert(self):
        self.sfx.play_uac()

        alert = tk.Toplevel(self.root)
        alert.title("Windows Security - Severe Threat Detected")
        alert.geometry("540x265")
        alert.resizable(False, False)
        alert.attributes("-topmost", True)
        alert.configure(bg="#f3f3f3")

        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        ax = (sw - 540) // 2
        ay = (sh - 265) // 2
        alert.geometry(f"+{ax}+{ay}")
        alert.bind("<Escape>", self.emergency_exit)
        self.popups.append(alert)

        hdr = tk.Frame(alert, bg="#ffffff", height=65)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)

        icon_cv = tk.Canvas(hdr, width=44, height=44, bg="#ffffff", highlightthickness=0)
        icon_cv.pack(side="left", padx=16, pady=10)
        icon_cv.create_oval(3, 3, 41, 41, fill="#e81123", width=0)
        icon_cv.create_line(14, 14, 30, 30, fill="#ffffff", width=3)
        icon_cv.create_line(30, 14, 14, 30, fill="#ffffff", width=3)

        title_lbl = tk.Label(
            hdr,
            text="Threat Detected: Trojan:Win32/LockBit.KernelBypass",
            font=("Segoe UI", 11, "bold"),
            fg="#111827",
            bg="#ffffff"
        )
        title_lbl.pack(side="left", pady=14)

        body = tk.Frame(alert, bg="#f3f3f3", padx=20, pady=14)
        body.pack(fill="both", expand=True)

        info_text = (
            f"Category: Ransomware / Data Exfiltration\n"
            f"Target System: {self.telemetry['user']}@{self.telemetry['host']} ({self.telemetry['ip']})\n"
            f"Affected File: C:\\Windows\\System32\\ntoskrnl.exe\n"
            f"Status: Kernel Execution Active (Error 0x80070005: Access Denied)\n"
            f"Warning: Master Boot Record encryption sequence in progress."
        )
        lbl_info = tk.Label(
            body,
            text=info_text,
            font=("Segoe UI", 9),
            fg="#222222",
            bg="#f3f3f3",
            justify="left"
        )
        lbl_info.pack(anchor="w")

        btn_frame = tk.Frame(alert, bg="#f3f3f3", padx=15, pady=10)
        btn_frame.pack(fill="x", side="bottom")

        def proceed_to_cascade():
            try:
                alert.destroy()
            except Exception:
                pass
            self.trigger_cascading_errors()

        btn_quarantine = tk.Button(
            btn_frame,
            text="Quarantine Threat",
            font=("Segoe UI", 9, "bold"),
            bg="#0067b8",
            fg="#ffffff",
            activebackground="#005da6",
            activeforeground="#ffffff",
            width=16,
            command=proceed_to_cascade
        )
        btn_quarantine.pack(side="right", padx=6)

        btn_cancel = tk.Button(
            btn_frame,
            text="Cancel",
            font=("Segoe UI", 9),
            bg="#e1e1e1",
            fg="#000000",
            width=10,
            command=proceed_to_cascade
        )
        btn_cancel.pack(side="right", padx=6)

        self.root.after(3800, proceed_to_cascade)

    # ==========================================
    # STAGE 2: CASCADING ERROR POPUPS
    # Cascades directly on the user's real desktop
    # ==========================================
    def trigger_cascading_errors(self):
        error_titles = [
            "Critical Process Failure",
            "Kernel Memory Corruption",
            "Access Violation (0xc0000005)",
            "Hardware Controller Disconnect",
            "System32 Corrupted"
        ]
        error_msgs = [
            "Windows cannot access the specified device, path, or file.",
            "The instruction at 0x77F832 referenced memory that could not be read.",
            "Cryptographic hardware token provider failed to respond.",
            "USB Mass Storage / Secondary Controller disconnected unexpectedly.",
            "Master File Table (MFT) damaged. System failure imminent."
        ]

        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()

        def spawn_one(idx):
            if not self.is_running or self.revealed:
                return

            if idx == 3:
                self.sfx.play_hardware_disconnect()
            else:
                self.sfx.play_critical_stop()

            pop = tk.Toplevel(self.root)
            pop.title(error_titles[idx % len(error_titles)])
            pop.geometry("380x155")
            pop.resizable(False, False)
            pop.attributes("-topmost", True)
            pop.configure(bg="#f0f0f0")
            pop.bind("<Escape>", self.emergency_exit)
            self.popups.append(pop)

            rx = int(sw * 0.12 + (idx * 105) + random.randint(-35, 35))
            ry = int(sh * 0.14 + (idx * 85) + random.randint(-25, 25))
            pop.geometry(f"+{rx}+{ry}")

            top_f = tk.Frame(pop, bg="#f0f0f0", padx=16, pady=16)
            top_f.pack(fill="both", expand=True)

            ic = tk.Canvas(top_f, width=34, height=34, bg="#f0f0f0", highlightthickness=0)
            ic.pack(side="left", padx=(0, 12))
            ic.create_oval(2, 2, 32, 32, fill="#e81123", width=0)
            ic.create_line(10, 10, 24, 24, fill="#ffffff", width=3)
            ic.create_line(24, 10, 10, 24, fill="#ffffff", width=3)

            msg = tk.Label(
                top_f,
                text=error_msgs[idx % len(error_msgs)],
                font=("Segoe UI", 9),
                fg="#222222",
                bg="#f0f0f0",
                wraplength=270,
                justify="left"
            )
            msg.pack(side="left")

            bf = tk.Frame(pop, bg="#f0f0f0", pady=8)
            bf.pack(fill="x", side="bottom")
            btn = tk.Button(
                bf,
                text="OK",
                font=("Segoe UI", 9),
                width=10,
                bg="#e1e1e1",
                command=lambda: pop.destroy()
            )
            btn.pack(side="right", padx=16)

            if idx + 1 < len(error_titles):
                self.root.after(350, lambda: spawn_one(idx + 1))
            else:
                self.root.after(850, self.start_main_virus_screen)

        spawn_one(0)

    # ==========================================
    # STAGE 3: MAIN VIRUS LOCKDOWN SCREEN
    # ==========================================
    def start_main_virus_screen(self):
        for p in self.popups:
            try:
                p.destroy()
            except Exception:
                pass
        self.popups.clear()

        # Reveal root window and lock full screen
        self.root.deiconify()
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)

        self.speak_async(self.config.get("speech_on_start"))
        self.start_alarm_siren()

        theme = self.config.get("theme", "ransomware").lower()
        if theme == "bsod":
            self.build_bsod_ui()
        elif theme == "hacker":
            self.build_hacker_ui()
        else:
            self.build_ransomware_ui()

    # ==========================================
    # THEME A: RANSOMWARE (MASTER THREAT LAYOUT)
    # ==========================================
    def build_ransomware_ui(self):
        self.root.configure(bg="#05060b")

        # Top Red Flashing Alert Header
        self.rw_header = tk.Frame(self.root, bg="#880000", pady=7)
        self.rw_header.pack(fill="x", side="top")

        self.rw_title = tk.Label(
            self.rw_header,
            text=f"☠️  {self.config.get('scary_title')}  ☠️",
            font=("Consolas", 15, "bold"),
            fg="#ffffff",
            bg="#880000"
        )
        self.rw_title.pack()

        # Telemetry & Camera Bar
        telem_bar = tk.Frame(self.root, bg="#0e111a", pady=5)
        telem_bar.pack(fill="x", side="top")

        t_text = (
            f"TARGET: {self.telemetry['user']}@{self.telemetry['host']}  |  "
            f"IP: {self.telemetry['ip']}  |  "
            f"OS: {self.telemetry['os']}  |  "
            f"CIPHER: RSA-4096 / AES-256-GCM"
        )
        self.telem_label = tk.Label(
            telem_bar,
            text=t_text,
            font=("Consolas", 9, "bold"),
            fg="#fbbf24",
            bg="#0e111a"
        )
        self.telem_label.pack(side="left", padx=16)

        if self.config.get("enable_webcam_spoof", True):
            self.cam_indicator = tk.Label(
                telem_bar,
                text="🔴 [LIVE STREAM] WEBCAM 1080p & AUDIO EXFILTRATING (54.2 MB/s)",
                font=("Consolas", 9, "bold"),
                fg="#ef4444",
                bg="#0e111a"
            )
            self.cam_indicator.pack(side="right", padx=16)
            self.blink_camera_dot(True)

        if self.config.get("enable_hardware_telemetry", True):
            hw_bar = tk.Frame(self.root, bg="#180000", pady=2)
            hw_bar.pack(fill="x", side="top")

            self.hw_label = tk.Label(
                hw_bar,
                text="🔥 CPU CORE: 102.4°C [CRITICAL THERMAL RUNAWAY]  |  GPU: 99.8% (XMR MINING RIG)  |  DISK I/O: 1.6 GB/s ZERO-FILL",
                font=("Consolas", 8, "bold"),
                fg="#f87171",
                bg="#180000"
            )
            self.hw_label.pack()
            self.update_hardware_gauges()

        # Split Body (Left Panel, Middle Terminal, Right Hex Memory Wipe + CMD)
        body = tk.Frame(self.root, bg="#05060b")
        body.pack(fill="both", expand=True, padx=14, pady=6)

        # LEFT PANEL: Skull + Countdown Timer + Ransom
        left_panel = tk.Frame(body, bg="#0e1017", bd=2, relief="ridge", width=420)
        left_panel.pack(side="left", fill="both", padx=(0, 10))
        left_panel.pack_propagate(False)

        skull_ascii = (
            "      .ed\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"be.\n"
            "    -\"           .-.           \"-\n"
            "  .\"   .d88b.   /   \\   .d88b.   \".\n"
            " /    88888888 |     | 88888888    \\\n"
            ":     88888888  \\   /  88888888     :\n"
            ":      \"Y88P\"    '-'    \"Y88P\"      :\n"
            " \\          [ ALL FILES ]          /\n"
            "  '.        [ ENCRYPTED ]        .'\n"
            "    '-_______________________-'\n"
        )
        self.lbl_skull = tk.Label(
            left_panel,
            text=skull_ascii,
            font=("Courier", 8, "bold"),
            fg="#ef4444",
            bg="#0e1017",
            justify="center"
        )
        self.lbl_skull.pack(pady=(4, 2))

        lbl_warn = tk.Label(
            left_panel,
            text="ALL DISK SECTORS WIPED IN:",
            font=("Consolas", 10, "bold"),
            fg="#f87171",
            bg="#0e1017"
        )
        lbl_warn.pack(pady=(0, 2))

        # Massive Countdown LED
        self.timer_label = tk.Label(
            left_panel,
            text=f"00:{self.remaining_seconds:02d}",
            font=("Consolas", 42, "bold"),
            fg="#ff0033",
            bg="#0e1017"
        )
        self.timer_label.pack(pady=2)

        # Progress bar
        self.progress_canvas = tk.Canvas(left_panel, height=18, bg="#2d0505", highlightthickness=0)
        self.progress_canvas.pack(fill="x", padx=20, pady=6)
        self.progress_bar = self.progress_canvas.create_rectangle(0, 0, 0, 18, fill="#dc2626", width=0)

        # Bitcoin Ransom instructions
        btc_box = tk.Label(
            left_panel,
            text=(
                "PAYMENT REQUIRED FOR PRIVATE KEY:\n"
                "Send 0.5 BTC to: 1BoatSLRHtKNngkd\n\n"
                "⚠️ DO NOT RESTART OR POWER OFF PC\n"
                "Master Boot Record & TPM keys will be\n"
                "permanently purged when timer hits 00:00."
            ),
            font=("Consolas", 8),
            fg="#94a3b8",
            bg="#0e1017",
            justify="center"
        )
        btc_box.pack(pady=(2, 6))

        # Audio visualizer / waveform graph
        self.wave_canvas = tk.Canvas(left_panel, height=42, bg="#05070c", highlightthickness=0)
        self.wave_canvas.pack(fill="x", padx=16, pady=4)
        self.wave_bars = []
        for i in range(24):
            x0 = i * 16 + 8
            b = self.wave_canvas.create_rectangle(x0, 38, x0 + 10, 42, fill="#ef4444", width=0)
            self.wave_bars.append(b)
        self.animate_waveform()

        # CENTER & RIGHT CONTAINER
        center_box = tk.Frame(body, bg="#05060b")
        center_box.pack(side="left", fill="both", expand=True)

        # File Shredder Terminal
        term_header = tk.Label(
            center_box,
            text="── [ REAL-TIME SYSTEM FILE SHREDDER & ENCRYPTOR ] ─────────────────────────",
            font=("Consolas", 9, "bold"),
            fg="#ef4444",
            bg="#040508",
            anchor="w"
        )
        term_header.pack(fill="x", pady=(0, 2))

        self.log_text = tk.Text(
            center_box,
            bg="#040508",
            fg="#22c55e",
            font=("Consolas", 9),
            bd=1,
            relief="solid",
            padx=10,
            pady=5,
            wrap="word",
            state="disabled",
            height=13
        )
        self.log_text.pack(fill="both", expand=True)

        # Split Lower Frame (Left: Hex Memory Wipe, Right: Elevated Command Prompt)
        lower_frame = tk.Frame(center_box, bg="#05060b")
        lower_frame.pack(fill="x", pady=(6, 0))

        # Left lower: Hex Memory Wipe
        hex_box = tk.Frame(lower_frame, bg="#040508", bd=1, relief="solid")
        hex_box.pack(side="left", fill="both", expand=True, padx=(0, 5))

        hex_header = tk.Label(
            hex_box,
            text="── [ LOW-LEVEL MBR & SECTOR ZERO-FILL (DRIVE 0) ] ────",
            font=("Consolas", 8, "bold"),
            fg="#38bdf8",
            bg="#040508",
            anchor="w"
        )
        hex_header.pack(fill="x", padx=4, pady=2)

        self.hex_text = tk.Text(
            hex_box,
            bg="#020306",
            fg="#f43f5e",
            font=("Consolas", 8),
            bd=0,
            padx=6,
            pady=3,
            state="disabled",
            height=8
        )
        self.hex_text.pack(fill="both", expand=True)

        # Right lower: Simulated Elevated Command Prompt
        cmd_box = tk.Frame(lower_frame, bg="#000000", bd=1, relief="solid")
        cmd_box.pack(side="right", fill="both", expand=True)

        cmd_header = tk.Label(
            cmd_box,
            text="── [ C:\\Windows\\System32\\cmd.exe - ELEVATED ] ─────────",
            font=("Consolas", 8, "bold"),
            fg="#eab308",
            bg="#111111",
            anchor="w"
        )
        cmd_header.pack(fill="x", padx=4, pady=2)

        self.cmd_text = tk.Text(
            cmd_box,
            bg="#000000",
            fg="#cccccc",
            font=("Consolas", 8),
            bd=0,
            padx=6,
            pady=3,
            state="disabled",
            height=8
        )
        self.cmd_text.pack(fill="both", expand=True)

        # Ghost Laser Cursor (Visual element on screen)
        if self.config.get("enable_ghost_cursor", True):
            self.ghost_lbl = tk.Label(
                self.root,
                text="🎯 [C2_RAT_ACTIVE]",
                font=("Consolas", 9, "bold"),
                fg="#ff0044",
                bg="#1a0008",
                bd=1,
                relief="solid"
            )
            self.ghost_lbl.place(x=self.ghost_x, y=self.ghost_y)
            self.root.after(300, self.animate_ghost_cursor)

        # Kick off background loops
        self.append_log("[PAYLOAD ACTIVATED] Injected into svchost.exe (PID: 4120)...", "#facc15")
        self.append_log(f"[TARGET IDENTIFIED] Host: {self.telemetry['host']} | User: {self.telemetry['user']}", "#38bdf8")
        self.flash_header(True)
        self.pulse_skull(True)
        self.root.after(200, self.stream_shredder_logs)
        self.root.after(150, self.stream_hex_wipe)
        self.root.after(600, self.stream_cmd_simulation)
        self.root.after(1000, self.update_countdown)

    # ==========================================
    # THEME B: HACKER MATRIX THEME
    # ==========================================
    def build_hacker_ui(self):
        self.root.configure(bg="#050505")

        self.rw_header = tk.Frame(self.root, bg="#006622", pady=10)
        self.rw_header.pack(fill="x", side="top")

        self.rw_title = tk.Label(
            self.rw_header,
            text=f"⚡ CYBER PENETRATION FRAMEWORK // KERNEL EXPLOIT ACTIVE ⚡",
            font=("Consolas", 15, "bold"),
            fg="#ffffff",
            bg="#006622"
        )
        self.rw_title.pack()

        body = tk.Frame(self.root, bg="#050505")
        body.pack(fill="both", expand=True, padx=25, pady=10)

        self.timer_label = tk.Label(
            body,
            text=f"MEMORY DUMP PURGE IN: 00:{self.remaining_seconds:02d}",
            font=("Consolas", 32, "bold"),
            fg="#22c55e",
            bg="#050505"
        )
        self.timer_label.pack(pady=8)

        self.progress_canvas = tk.Canvas(body, height=18, bg="#002200", highlightthickness=0)
        self.progress_canvas.pack(fill="x", padx=60, pady=(0, 10))
        self.progress_bar = self.progress_canvas.create_rectangle(0, 0, 0, 18, fill="#00ff66", width=0)

        self.log_text = tk.Text(
            body,
            bg="#050a05",
            fg="#00ff66",
            font=("Consolas", 10),
            bd=1,
            relief="solid",
            padx=14,
            pady=10,
            state="disabled"
        )
        self.log_text.pack(expand=True, fill="both")

        self.root.after(200, self.stream_shredder_logs)
        self.root.after(1000, self.update_countdown)

    # ==========================================
    # THEME C: WINDOWS BSOD THEME
    # ==========================================
    def build_bsod_ui(self):
        self.root.configure(bg="#0078d7")

        bsod_frame = tk.Frame(self.root, bg="#0078d7")
        bsod_frame.place(relx=0.12, rely=0.18, relwidth=0.76, relheight=0.7)

        emoticon = tk.Label(
            bsod_frame,
            text=":(",
            font=("Segoe UI", 110, "normal"),
            fg="#ffffff",
            bg="#0078d7"
        )
        emoticon.pack(anchor="w", pady=(0, 20))

        bsod_text = tk.Label(
            bsod_frame,
            text=f"Your PC ran into a problem and needs to restart. We're just\ncollecting some error info from {self.telemetry['user']}'s system,\nand then we'll restart for you.",
            font=("Segoe UI", 22, "normal"),
            fg="#ffffff",
            bg="#0078d7",
            justify="left"
        )
        bsod_text.pack(anchor="w", pady=(0, 30))

        self.bsod_percent = tk.Label(
            bsod_frame,
            text="0% complete",
            font=("Segoe UI", 24, "normal"),
            fg="#ffffff",
            bg="#0078d7"
        )
        self.bsod_percent.pack(anchor="w", pady=(0, 30))

        stop_code = tk.Label(
            bsod_frame,
            text=f"Stop code: CRITICAL_PROCESS_DIED\nWhat failed: ntoskrnl.exe",
            font=("Segoe UI", 12),
            fg="#e0e0e0",
            bg="#0078d7",
            justify="left"
        )
        stop_code.pack(anchor="w")

        self.bsod_progress = 0
        self.update_bsod()

    def update_bsod(self):
        if not self.is_running or self.revealed:
            return

        self.bsod_progress += int(100 / self.total_seconds)
        if self.bsod_progress >= 100:
            self.bsod_percent.configure(text="100% complete")
            self.trigger_glitch_and_reveal()
        else:
            self.bsod_percent.configure(text=f"{self.bsod_progress}% complete")
            if HAS_WINSOUND and self.config.get("enable_sound", True):
                try:
                    winsound.Beep(900, 80)
                except Exception:
                    pass
            self.root.after(1000, self.update_bsod)

    # ==========================================
    # VISUAL CONTROLLERS & ANIMATIONS
    # ==========================================
    def animate_waveform(self):
        if not self.is_running or self.revealed:
            return
        for i, bar in enumerate(self.wave_bars):
            h = random.randint(4, 38)
            x0 = i * 16 + 8
            col = "#ef4444" if h > 24 else "#f97316"
            try:
                self.wave_canvas.coords(bar, x0, 42 - h, x0 + 10, 42)
                self.wave_canvas.itemconfig(bar, fill=col)
            except Exception:
                pass
        self.root.after(80, self.animate_waveform)

    def animate_ghost_cursor(self):
        if not self.is_running or self.revealed or not self.ghost_lbl:
            return

        dx = self.ghost_tx - self.ghost_x
        dy = self.ghost_ty - self.ghost_y
        dist = math.hypot(dx, dy)

        if dist < 18:
            sw = self.root.winfo_screenwidth()
            sh = self.root.winfo_screenheight()
            self.ghost_tx = random.randint(int(sw * 0.2), int(sw * 0.8))
            self.ghost_ty = random.randint(int(sh * 0.2), int(sh * 0.8))
            try:
                self.ghost_lbl.configure(bg="#ffff00", fg="#000000")
                self.root.after(100, lambda: self.ghost_lbl.configure(bg="#1a0008", fg="#ff0044"))
            except Exception:
                pass
        else:
            speed = 14
            self.ghost_x += int((dx / dist) * speed)
            self.ghost_y += int((dy / dist) * speed)
            try:
                self.ghost_lbl.place(x=self.ghost_x, y=self.ghost_y)
            except Exception:
                pass

        self.root.after(50, self.animate_ghost_cursor)

    def blink_camera_dot(self, state):
        if not self.is_running or self.revealed:
            return
        fg_col = "#ef4444" if state else "#330000"
        try:
            self.cam_indicator.configure(fg=fg_col)
            self.root.after(450, lambda: self.blink_camera_dot(not state))
        except Exception:
            pass

    def update_hardware_gauges(self):
        if not self.is_running or self.revealed:
            return
        temp = round(random.uniform(99.2, 104.8), 1)
        volt = round(random.uniform(1.61, 1.74), 2)
        io_speed = round(random.uniform(1.3, 1.9), 1)
        txt = f"🔥 CPU CORE: {temp}°C [CRITICAL THERMAL RUNAWAY]  |  GPU: 99.8% (XMR MINING RIG)  |  DISK I/O: {io_speed} GB/s ZERO-FILL"
        try:
            self.hw_label.configure(text=txt)
            self.root.after(650, self.update_hardware_gauges)
        except Exception:
            pass

    def pulse_skull(self, state):
        if not self.is_running or self.revealed:
            return
        fg_col = "#ef4444" if state else "#7f1d1d"
        try:
            if hasattr(self, "lbl_skull"):
                self.lbl_skull.configure(fg=fg_col)
            self.root.after(550, lambda: self.pulse_skull(not state))
        except Exception:
            pass

    # ==========================================
    # HEX SECTOR WIPE STREAMER
    # ==========================================
    def stream_hex_wipe(self):
        if not self.is_running or self.revealed:
            return
        addr = hex(random.randint(0x00000000, 0x0FFFFFFF))[2:].upper().zfill(8)
        bytes_before = " ".join([f"{random.randint(0x10, 0xFF):02X}" for _ in range(8)])
        bytes_after = "00 00 00 00 00 00 00 00 [ZERO-FILLED]"
        line = f"0x{addr}: {bytes_before} --> {bytes_after}\n"

        try:
            self.hex_text.configure(state="normal")
            self.hex_text.insert("end", line)
            lines = self.hex_text.get("1.0", "end").splitlines()
            if len(lines) > 8:
                self.hex_text.delete("1.0", "2.0")
            self.hex_text.see("end")
            self.hex_text.configure(state="disabled")
        except Exception:
            pass

        self.root.after(random.randint(90, 220), self.stream_hex_wipe)

    # ==========================================
    # ELEVATED CMD EXECUTION STREAMER
    # ==========================================
    def stream_cmd_simulation(self):
        if not self.is_running or self.revealed:
            return

        if self.cmd_scripts:
            cmd_line, color = self.cmd_scripts.pop(0)
            self.cmd_scripts.append((cmd_line, color))
            try:
                self.cmd_text.configure(state="normal")
                tag_name = f"cmd_{random.randint(1000, 99999)}"
                self.cmd_text.tag_config(tag_name, foreground=color)
                self.cmd_text.insert("end", f"{cmd_line}\n", tag_name)
                lines = self.cmd_text.get("1.0", "end").splitlines()
                if len(lines) > 8:
                    self.cmd_text.delete("1.0", "2.0")
                self.cmd_text.see("end")
                self.cmd_text.configure(state="disabled")
            except Exception:
                pass

        self.root.after(random.randint(600, 1100), self.stream_cmd_simulation)

    # ==========================================
    # LOG STREAMING & FILE ENCRYPTION
    # ==========================================
    def append_log(self, text, color="#22c55e"):
        try:
            self.log_text.configure(state="normal")
            tag_name = f"t_{random.randint(1000, 99999)}"
            self.log_text.tag_config(tag_name, foreground=color)
            self.log_text.insert("end", f"{text}\n", tag_name)
            self.log_text.see("end")
            self.log_text.configure(state="disabled")
        except Exception:
            pass

    def stream_shredder_logs(self):
        if not self.is_running or self.revealed:
            return

        if self.sample_files and random.random() < 0.76:
            target_file = self.sample_files.pop(0)
            self.sample_files.append(target_file)
            tag = random.choice(["[ENCRYPTING]", "[SHREDDING]", "[CORRUPTING]", "[OVERWRITING]"])
            color = random.choice(["#ef4444", "#f87171", "#f97316"])
            hash_snippet = "".join(random.choices("0123456789abcdef", k=12))
            self.append_log(f"{tag} {target_file} -> SHA256:{hash_snippet}... [LOCKED]", color)
        elif self.fake_logs:
            log_line = self.fake_logs.pop(0)
            self.fake_logs.append(log_line)
            self.append_log(log_line, "#38bdf8")
        else:
            mem_addr = hex(random.randint(0x10000000, 0x7FFFFFFF))
            self.append_log(f"[ZERO-FILL] Partition sector {mem_addr} overwritten.", "#e11d48")

        delay = random.randint(110, 260)
        self.root.after(delay, self.stream_shredder_logs)

    def flash_header(self, state):
        if not self.is_running or self.revealed:
            return
        bg_col = "#990000" if state else "#550000"
        try:
            self.rw_header.configure(bg=bg_col)
            self.rw_title.configure(bg=bg_col)
            self.root.after(400, lambda: self.flash_header(not state))
        except Exception:
            pass

    # ==========================================
    # COUNTDOWN CONTROLLER
    # ==========================================
    def update_countdown(self):
        if not self.is_running or self.revealed:
            return

        self.remaining_seconds -= 1
        elapsed = self.total_seconds - self.remaining_seconds
        ratio = min(1.0, elapsed / self.total_seconds)

        if self.remaining_seconds == int(self.total_seconds / 2) and not self.said_midway:
            self.said_midway = True
            self.speak_async(self.config.get("speech_on_midway"))

        if self.remaining_seconds == 5 and not self.said_countdown_5:
            self.said_countdown_5 = True
            self.speak_async(self.config.get("speech_on_countdown_5"))

        if self.remaining_seconds > 0:
            self.play_countdown_beep(ratio)

        try:
            if hasattr(self, "timer_label"):
                self.timer_label.configure(
                    text=f"00:{max(0, self.remaining_seconds):02d}"
                )
            if hasattr(self, "progress_canvas"):
                w = self.progress_canvas.winfo_width()
                if w > 1:
                    self.progress_canvas.coords(self.progress_bar, 0, 0, int(w * ratio), 18)
        except Exception:
            pass

        if self.remaining_seconds <= 0:
            self.trigger_glitch_and_reveal()
        else:
            self.root.after(1000, self.update_countdown)

    # ==========================================
    # STAGE 4: GLITCH & SILENCE
    # ==========================================
    def trigger_glitch_and_reveal(self):
        self.stop_alarm_siren()
        self.sfx.play_critical_stop()

        def glitch_flash(step):
            if step > 8:
                self.root.configure(bg="#000000")
                for w in self.root.winfo_children():
                    w.destroy()
                self.root.after(750, self.reveal_prank)
                return
            col = "#ffffff" if (step % 2 == 0) else "#ff0000"
            self.root.configure(bg=col)
            self.root.after(60, lambda: glitch_flash(step + 1))

        glitch_flash(0)

    # ==========================================
    # STAGE 5: THE GRAND REVEAL (AUTHENTIC SFX)
    # ==========================================
    def reveal_prank(self):
        self.revealed = True
        self.stop_alarm_siren()
        self.root.configure(bg="#0b0f19")

        # Play authentic Windows celebration chime / tada!
        self.sfx.play_victory()
        self.speak_async(self.config.get("speech_on_reveal"))

        self.confetti_canvas = tk.Canvas(self.root, bg="#0b0f19", highlightthickness=0)
        self.confetti_canvas.pack(fill="both", expand=True)

        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()

        # 140 colorful falling confetti particles
        self.particles = []
        colors = ["#ff0055", "#00ffcc", "#ffcc00", "#38bdf8", "#a855f7", "#22c55e", "#f97316", "#ec4899", "#eab308"]
        for _ in range(140):
            self.particles.append({
                "x": random.randint(0, sw),
                "y": random.randint(-sh, 0),
                "speed": random.randint(4, 14),
                "size": random.randint(7, 16),
                "color": random.choice(colors),
                "id": None
            })

        for p in self.particles:
            p["id"] = self.confetti_canvas.create_oval(
                p["x"], p["y"], p["x"] + p["size"], p["y"] + p["size"],
                fill=p["color"], outline=""
            )

        # Center Prank Modal Card
        self.modal = tk.Frame(
            self.confetti_canvas,
            bg="#1e293b",
            bd=3,
            relief="ridge",
            padx=60,
            pady=35
        )
        self.confetti_canvas.create_window(sw // 2, sh // 2, window=self.modal)

        icon_label = tk.Label(
            self.modal,
            text="🤡 🤣 🥳 🎉 😆 💀 🎭",
            font=("Segoe UI Emoji", 40),
            bg="#1e293b",
            fg="#facc15"
        )
        icon_label.pack(pady=(0, 6))

        popup_title = self.config.get("popup_title", "🎉 GOTCHA! PRANK ALERT! 😂")
        title_label = tk.Label(
            self.modal,
            text=popup_title,
            font=("Consolas", 22, "bold"),
            bg="#1e293b",
            fg="#38bdf8"
        )
        title_label.pack(pady=(0, 8))

        div = tk.Frame(self.modal, height=2, bg="#334155")
        div.pack(fill="x", pady=(0, 14))

        popup_msg = self.config.get(
            "popup_message",
            "You become fool! 🤡😂\n\nChill out, bro! It's just a prank!\nNO files were touched, deleted, or harmed.\nYour PC is 100% safe and sound! ❤️"
        )
        msg_label = tk.Label(
            self.modal,
            text=popup_msg,
            font=("Consolas", 14),
            bg="#1e293b",
            fg="#f8fafc",
            justify="center",
            wraplength=640
        )
        msg_label.pack(pady=(0, 20))

        # Button Row
        btn_box = tk.Frame(self.modal, bg="#1e293b")
        btn_box.pack()

        def copy_brag():
            try:
                self.root.clipboard_clear()
                self.root.clipboard_append("I just got totally fooled by the ultimate fake virus prank! 😭🤣 No files harmed!")
                copy_btn.configure(text="Copied to Clipboard! ✅")
            except Exception:
                pass

        def toggle_rave():
            for p in self.particles:
                new_col = random.choice(colors)
                self.confetti_canvas.itemconfig(p["id"], fill=new_col)
            self.sfx.play_victory()

        copy_btn = tk.Button(
            btn_box,
            text="Copy Prank Joke 📋",
            font=("Consolas", 11, "bold"),
            bg="#8b5cf6",
            fg="#ffffff",
            activebackground="#7c3aed",
            activeforeground="#ffffff",
            bd=0,
            padx=14,
            pady=10,
            cursor="hand2",
            command=copy_brag
        )
        copy_btn.pack(side="left", padx=5)

        rave_btn = tk.Button(
            btn_box,
            text="Rave Party 🌈",
            font=("Consolas", 11, "bold"),
            bg="#ec4899",
            fg="#ffffff",
            activebackground="#db2777",
            activeforeground="#ffffff",
            bd=0,
            padx=14,
            pady=10,
            cursor="hand2",
            command=toggle_rave
        )
        rave_btn.pack(side="left", padx=5)

        replay_btn = tk.Button(
            btn_box,
            text=self.config.get("replay_button_text", "Prank Again 🔄"),
            font=("Consolas", 11, "bold"),
            bg="#0284c7",
            fg="#ffffff",
            activebackground="#0369a1",
            activeforeground="#ffffff",
            bd=0,
            padx=14,
            pady=10,
            cursor="hand2",
            command=self.replay_prank
        )
        replay_btn.pack(side="left", padx=5)

        close_btn = tk.Button(
            btn_box,
            text=self.config.get("button_text", "Close Prank & Forgive Me 😆"),
            font=("Consolas", 11, "bold"),
            bg="#22c55e",
            fg="#052e16",
            activebackground="#16a34a",
            activeforeground="#ffffff",
            bd=0,
            padx=16,
            pady=10,
            cursor="hand2",
            command=self.emergency_exit
        )
        close_btn.pack(side="left", padx=5)

        self.animate_confetti(sw, sh)

    def animate_confetti(self, sw, sh):
        if not self.is_running or not hasattr(self, "confetti_canvas"):
            return

        for p in self.particles:
            p["y"] += p["speed"]
            p["x"] += random.randint(-1, 1)
            if p["y"] > sh:
                p["y"] = random.randint(-60, 0)
                p["x"] = random.randint(0, sw)
            self.confetti_canvas.coords(
                p["id"],
                p["x"], p["y"], p["x"] + p["size"], p["y"] + p["size"]
            )

        self.root.after(35, lambda: self.animate_confetti(sw, sh))

    def replay_prank(self):
        for w in self.root.winfo_children():
            w.destroy()
        self.__init__(self.root)


def main():
    root = tk.Tk()
    app = MasterFakeVirus(root)
    root.mainloop()


if __name__ == "__main__":
    main()
