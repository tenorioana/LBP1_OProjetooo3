from flask import Flask, render_template , session, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key= 'senha'

usuarios = {
    'paciente1': 'senha',
    'SP3115542': 'senha'
}

@app.route('/')
def chamahtml():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(debug=True)
