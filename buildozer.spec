[app]

# (str) Title of your application
title = TextToBinary

# (str) Package name
package.name = texttobinary

# (str) Package domain (needed for .java)
package.domain = org.example

# (str) Source code where the main.py is located
source.include_exts = py,png,jpg,kv,atlas

# (str) Directory where the application's source code is located
source.dir = .

# (str) Version number
version = 0.1

# (list) Application requirements
requirements = kivy,pyjnius

# (list) Permissions
android.permissions = INTERNET, USB_PERMISSION, USB_HOST

# (list) Supported platforms
android.archs = armeabi-v7a, arm64-v8a

# (str) Android SDK version to use
android.sdk = 29

# (str) Android NDK version to use
android.ndk = 21b

# (list) Supported platforms
android = true

