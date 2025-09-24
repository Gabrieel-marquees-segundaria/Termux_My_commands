from flask import Flask, request, send_from_directory, jsonify
import os
from modules.zip_manager import ZipManager
import subprocess

app = Flask(__name__)
zip = ZipManager(None)
# Caminho base onde estão os arquivos JS
BASE_JS_PATH = os.path.join(app.root_path, "static", "js")


@app.route("/")
def home():
    return """
    <h1>Servidor Flask para modelos JS</h1>
    <p>Use a rota <code>/model/&lt;versao&gt;</code> para carregar o arquivo JS.</p>
    <p>Exemplo: <a href="/model/149">/model/149</a></p>
    """


@app.route("/model/<versao>")
def get_model(versao: str):
    """
    Rota que serve o arquivo JS de acordo com a versão passada na URL.
    Exemplo: /model/149  -> static/js/v149/three.module.js
    """
    zipfile  = os.environ.copy()["threejsZipFile"]
    folder = f"v{versao}"  # exemplo: "v149"
    file_name = "three.module.js"
    print(zipfile)
    # Caminho absoluto da pasta onde o arquivo deveria estar
    dir_path = os.path.join(BASE_JS_PATH, folder)
    zip.extract_path(zipfile,f"r{versao}", dir_path)
    if not os.path.exists(os.path.join(dir_path, file_name)):
        return jsonify({"erro": f"Versão {versao} não encontrada"}), 404

    return send_from_directory(dir_path, file_name)
if __name__ == "__main__":
    # Executa o servidor Flask
    app.run(host="0.0.0.0", port=5000, debug=True)
    zip.remove_temp_dir()
