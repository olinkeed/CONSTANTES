import sys
import nodlehs

def executarArquivo(caminhoArquivo):
    if not caminhoArquivo.endswith('.nls'):
        print("A extensão do arquivo não é .nls")
        return
    
    try:
        with open(caminhoArquivo, 'r') as arquivo:
            texto = arquivo.read()
    except FileNotFoundError:
        print(f'Arquivo {caminhoArquivo} não encontrado')
        return
    
    for numero, linha in enumerate(texto.split('\n'), start=1):
        if linha.strip() == '' or linha.strip().startswith('#'):
            continue

        try:
            resultado, erro = nodlehs.run(caminhoArquivo, linha)
            if erro is not None:
                print(erro.printDoErro())
        except nodlehs.ErroExecucao as e:
            print(f"Erro na linha {numero}: {e}")
        except nodlehs.ErroSintaxeInvalida as e:
            print(f"Erro de sintaxe na linha {numero}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: python shell.py <nomeArquivo.nls>")
    else:
        executarArquivo(sys.argv[1])
