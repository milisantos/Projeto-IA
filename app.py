app = Flask(__name__)


@app.route('/', methods=['GET'])
def form():
    return render_template_string('...')  # Substitua '...' pelo conteúdo do seu HTML acima


@app.route('/submit_form', methods=['POST'])
def submit_form():
    envolvidos = request.form.get('envolvidos')
    sexo = request.form.get('sexo')
    cinto_de_seguranca = request.form.get('cinto')
    embreagues = request.form.get('embreagues')
    idade = request.form.get('idade')
    categoria_habilitacao = request.form.get('categoria_habilitacao')
    especie_veiculo = request.form.get('especie_veiculo')
    pedestre = request.form.get('pedestre')
    passageiro = request.form.get('passageiro')


    # Processamento dos dados aqui...


    return "Dados recebidos!"


if __name__ == '__main__':
    app.run(debug=True)