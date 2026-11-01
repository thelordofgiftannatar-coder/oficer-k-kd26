"""Adds the permissions the player needs to the generated Android manifest."""
import pathlib
p = pathlib.Path("android/app/src/main/AndroidManifest.xml")
x = p.read_text(encoding="utf-8")
perms = [
 "android.permission.INTERNET","android.permission.WAKE_LOCK",
 "android.permission.FOREGROUND_SERVICE","android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK",
 "android.permission.POST_NOTIFICATIONS","android.permission.READ_MEDIA_AUDIO",
 "android.permission.READ_MEDIA_VIDEO","android.permission.READ_MEDIA_IMAGES",
 "android.permission.SYSTEM_ALERT_WINDOW",
]
add = "".join(f'    <uses-permission android:name="{n}" />\n' for n in perms if n not in x)
if "READ_EXTERNAL_STORAGE" not in x:
    add += '    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" android:maxSdkVersion="32" />\n'
x = x.replace("<application", add + "\n    <application", 1)
if "usesCleartextTraffic" not in x:
    x = x.replace("<application", '<application android:usesCleartextTraffic="true"', 1)
p.write_text(x, encoding="utf-8")
print("Manifest patched")
