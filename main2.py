from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Line, InstructionGroup
from kivy.clock import Clock
from random import randint


class MyWidget(Widget):

    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)

        # Create a Line instruction and add it to the canvas
        self.line = Line(points=[10, 20, 130, 140])
        self.canvas.add(self.line)

        # Schedule the draw method to run every 0.5 seconds
        Clock.schedule_interval(self.draw, 0.5)

    def draw(self, dt):
        # Update the Line points in the main thread
        self.line.points = [randint(0, 200) for _ in range(4)]


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
        tab2_content = MyWidget()

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