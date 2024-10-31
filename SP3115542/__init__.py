from flask import Flask, render_template , session, redirect, url_for, request, flash, make_response

app = Flask(__name__)
app.secret_key= 'senha'

usuarios = {
    'paciente': 'senha',
}

exames = {
    'exame1': {'nome': 'Exame de Sangue', 'preco': 50},
    'exame2': {'nome': 'Exame de Urina', 'preco': 30},
    'exame3': {'nome': 'Exame de Fezes', 'preco': 20}
}

@app.route('/')
def chamahtml():
    return render_template('index.html', exames=exames)

@app.route('/loginmedico', methods=['GET', 'POST'])
def loginMedico():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in usuarios and usuarios[username] == password:
            session['username'] = username
            flash('Login realizado com sucesso!', 'success')
            return render_template('acessomedico.html')
        else:
            flash('Usuário ou senha incorretos!', 'danger')

    return render_template('loginmedico.html')

@app.route('/loginpaciente', methods=['GET', 'POST'])
def loginpaciente():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in usuarios and usuarios[username] == password:
            session['username'] = username
            flash('Login realizado com sucesso!', 'success')
            return render_template('acessopaciente.html')
        else:
            flash('Usuário ou senha incorretos!', 'danger')

    return render_template('loginpaciente.html')

@app.route('/carrinho', methods=['GET'])
def carrinho():
    carrinho = request.cookies.get('carrinho')
    if carrinho:
        itens = carrinho.split(',')
    else:
        itens = []
    
    detalhes_exames = {exame_id: exames[exame_id] for exame_id in itens if exame_id in exames}
    
    return render_template('carrinho.html', itens=detalhes_exames, exames=exames)

@app.route('/adicionar_ao_carrinho/<exame_id>', methods=['POST'])
def adicionar_ao_carrinho(exame_id):
    carrinho = request.cookies.get('carrinho', '')
    if carrinho:
        carrinho += f',{exame_id}'
    else:
        carrinho = exame_id

    response = make_response(redirect(url_for('carrinho')))
    response.set_cookie('carrinho', carrinho)
    flash('Exame adicionado ao carrinho!', 'success')
    return response

@app.route('/remover_do_carrinho/<exame_id>', methods=['POST'])
def remover_do_carrinho(exame_id):
    carrinho = request.cookies.get('carrinho', '')
    itens = carrinho.split(',')
    if exame_id in itens:
        itens.remove(exame_id)
    carrinho = ','.join(itens)

    response = make_response(redirect(url_for('carrinho')))
    response.set_cookie('carrinho', carrinho)
    flash('Exame removido do carrinho!', 'warning')
    return response

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(401)
def unauthorized_error(error):
    return render_template('401.html'), 401

@app.errorhandler(403)
def forbidden_error(error):
    return render_template('403.html'), 403

if __name__ == '__main__':
    app.run(debug=True)