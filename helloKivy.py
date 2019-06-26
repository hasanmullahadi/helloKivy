import kivy


kivy.require('1.11.1')


from kivy.app import App


from kivy.uix.button import Label

class HelloKivyApp(App):
    def build(self):
        return Label()







def main():

    hellokivy = HelloKivyApp()
    hellokivy.run()





if __name__ =="__main__":
    main()
