from wakeonlan import send_magic_packet
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.properties import ListProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.anchorlayout import AnchorLayout

# Set the window size
Window.size = (400, 300)

class RoundButton(ButtonBehavior, BoxLayout):
    """
    Custom round button using ButtonBehavior and BoxLayout.
    """
    background_color = ListProperty([1, 0, 0, 1])  # Red color by default

    def __init__(self, **kwargs):
        super(RoundButton, self).__init__(**kwargs)
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        """
        Draw a rounded rectangle as the button background.
        """
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.background_color)  # Set the button color
            RoundedRectangle(pos=self.pos, size=self.size, radius=[self.height / 2])

class WakeOnLANApp(App):
    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        # Label for instructions
        self.label = Label(
            text="Press the button to wake up the PC",
            font_size=20,
            size_hint=(1, 0.2)
        )
        main_layout.add_widget(self.label)

        # AnchorLayout to center the button
        anchor_layout = AnchorLayout(anchor_x="center", anchor_y="center")
        main_layout.add_widget(anchor_layout)

        # Round red button
        self.button = RoundButton(
            orientation="vertical",
            size_hint=(None, None),
            size=(200, 200),  # Make the button round by setting equal width and height
            background_color=[1, 0, 0, 1]  # Red color
        )
        self.button.bind(on_press=self.wake_up_pc)  # Bind button press to function

        # Add a label inside the button
        button_label = Label(
            text="Wake Up!",
            font_size=30,
            color=(1, 1, 1, 1)  # White text
        )
        self.button.add_widget(button_label)

        # Add the button to the AnchorLayout
        anchor_layout.add_widget(self.button)

        return main_layout

    def wake_up_pc(self, instance):
        """
        Send a Wake-on-LAN magic packet when the button is pressed.
        """
        try:
            # Replace with the MAC address of the device you want to wake up
            mac_address = "00:11:22:33:44:55"  # Example MAC address, replace with the actual one

            # Optional: Specify the IP address or broadcast address (e.g., '192.168.1.255')
            ip_address = "192.168.1.255"  # Broadcast address for the local network

            # Optional: Specify the port (default is 9)
            port = 9

            # Send the Wake-on-LAN magic packet
            send_magic_packet(mac_address, ip_address=ip_address, port=port)

            # Show a success message
            self.show_popup("Success", "Magic packet sent successfully!")
        except Exception as e:
            # Show an error message if something goes wrong
            self.show_popup("Error", f"An error occurred: {e}")

    def show_popup(self, title, message):
        """
        Show a popup with a message.
        """
        popup_layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        popup_label = Label(text=message, font_size=20)
        close_button = Button(text="Close", size_hint=(1, 0.2))
        popup = Popup(title=title, content=popup_layout, size_hint=(0.8, 0.4))

        # Bind the close button to dismiss the popup
        close_button.bind(on_press=popup.dismiss)

        # Add widgets to the popup layout
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(close_button)

        # Open the popup
        popup.open()

if __name__ == "__main__":
    WakeOnLANApp().run()