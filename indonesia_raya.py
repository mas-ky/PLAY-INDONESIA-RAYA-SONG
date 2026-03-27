import time
from datetime import datetime
import winsound
import os

from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# ==============================
# PENGATURAN
# ==============================

AUDIO_FILE = "Indonesia_Raya.wav"
PLAY_TIMES = ["10:00"]

last_played_date = {}

# ==============================
# SET VOLUME FIX (0% - 100%)
# ==============================

def set_volume_percent(percent):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Set volume (0.0 - 1.0)
    volume.SetMasterVolumeLevelScalar(percent / 100.0, None)

# ==============================
# LOOP UTAMA
# ==============================

print("Program berjalan (volume FIX)...")

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    today = now.date()

    if current_time in PLAY_TIMES:
        if last_played_date.get(current_time) != today:
            if os.path.exists(AUDIO_FILE):
                print(f"Memutar lagu jam {current_time}")

                # Volume ke 50%
                set_volume_percent(50)

                # Putar lagu
                winsound.PlaySound(AUDIO_FILE, winsound.SND_FILENAME)

                # Setelah selesai → volume ke 0%
                set_volume_percent(0)

                last_played_date[current_time] = today
            else:
                print("File audio tidak ditemukan!")

    time.sleep(20)