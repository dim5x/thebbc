import os
from flask import Flask, render_template, request, redirect, flash
import yadisk

app = Flask(__name__)
app.template_folder = 'template'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # для работы session

TOKEN = os.environ['TOKEN_BBC']
y = yadisk.YaDisk(token=TOKEN)


def convert_bytes(size: int) -> str:
    for x in ['bytes', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f'{size:.2f} {x}'
        size /= 1024.0


@app.route('/', methods=['GET', 'POST'])
def hello():
    flag = True
    data = []

    if request.method == 'POST':
        match request.form.get('button'):
            case 'Отправить':
                print('Отправить')
                links = request.form['text']
                with open('request.txt', 'w') as f:
                    f.write(links)
                try:
                    y.upload('request.txt', '/BBC/request.txt')
                except yadisk.exceptions.PathExistsError as error:
                    print(error)
                    flash('Ресурс "/BBC/request.txt" уже существует. Обратитесь-ка к Дмитричу.')
                    flag = False
                    pass
                if flag:
                    flash('Заявка отправлена.')
                return redirect('/')

            # if request.form.get('button') == 'Удалить всё':
            case 'Удалить всё':
                print('Удалить всё.')
                try:
                    for filename in y.listdir('/BBC/download'):
                        y.remove(f'/BBC/download/{filename.name}')
                        print(f'Файл {filename.name} удалён')
                except Exception as error:
                    print(error)
                    pass
                flash(f'Все файлы удалены.')
                redirect('/')

            case _:  # request.form['button']:
                print('Удалить.')
                print(request.form['button'])
                filename = request.form['button']
                try:
                    ans = y.remove(f'/BBC/download/{filename}')
                except Exception as error:
                    print(error)
                    pass
                flash(f'Файл {filename} удалён.')
                redirect('/')

    try:
        print('Запрос списка файлов в Яндексе.')
        for i in y.listdir("/BBC/download"):
            d = {'link': i['file'],
                 'size': convert_bytes(int(i['size'])),
                 'name': i['name'],
                 'date': i['created'].strftime('%d.%m.%y - %H:%M:%S')}
            data.append(d)
    except Exception as error:
        print(error)
        flash(str(error))
        pass

    return render_template('bbc.html', data=data)


if __name__ == '__main__':
    app.run(debug=False)
