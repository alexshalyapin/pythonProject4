from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Line, Ellipse, Color, InstructionGroup
from kivy.clock import Clock
from math import sin, cos, radians


class PendulumWidget(Widget):

    def __init__(self, **kwargs):
        super(PendulumWidget, self).__init__(**kwargs)

        # Pendulum properties
        self.angle = 90  # Initial angle in degrees
        self.length = 200  # Length of the pendulum
        self.origin = (400, 500)  # Origin point of the pendulum
        self.bob_radius = 20  # Radius of the pendulum bob
        self.angular_velocity = 0  # Angular velocity of the pendulum
        self.gravity = 0.01  # Gravity effect

        # Schedule the update method to run every frame
        Clock.schedule_interval(self.update, 1 / 60.0)

    def update(self, dt):
        # Update the pendulum's angle based on angular velocity
        self.angle += self.angular_velocity
        self.angular_velocity -= self.gravity * sin(radians(self.angle))

        # Calculate the bob's position
        bob_x = self.origin[0] + self.length * sin(radians(self.angle))
        bob_y = self.origin[1] - self.length * cos(radians(self.angle))

        # Clear the canvas and redraw the pendulum
        self.canvas.clear()
        with self.canvas:
            # Draw the pendulum string
            Color(1, 1, 1)
            Line(points=[self.origin[0], self.origin[1], bob_x, bob_y], width=2)
            Line(points=[self.origin[0]+40, self.origin[1], bob_x, bob_y], width=2)

            # Draw the pendulum bob
            Color(0, 1, 0)
            Ellipse(pos=(bob_x - self.bob_radius, bob_y - self.bob_radius), size=(2 * self.bob_radius, 2 * self.bob_radius))


class MyApp(App):
    def build(self):
        # Create a TabbedPanel
        tabbed_panel = TabbedPanel(do_default_tab=False)

        # Create the first tab (Input Form)
        tab1 = TabbedPanelItem(text='Input Form')
        tab1_content = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Add a TextInput for entering a number
        self.number_input = TextInput(hint_text='Enter a number', multiline=False, input_type='number')

        # Add a TextInput for entering a second number
        self.number_input2 = TextInput(hint_text='Enter 2 number', multiline=False, input_type='number')

        # Add a TextInput for entering a third number
        self.number_input3 = TextInput(hint_text='Enter 3 number', multiline=False, input_type='number')

        # Add a Button to submit the form
        self.button = Button(text='Submit')
        self.button.bind(on_press=self.on_button_press)

        # Add a Label to display the result
        self.result_label = Label(text='Fill the form and press Submit')

        # Add widgets to the first tab
        tab1_content.add_widget(self.number_input)
        tab1_content.add_widget(self.number_input2)
        tab1_content.add_widget(self.number_input3)
        tab1_content.add_widget(self.button)
        tab1_content.add_widget(self.result_label)

        # Set the content of the first tab
        tab1.add_widget(tab1_content)

        # Create the second tab (Drawing Tab)
        tab2 = TabbedPanelItem(text='Drawing Tab')
        tab2_content = PendulumWidget()

        # Set the content of the second tab
        tab2.add_widget(tab2_content)

        # Add the tabs to the TabbedPanel
        tabbed_panel.add_widget(tab1)
        tabbed_panel.add_widget(tab2)

        return tabbed_panel

    def on_button_press(self, instance):
        try:
            # Get the text from the TextInput widgets
            number = float(self.number_input.text)
            number2 = float(self.number_input2.text)
            number3 = float(self.number_input3.text)

            # Calculate the sum of the three numbers
            total_sum = number + number2 + number3

            # Update the Label widget with the sum
            self.result_label.text = f'Sum: {total_sum}'

            # Clear the input fields
            self.number_input.text = ''
            self.number_input2.text = ''
            self.number_input3.text = ''
        except ValueError:
            # Handle the case where the input is not a valid number
            self.result_label.text = 'Please enter valid numbers'


MyApp().run()