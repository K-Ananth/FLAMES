from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_string('''
<BoxLayout>
    canvas.before:
        Color:
            rgba: 0.6, 0, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size''')

class SimpleApp(App):
    def build(self):

        self.bx = BoxLayout(orientation="vertical",spacing="15")

        self.yn = TextInput(font_size=50, height=75,size_hint= (0.8, None),pos_hint={'center_x':0.5,'center_y':0.5}, multiline=False, foreground_color= (3, 0.4, 0.5, 1))
        self.cn = TextInput(font_size=50, height=75,size_hint= (0.8, None),pos_hint={'center_x':0.5,'center_y':0.5}, multiline=False, foreground_color= (3, 0.4, 0.5, 1))
        bt = Button(text="FLAMES", font_size=60,size_hint= (0.4, None),pos_hint={'center_x':0.5,'center_y':0.5}, background_color= (1, 5, 2, 1))
        bt.bind(on_press=self.on_press_bt)
        self.l = Label(text="", font_size=75)

        self.bx.add_widget(Label(text="your name", font_size=50))
        self.bx.add_widget(self.yn)
        self.bx.add_widget(Label(text="your crush name", font_size=50))
        self.bx.add_widget(self.cn)
        self.l = Label(text="", font_size=75, font_name="Ravie")

        self.bx.add_widget(bt)
        self.bx.add_widget(self.l)

        return self.bx

    def on_press_bt(self, istance):

        FLAMES = ['F', 'L', 'A', 'M', 'E', 'S']
        a = self.yn.text
        c = len(a)
        b = self.cn.text
        d = len(b)
        mylist_1 = []
        nlist_1 = []
        mylist_2 = []
        nlist_2 = []
        slist = []

        # Finding the special characters and numbers in first string

        for i in range(33, 65):
            for j in range(c):
                for k in range(d):
                    if (a[j] == chr(i)) or (b[k] == chr(i)):
                        self.l.text = "! Don't use special characters or numbers"

        # For storing elements of first string in list

        for i in range(65, 92):
            nlist_1.append(sum(mylist_1))
            mylist_1.clear()
            for j in range(c):
                if (chr(i) == a[j]) or (chr(i + 32) == a[j]):
                    mylist_1.append(1)
                else:
                    mylist_1.append(0)

        # For storing elements of second string in list

        for i in range(65, 92):
            nlist_2.append(sum(mylist_2))
            mylist_2.clear()
            for j in range(d):
                if (chr(i) == b[j]) or (chr(i + 32) == b[j]):
                    mylist_2.append(1)
                else:
                    mylist_2.append(0)

        # subracting two list

        for r in range(26):
            slist.append(nlist_1[r] - nlist_2[r])
            # Making negative values positive
            if slist[r] < 0:
                slist[r] = slist[r] * (-1)

        x = sum(slist)

        z = 0
        for e in range(1, 6):
            z = x % (7 - e)
            FLAMES.remove(FLAMES[z - 1])
            for s in range(0, z - 1):
                FLAMES.append(FLAMES[s])
            for t in range(0, z - 1):
                FLAMES.remove(FLAMES[0])

        if FLAMES[0] == 'F':
            self.l.text = "FRIENDS"
        if FLAMES[0] == 'L':
            self.l.text = "LOVE"
        if FLAMES[0] == 'A':
            self.l.text = "AFFECTION"
        if FLAMES[0] == 'M':
            self.l.text = "MARRIAGE"
        if FLAMES[0] == 'E':
            self.l.text = "ENEMY"
        if FLAMES[0] == 'S':
            self.l.text = "SISTER"

        print(self.l.text)

if __name__ == "__main__":
    SimpleApp().run()