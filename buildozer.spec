
[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
presplash.filename = %(source.dir)s/data/presplash.png
icon.filename = %(source.dir)s/data/icon.png

[buildozer]
log_level = 2
warn_on_root = 1

# Android specific
[android]
# Android SDK and NDK paths will be auto-detected in WSL
# (Will be set after WSL installation completes)
android.accept_sdk_license = True
android.arch = armeabi-v7a

# Android permissions
android.permissions = INTERNET

# Android API
android.api = 30
android.minapi = 21
android.ndk = 19c
android.sdk = 22
android.gradle_dependencies = 'com.android.tools.build:gradle:3.5.4'

# Kivy requirements
requirements = python3,kivy==2.1.0,android
