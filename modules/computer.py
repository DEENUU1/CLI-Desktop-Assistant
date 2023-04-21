import psutil
from rich.table import Table 

def return_pc_info():
    ram = psutil.virtual_memory()
    system_disk = psutil.disk_usage('/')

    logical_processors = psutil.cpu_count()
    cores = psutil.cpu_count(logical=False)
    cpu_freq = psutil.cpu_freq().current / 1000.0
    
    ram_total = ram.total / (1024.0 ** 3)
    ram_used = ram.used / (1024.0 ** 3)
    ram_free = ram.free / (1024.0 ** 3)
    ram_percent = ram.percent

    disk_total = system_disk.total / (1024.0 ** 3)
    disk_used = system_disk.used / (1024.0 ** 3)
    disk_free = system_disk.free / (1024.0 ** 3)
    disk_percent = system_disk.percent

    table = Table("name", "value")
    table.add_row("CPU logical processors: ", f"{logical_processors} ")
    table.add_row("CPU cores: ", f"{cores}")
    table.add_row("CPU frequency: ", f"{cpu_freq} MHz")
    table.add_row("RAM total: ", f"{ram_total:.2f} GB")
    table.add_row("RAM used: ", f"{ram_used:.2f} GB")
    table.add_row("RAM free: ", f"{ram_free:.2f} GB")
    table.add_row("RAM percent: ", f"{ram_percent:.2f} %")
    table.add_row("Disk total: ", f"{disk_total:.2f} GB")
    table.add_row("Disk used: ", f"{disk_used:.2f} GB")
    table.add_row("Disk free: ", f"{disk_free:.2f} GB")
    table.add_row("Disk percent: ", f"{disk_percent:.2f} %")
    return table 