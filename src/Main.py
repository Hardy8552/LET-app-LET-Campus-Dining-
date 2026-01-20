from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

# Set window size (mobile-like)
Window.size = (360, 640)

class LETApp(App):
    def build(self):
        self.title = "LET - Leeds Campus Dining"
        layout = BoxLayout(orientation='vertical')
        
        # Header
        header = Label(
            text="LET",
            font_size=48,
            color=(0.1, 0.4, 0.8, 1)  # Leeds blue
        )
        
        # Subtitle
        subtitle = Label(
            text="Leeds Eating Technology",
            font_size=20,
            color=(0.3, 0.3, 0.3, 1)
        )
        
        # Tagline
        tagline = Label(
            text="Skip the Queue. Save Your Time.",
            font_size=16,
            color=(1, 0.4, 0, 1)  # Food orange
        )
        
        layout.add_widget(header)
        layout.add_widget(subtitle)
        layout.add_widget(tagline)
        
        return layout

if __name__ == '__main__':
    LETApp().run()