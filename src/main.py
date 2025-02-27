nao_ip = "192.168.178.214"  # Sostituiscilo con l'IP di NAO
nao_port = 9559

from functions.voice import parla


if __name__ == "__main__":
    parla("Ciao, sono NAO!", nao_ip, nao_port)