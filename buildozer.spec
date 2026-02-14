[app]
# ================= APP INFO =================
title = Student Leave App
package.name = studentleave
package.domain = org.college

# ================= SOURCE ==================
source.dir = .
source.include_exts = py,kv,db,png,jpg,jpeg,ttf

# ================= VERSION =================
version = 0.1

# ================= REQUIREMENTS ============
requirements = python3,kivy

# ================= UI SETTINGS =============
orientation = portrait
fullscreen = 1

# ================= ANDROID SETTINGS ========
android.permissions = INTERNET

# ---- FORCE STABLE ANDROID VERSIONS (IMPORTANT) ----
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2
android.ndk = 25b

# ================= BUILD SETTINGS ==========
[buildozer]
log_level = 2
warn_on_root = 1
