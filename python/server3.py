from flask import Flask, url_for, send_from_directory
import subprocess


app = Flask(__name__)
subprocess.run(
[
"python"
,"export_files.py"
, "extract"
, "/storage/emulated/0/__Projetos__/git_off/public/javascript/threejs-v/threejs.zip",
 "r149"
]
      )


@app.route('/static/<path:filename>')
def serve_static(filename):
    # Este endpoint serve os arquivos da pasta static
    # no diretório raiz do seu aplicativo.
    return send_from_directory(app.static_folder, filename)

@app.route('/exibir_imagem')
def exibir_imagem():
    # Gere o URL para uma imagem chamada 'minha_imagem.png' na pasta static
    # e retorne-o ou use-o em um template.
    imagem_url = url_for('static', filename='minha_imagem.png')
    return f'<img src="{imagem_url}" alt="Minha Imagem">'

if __name__ == '__main__':
    app.run(debug=True)
    subprocess.run([
	"python"
,"export_files.py"
, "rm"
	])
