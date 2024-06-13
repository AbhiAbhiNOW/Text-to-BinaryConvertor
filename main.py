from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass, cast
    from android.permissions import request_permissions, Permission

class MainApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.input_text = TextInput(hint_text="Enter text")
        self.layout.add_widget(self.input_text)

        self.binary_text = Label(text="Binary output will be shown here")
        self.layout.add_widget(self.binary_text)

        self.button = Button(text="Convert to Binary and Send to Arduino")
        self.button.bind(on_press=self.convert_and_send)
        self.layout.add_widget(self.button)

        if platform == 'android':
            request_permissions([Permission.INTERNET, Permission.USB_PERMISSION])

        return self.layout

    def convert_and_send(self, instance):
        text = self.input_text.text
        binary_string = self.convert_to_binary(text)
        self.binary_text.text = binary_string

        if platform == 'android':
            self.send_to_arduino(binary_string)

    def convert_to_binary(self, text):
        binary = ' '.join(format(ord(char), '08b') for char in text)
        return binary

    def send_to_arduino(self, data):
        UsbManager = autoclass('android.hardware.usb.UsbManager')
        UsbAccessory = autoclass('android.hardware.usb.UsbAccessory')
        UsbDeviceConnection = autoclass('android.hardware.usb.UsbDeviceConnection')
        ParcelFileDescriptor = autoclass('android.os.ParcelFileDescriptor')
        FileOutputStream = autoclass('java.io.FileOutputStream')

        activity = autoclass('org.kivy.android.PythonActivity').mActivity
        usb_manager = activity.getSystemService(activity.USB_SERVICE)

        accessory_list = usb_manager.getAccessoryList()
        if accessory_list is None:
            self.binary_text.text = "No accessory found"
            return

        accessory = accessory_list[0]
        if not usb_manager.hasPermission(accessory):
            self.binary_text.text = "No permission to access USB"
            return

        connection = usb_manager.openAccessory(accessory)
        if connection is None:
            self.binary_text.text = "Failed to open accessory"
            return

        file_descriptor = connection.getFileDescriptor()
        if file_descriptor is None:
            self.binary_text.text = "Failed to get file descriptor"
            return

        output_stream = FileOutputStream(file_descriptor)
        output_stream.write(data.encode('utf-8'))
        output_stream.close()
        connection.close()

if __name__ == '__main__':
    MainApp().run()
