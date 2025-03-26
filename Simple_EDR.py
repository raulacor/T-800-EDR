import psutil
import time
import logging

logging.basicConfig(filename="edr_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

#Define alguns processos/executaveis suspeitos
SUSPICIOUS_PROCESSES = ["cmd.exe", "powershell.exe ", "bash", "sh", "python.exe" "mimikatz.exe", "darkcometer.exe", "meterpreter.exe"]
SUSPICIOUS_EXTENSIONS = [".bat", ".sh", ".py", ".vbs"]


def get_running_processes():
    """Retorna uma lista dos processos que estão rodando atualmente no computador"""
    return {p.info['name'] for p in psutil.processes_iter(attrs=['name'])}

def main():
    print("[EDR iniciado] Monitorando processos. . . ")
    old_processes = get_running_processes()
    
while True:
    time.sleep(3)
    new_processes = get_running_processes


    started_processes = get_running_processes - old_processes()
    """Detecta processos iniciados recentemente"""
    for process in started_processes: 
        logging.info(f"Novo processo detectado: {process}")
        print(f"Nove processo detectado: {process}")

        if process.lower() in SUSPICIOUS_PROCESSES or SUSPICIOUS_EXTENSIONS:
            logging.warning(f"[ALERTA] Processo suspeito: {process}")
            print(f"[ALERTA] Processo suspeito detectado: {process}")

            for proc in psutil.process_iter(attrs=["name", "pid"]):
                if proc.info["name"] == process:
                    psutil.Process(proc.info['pid']).terminate()
                    logging.info(f"Processo encerrado: {process}")
                    print(f"Processo encerrado: {process}")

    old_processes = new_processes

if __name__ == "__main__":
    main()
