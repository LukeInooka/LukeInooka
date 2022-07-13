import subprocess

def nmap(network_range: str)-> str:
    return subprocess.run(f'nmap -sn {network_range}', stdout=subprocess.PIPE).stdout.decode('utf-8')


def etter_cap(rip:str,tip:str):
    etter_out = subprocess.run(f'sudo ettercap -T -S -i enp0s3 /{rip}// /{tip}//', stdout=subprocess.PIPE).stdout.decode('utf-8')


def run_wire(password):
    a = subprocess.run('sudo wireshark', stdout=subprocess.PIPE).stdout.decode('utf-8')
    b = subprocess.run(str(password), stdout=subprocess.PIPE).stdout.decode('utf-8')


network_range = input('Enter Network Range')
nmap(network_range)
target = input('Enter Target IP')
router_ip = input('Enter Router IP')
ettercap(target,router_ip)
password = input('Enter password')
run_wire(password)
