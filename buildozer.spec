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

# (str) NDK path
android.ndk_path = C:/Android/ndk/21.3.6528147

# (str) SDK path
android.sdk_path = C:/Android/cmdline-tools

# (str) NDK version
android.ndk = 21b


# (list) Supported platforms
android = true
