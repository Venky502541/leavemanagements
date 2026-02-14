[app]
title = Student Leave App
package.name = studentleave
package.domain = org.college

source.dir = .
source.include_exts = py,kv,db,png,jpg,ttf

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.permissions = INTERNET
android.api = 33
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
