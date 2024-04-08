from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shoes/')
def shoes():
    _shoes = [
        {
            "name": "Абаркасы (avarcas)",
            "price": '15 $',
            "description": 'Сандалии - это летняя обувь закрытым носом и открытой пяткой.'
                           ' Традиционно изготавливается из натуральных материалов.' ,
        },
        {
            "name": "Аскетичные броги (austerity brogues)",
            "price": '25 $',
            "description": 'классические туфли с W-образными швами на мысах. Главной особенностью '
                           'является отсутствие декоративной перфорации. Модель пришла из мужского'
                           ' гардероба, как и большинство классических вариантов.',
        },
    ]
    return render_template('shoes.html', content=_shoes)


@app.route('/accessories/')
def accessories():
    _accessories = [
        {
            "name": "Ornamentals",
            "price": '25 $',
            "description": 'украшения',
        },
        {
            "name": "Jewelry",
            "price": '16 $',
            "description": 'бижутерия',
        },
        {
            "name": "Jew",
            "price": '12 $',
            "description": 'бижутерия',
        },
    ]
    return render_template('accessories.html', content=_accessories)


if __name__ == '__main__':
    app.run(debug=True)
    