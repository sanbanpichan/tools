import tkinter as tk
from tkinter import ttk


class MyRadioButton(tk.Frame):
    ''' ボタンでラジオボタンを実現する。

        引数：
        master:配置先の親フレーム
        dict_text_value:ボタンに表示するテキストと設定される値の組：辞書

        最後に押されたボタンの値を保持する
    '''

    def __init__(self, master, **kw):
        ''' コンストラクタ
        '''
        super().__init__(master)

        # ボタンインスタンスとそのテキストを持つ
        # 構造{text:{button:value}}
        self.dict_button_text = {}

        if 'dict_text_value' in kw:
            self.dict_text_value = kw.pop('dict_text_value')
        else:
            self.dict_text_value = None

        if 'button_layout' in kw:
            self.button_layout = kw.pop('button_layout')
        else:
            self.button_layout = None

        # 押された状態のボタンのvalueを保持する
        if 'pressed_val' in kw:
            self.pressed_val = kw.pop('pressed_val')
        else:
            self.pressed_val = None

        # 押された状態のボタンのvalueを保持する
        if 'font' in kw:
            self.font = kw.pop('font')
        else:
            self.font = None

        self.create_wiget()

    def create_wiget(self):
        '''ウィジェットの描画

        '''
        for text, value in self.dict_text_value.items():
            button = tk.Button(self, text=text, relief=tk.GROOVE, font=self.font)
            dict_button_val = {button: value}
            self.dict_button_text[text] = dict_button_val
            button.bind('<Button-1><ButtonRelease-1>', self.onClick)
            button.bind('<Enter>', self.onEnter)
            button.bind('<Leave>', self.onLeave)
            button.pack(side=self.button_layout)

            if value == self.pressed_val:
                button.config(state='disable')
                button.configure(bg='#cce4f7')



    def onEnter(self, event):
        ''' マウスオーバーしたときに色を変化させる
            ただし、選択されているボタンは色を変化させない
        '''
        wiget_text = event.widget['text']
        for text, btn_value in self.dict_button_text.items():

            if text == wiget_text:  # マウスオーバーした
                for btn, val in btn_value.items():#実質一つの値のペアを取得
                        if val != self.pressed_val:
                            btn.configure(bg='#e5f1fb')


    def onLeave(self, event):
        ''' マウスカーソルが外に出たときのイベント
        '''
        wiget_text = event.widget['text']
        for text, btn_value in self.dict_button_text.items():

            if text == wiget_text:  #領域からでた
                for btn, val in btn_value.items():
                    if val != self.pressed_val: #既に押されているボタンでなければ、ボタンを通常色に戻す
                        btn.configure(bg='SystemButtonFace')


    def onClick(self, event):
        ''' クリックされたイベントを拾ってどのボタンが押されたかを判断する
        '''
        wiget_text = event.widget['text']
        for text, btn_value in self.dict_button_text.items():

            if text == wiget_text:  # クリックされた
                for btn, val in btn_value.items():#実質一つの値のペアを取得
                    if val != self.pressed_val:
                        btn.config(state='disable')
                        btn.configure(bg='#cce4f7')
                        self.pressed_val = val
            else:
                for btn, val in btn_value.items():#実質一つの値のペアを取得
                    btn.config(state='active')
                    btn.configure(bg='SystemButtonFace')


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('200x200')
    root.title('ボタンラジオ')

    radio_txt_value = {'ボタン１': 10, 'ボタン２': 20, 'ボタン３': 30}
    cnf = {'dict_text_value': radio_txt_value, 'button_layout': tk.LEFT, 'pressed_val':20}

    radio = MyRadioButton(root, **cnf)

    radio.pack()

    root.mainloop()
