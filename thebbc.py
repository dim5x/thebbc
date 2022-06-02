# from flask import Flask, render_template
# import requests
# import os
# import yadisk
# from sys import platform
#
# app = Flask(__name__)
# app.template_folder = 'template'
#
#
# @app.route('/', methods=['GET'])
# def hello():
#     # try:
#     #     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
#     #                              'Chrome/41.0.2228.0 Safari/537.3'}
#     #     res1 = requests.get('https://github.com/', headers=headers)
#     #     res2 = requests.get('https://ria.ru/', headers=headers)
#     #     res3 = requests.get('https://google.com', headers=headers)
#     #
#     #     try:
#     y = yadisk.YaDisk(token='AQAAAAAHBpK9AAfzjZd-UO44LUPQqAIrb7HeYEI')
#     # y.upload("requirements.txt", "/test-dir/requirements.txt")
#     l = list(y.listdir("/test-dir"))
#     print(l)
#     for i in l:
#         print(f"Имя: {i['name']}, дата: {i['created'].strftime('%d.%m.%y')}, "
#               f"время: {i['created'].strftime('%H:%M:%S')}, размер: {i['size']}.")
#     return render_template('index.html', l=l)
#
#
# # except:
# #     return 'Ya error'
#
# # return f'''hello
# # Github = {str(res1.status_code)}
# # Ria = {str(res2.status_code)}
# # Google = {str(res3.status_code)}
# # Yandex = ok.
# # {platform}
# # '''
#
# # except:
# #     return 'Error'
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
"""
Example of serving a Flexx app using a regular web server. In this case flask.
See serve_with_aiohttp.py for a slightly more advanced example.
"""

# from flask import Flask

from flexx import flx, ui, event
from flexxamples.howtos.editor_cm import CodeEditor


# Define an app

class AppLayoutExample(flx.Widget):
    def init(self):
        with flx.VBox():
            flx.Label(style='background:#cfc;', wrap=1,
                      text='Here is some content at the top for which we want to '
                           'use minimal size. Thus the use of a VBox. '
                           'Below is a splitter, with a box layout on the left '
                           'and a fix layout on the right.')

            with flx.HSplit(flex=1):
                with flx.VBox(style='border:1px solid #777;'):
                    flx.Label(text='Flex 0 0 0')
                    with flx.HBox(flex=0):
                        self.b1 = flx.Button(text='Hi')
                        self.b2 = flx.Button(text='Helloooo world!')
                        self.b3 = flx.Button(text='Foo bar')

                    flx.Label(text='Flex 1 1 1')
                    with flx.HBox(flex=0):
                        self.b1 = flx.Button(flex=1, text='Hi')
                        self.b2 = flx.Button(flex=1, text='Helloooo world!')
                        self.b3 = flx.Button(flex=1, text='Foo bar')

                    flx.Label(text='Flex 1 0 3')
                    with flx.HBox(flex=0):
                        self.b1 = flx.Button(flex=1, text='Hi')
                        self.b2 = flx.Button(flex=0, text='Helloooo world!')
                        self.b3 = flx.Button(flex=3, text='Foo bar')

                    # flx.Widget(flex=1)  # spacer widget

                with flx.VFix(style='border:1px solid #777;'):
                    flx.Label(text='Flex 0 0 0 (space divided equally)', style='')
                    with flx.HFix():
                        self.b1 = flx.Button(text='Hi')
                        self.b2 = flx.Button(text='Helloooo world!')
                        self.b3 = flx.Button(text='Foo bar')

                    flx.Label(text='Flex 1 1 1', style='')
                    with flx.HFix():
                        self.b1 = flx.Button(flex=1, text='Hi')
                        self.b2 = flx.Button(flex=1, text='Helloooo world!')
                        self.b3 = flx.Button(flex=1, text='Foo bar')

                    flx.Label(text='Flex 1 0 3 (the widget with zero collapses')
                    with flx.HFix():
                        self.b1 = flx.Button(flex=1, text='Hi')
                        self.b2 = flx.Button(flex=0, text='Helloooo world!')
                        self.b3 = flx.Button(flex=3, text='Foo bar')

    # @event.reaction('line.user_text')
    # def when_user_changes_text(self, *events):
    #     self.l1.set_text('user_text: ' + self.line.text)
    #
    # @event.reaction('line.user_done')
    # def when_user_is_done_changing_text(self, *events):
    #     self.l2.set_text('user_done: ' + self.line.text)
    #
    # @event.reaction('line.submit')
    # def when_user_submits_text(self, *events):
    #     self.l3.set_text('submit: ' + self.line.text)


# Dump it to a dictionary of assets that we can serve. Make the main
# page index.html. The link=0 means to pack the whole app into a single
# html page (note that data (e.g. images) will still be separate).
# fl_app = flx.App(MyApp)
# assets = fl_app.dump('index1.html', link=0)
if __name__ == '__main__':
    m = flx.launch(AppLayoutExample)
    flx.run()