import os
import sys
import subprocess

lista = []
string = "selecione uma opcao:\n"

if __name__ == "__main__":

    args = sys.argv
    cont = 0
    if len(args) > 1:
        # faz algo com args[1]
        for dir in os.listdir():
            if os.path.isdir(dir):
            
               if args[1]:
                  # print(dir)
                  lista.append(dir)
               
                  string += f"{cont}: {dir}\n"
                  cont += 1


          selected =int( input(string))
          #os.chdir(lista[selected])
          #print(f"{os.getcwd()}")
          #subprocess.run(f"cd \{lista[selected]}", shell=True)
          print(lista[selected])
