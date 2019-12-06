class VirtualMachine:
    def __init__(self, name, ram=1, cpu=1.3, hdd=100, os='debian'):
        self.name = name
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd
        self.os = os
        self.status = 0
        self.proc = list()

    def stop(self):
        self.status = 0
        self.proc = list()

    def start(self):
        self.status = 1

    def suspend(self):
        self.status = 2

    def reboot(self):
        self.stop()
        self.start()

    def run(self, pid, ram, cpu, hdd):
        print('Ejecutando proceso con PID:', pid)
        self.proc.append({'pid' : pid, 'ram' : ram, 'cpu' : cpu, 'hdd' : hdd})

    def ram_usage(self):
        ram_pr = 0
        for process in self.proc:
            ram_pr += process['ram']
        ram_usage = ram_pr * 100 / self.ram
        return ram_usage

    def cpu_usage(self):
        cpu_pr = 0
        for process in self.proc:
            cpu_pr += process['cpu']
        cpu_usage = cpu_pr * 100 / self.cpu
        return cpu_usage

    def hdd_usage(self):
        hdd_pr = 0
        for process in self.proc:
            hdd_pr += process['hdd']
        hdd_usage = hdd_pr * 100 / self.hdd
        return hdd_usage

    def __str__(self):
        if self.status == 0:
                 self.status = 'Stopped'
        elif self.status == 1:
                 self.status = 'Running'
        elif self.status == 2:
                 self.status = 'Suspended'
        return f'''
        {self.os} <{self.name}> [{self.status}]
        {self.ram_usage()}% RAM used | {self.cpu_usage()}% CPU used | {self.hdd_usage()}% HDD used
        '''


if __name__ == '__main__':
    machine1 = VirtualMachine('Minas Tirith', 8, 2.3, 380, 'ubuntu')
    machine2 = VirtualMachine('Rohan', 6, 1.9, 250, 'debian')
    machine3 = VirtualMachine('Rivendel', 16, 3, 1000, 'opensuse')
    print(machine1)
    machine1.start()
    print(machine1)
    machine1.run(1, 1.7, 0.3, 20)
    machine1.run(4, 4, 0.9, 100)
    machine1.run(7, 0.4, 1.1, 250)
    print(machine1)
    print(machine2)
    machine2.start()
    print(machine2)
    machine2.run(2, 0.6, 0.7, 50)
    machine2.run(5, 2.1, 0.2, 75)
    machine2.run(8, 2.5, 0.4, 30)
    print(machine2)
    machine2.reboot()
    print(machine2)
    print(machine3)
    machine3.start()
    print(machine3)
    machine3.run(3, 2, 1, 25)
    machine3.run(6, 0.3, 0.5, 12)
    machine3.run(9, 1.4, 0.8, 65)
    print(machine3)
    machine3.reboot()
    print(machine3)
