import os
import sys
import subprocess

lista = []
string = "selecione uma opcao:\n"

if __name__ == "__main__":
    os.chdir("/storage/emulated/0/__Projetos__")
    args = sys.argv
    cont = 0
    if len(args) > 1:
        # faz algo com args[1]
        for dir in os.listdir():
            if os.path.isdir(dir):

               if args[1] in dir:
                  # print(dir)
                  lista.append(dir)

                  string += f"{cont}: {dir}\n"
                  cont += 1


        dirs = [d for d in os.listdir() if os.path.isdir(d) if args[1] in d ]

        with open("/dev/tty", "w") as tty:
            for i, d in enumerate(dirs):
                print(f"{i}: {d}", file=tty)
        idx =int( input())
        #os.chdir(lista[selected])
        #print(f"{os.getcwd()}")
        #subprocess.run(f"cd \{lista[selected]}", shell=True)
        #print(lista[selected])
        print(lista[idx])




