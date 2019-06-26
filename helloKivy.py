import kivy


kivy.require('1.11.1')


from kivy.app import App


from kivy.uix.button import Label

class HelloKivy(App):
    def build(self):
        return Label(text = "Hello there Kivy")







def main():

    hellokivy = HelloKivy()
    hellokivy.run()





if __name__ =="__main__":
    main()
