import kivy

kivy.require("1.11.1")


from kivy.app import App
from kivy.uix.widget import Widget


class CustomWidget(Widget):
    pass


class CustomWidgetApp(App):
    def build(self):
        return CustomWidget()





def main():

    customeWidget = CustomWidgetApp()
    customeWidget.run()




if __name__ == "__main__":
    main()