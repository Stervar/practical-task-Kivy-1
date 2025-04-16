


"pip install buildozer"

buildozer init



Правильное название приложения: title = Kivy Image Viewer
Корректное имя пакета: package.name = kivyimageviewer

Домен пакета: package.domain = org.kivy
Требования: requirements = python3,kivy,pillow
Разрешения: android.permissions = android.permission.READ_EXTERNAL_STORAGE
Версии Android API: android.api = 31 и android.minapi = 21
Поддерживаемые архитектуры: android.archs = arm64-v8a, armeabi-v7a



buildozer -v android debug


buildozer --help


pip list | grep python-for-android


pip list



pip install python-for-android



python -m pip install --upgrade pip



pip install --upgrade buildozer


buildozer android debug






Сборка через WSL (рекомендуется):

Установите WSL (Windows Subsystem for Linux)
В терминале WSL выполните:
sudo apt update && sudo apt install -y python3-pip
pip3 install buildozer
buildozer init
buildozer android debug
Сборка через Docker:

docker run -it --rm -v "%cd%":/home/user/hostcwd kivy/buildozer android debug
Ручная сборка через python-for-android:

p4a apk --requirements=python3,kivy,pillow --private . --package=org.kivy.kivyimageviewer --name "Kivy  Image Viewer"I
