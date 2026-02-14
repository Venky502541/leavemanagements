[app]
title = Student Leave App
package.name = studentleave
package.domain = org.college

# App source
source.dir = .
source.include_exts = py,kv,db,png,jpg,jpeg,ttf

# Version
version = 0.1

# Requirements
requirements = python3,kivy

# App orientation
orientation = portrait
fullscreen = 1

# Android permissions
android.permissions = INTERNET

# Android versions (STABLE – no preview)
android.api = 33
android.minapi = 21

# IMPORTANT: prevent preview / RC tools
android.build_tools_version = 33.0.2
android.ndk = 25b

# Automatically accept licenses (fixes your error)
android.accept_sdk_license = True

# Architecture
android.archs = arm64-v8a,armeabi-v7a


[buildozer]
log_level = 2
warn_on_root = 0
