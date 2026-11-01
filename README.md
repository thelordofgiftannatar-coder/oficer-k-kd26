# Officer K – build the APK on GitHub

1. Create a new **empty repository** on GitHub (e.g. `officer-k-app`).
2. Upload everything from this folder (on github.com: *Add file → Upload files*, drag all files and folders, including the hidden `.github` folder), then commit to `main`.
3. Open the **Actions** tab → **Build APK** (it starts by itself; or press *Run workflow*).
4. When it turns green (about 5–10 min), open the run and download **officer-k-apk** under *Artifacts*. Unzip it and install `app-debug.apk` on your phone (allow "Install unknown apps").

## Updating the app
Replace `www/index.html` with the new version and commit. The APK is rebuilt automatically.

## Notes
- `www/` holds the app (index.html, icons, manifest). Everything else only builds it.
- The lock-screen player, device scan and "write tags into songs" rely on a custom native plugin named `LocalMusic`. It is not part of this project, so in this build those features fall back to the web versions (picking files by hand). Everything else works, including wallpapers, themes and the redesigned menus.
- This produces a *debug* APK, fine for personal use. A Play Store release needs a signing key.
