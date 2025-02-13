from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        # Create a TabbedPanel
        tabbed_panel = TabbedPanel(do_default_tab=False)

        # Create the first tab (Input Form)
        tab1 = TabbedPanelItem(text='Input Form')
        tab1_content = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Add a TextInput for entering a number
        self.number_input = TextInput(hint_text='Enter a number', multiline=False, input_type='number')

        # Add a TextInput for entering a name
        self.name_input = TextInput(hint_text='Enter your name', multiline=False)

        # Add a TextInput for entering an email
        self.email_input = TextInput(hint_text='Enter your email', multiline=False)

        # Add a Button to submit the form
        self.button = Button(text='Submit')
        self.button.bind(on_press=self.on_button_press)

        # Add a Label to display the result
        self.result_label = Label(text='Fill the form and press Submit')

        # Add widgets to the first tab
        tab1_content.add_widget(self.number_input)
        tab1_content.add_widget(self.name_input)
        tab1_content.add_widget(self.email_input)
        tab1_content.add_widget(self.button)
        tab1_content.add_widget(self.result_label)

        # Set the content of the first tab
        tab1.add_widget(tab1_content)

        # Create the second tab (Placeholder)
        tab2 = TabbedPanelItem(text='Tab 2')
        tab2_content = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Add a placeholder label to the second tab
        placeholder_label = Label(text='This is Tab 2')
        tab2_content.add_widget(placeholder_label)

        # Set the content of the second tab
        tab2.add_widget(tab2_content)

        # Add the tabs to the TabbedPanel
        tabbed_panel.add_widget(tab1)
        tabbed_panel.add_widget(tab2)

        return tabbed_panel

    def on_button_press(self, instance):
        # Get the text from the TextInput widgets
        number = self.number_input.text
        name = self.name_input.text
        email = self.email_input.text

        # Update the Label widget with the entered data
        self.result_label.text = f'Number: {number}\nName: {name}\nEmail: {email}'

if __name__ == '__main__':
    MyApp().run()