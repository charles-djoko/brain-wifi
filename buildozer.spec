[app]
title = Brain Wi-Fi Direct
package.name = brainwifidirect
package.domain = org.brain
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
version = 1.0
requirements = python3,kivy,plyer,jnius
orientation = portrait
fullscreen = 0
android.permissions = ACCESS_WIFI_STATE, CHANGE_WIFI_STATE, ACCESS_FINE_LOCATION, INTERNET, ACCESS_NETWORK_STATE
android.api = 31
android.minapi = 21
android.sdk = 30
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
