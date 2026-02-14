[app]
title = Student Leave App
package.name = studentleave
package.domain = org.college

source.dir = .
source.include_exts = py,kv,db,png,jpg,jpeg,ttf

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.permissions = INTERNET

# 🔒 FORCE STABLE ANDROID STACK
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
