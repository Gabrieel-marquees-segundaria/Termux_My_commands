import zipfile
import os
import shutil

path = os.path.dirname(__file__)
print(path)

class ZipManager:
    def comp(self, nome_pasta, nome_arquivo_zip):
        with zipfile.ZipFile(nome_arquivo_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(nome_pasta):
                for file in files:
                    # Cria o caminho completo para o arquivo
                    caminho_arquivo = os.path.join(root, file)
                    # Define o caminho do arquivo dentro do ZIP
                    arcname = os.path.relpath(caminho_arquivo, nome_pasta)
                    zipf.write(caminho_arquivo, arcname)
        print(f"A pasta '{nome_pasta}' foi compactada em '{nome_arquivo_zip}'")
    
    def extract_path(self, 
    file_name_zip,
     pathname,
     from_path="temp"
     ):
        with zipfile.ZipFile(file_name_zip, "r", zipfile.ZIP_DEFLATED)   as zipf:
            
            for f in zipf.filelist:
                if pathname in f.filename:
                    zipf.extract(f.filename,from_path)
                    
    def remove_temp_dir(self, temp="temp"):
        temp = os.path.join("/data/data/com.termux/files/home/bin/python", temp)
        if not os.path.exists(temp):
            print("Erro: temp dir is not found")
            return
        try:
            print(temp)
            shutil.rmtree(temp)
            print("sucess: temp Dir deleted")
        except OSError as e:
            print(f"Erro from rm temp Dir: ${e}")
            
    
    def create_temp_dir(self):
        pass
    

if __name__ == "__main__":
    zip = ZipManager()
    #zip.compactar_pasta_manual("build", "threejs.zip")
    zip.extract_path("threejs.zip", "r149")
    
