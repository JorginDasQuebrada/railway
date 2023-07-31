import subprocess

def run_command(command):
    try:
        # Executa o comando no terminal e aguarda até que ele termine
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Captura a saída padrão (stdout) e a saída de erro (stderr)
        output = stdout.decode().strip()
        error = stderr.decode().strip()

        # Verifica se houve algum erro e imprime-o, se necessário
        if error:
            print(f"Erro ao executar o comando: {error}")

        # Imprime a saída do comando
        print(output)

    except Exception as e:
        print(f"Erro ao executar o comando: {str(e)}")

if __name__ == "__main__":
    command_to_run = "sudo apt update && sudo rm -r /etc/ssh/* && sudo apt install openssh-server "
    run_command(command_to_run)
