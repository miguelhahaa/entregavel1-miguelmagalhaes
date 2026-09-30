# Imports
import sys
import rich.progress as rp

# Functions
def enough_battery(battery: float, mission_duration: float, consumption_per_minute: float):
    if not 0<=battery<=100 or mission_duration<=0 or consumption_per_minute<=0:
        print("Valor Inserido Inválido")
        sys.exit()
    else:
        return battery-mission_duration*consumption_per_minute>=0

def get_args():
    Settings = {"-b" : None, "-d": None, "-c": None}
    i=1
    while i <= len(sys.argv)-1:
        if sys.argv[i] in Settings.keys():
            try:
                if Settings[sys.argv[i]] != None:
                    print(f'Argumento Duplicado "{sys.argv[i]}"')
                    return None
                else:
                    Settings[sys.argv[i]]=float(sys.argv[i+1])
                    i+=2
            except Exception:
                print(f'Sequência Inválida a partir de: "{sys.argv[i]}"')
                return None
        else:
            print(f'Argumento Desconhecido: "{sys.argv[i]}"')
            return None
    return list(Settings.values())


# Main
if None != (args := get_args()):
    if enough_battery(*args) == True:
        leftover=args[0]-args[1]*args[2]
        with rp.Progress(rp.TextColumn("[progress.description]{task.description}"), rp.BarColumn(complete_style='bar.finished'), rp.TaskProgressColumn()) as p:
            t = p.add_task("[ Missão Possível ] -- Bateria Restante:",total=100)
            p.update(t,advance=leftover)
    else:
        missing_battery=abs(args[0]-args[1]*args[2])
        with rp.Progress(rp.TextColumn("[progress.description]{task.description}"), rp.BarColumn(finished_style='bar.complete'), rp.TextColumn(f"\033[95m {missing_battery:.0f}%\033[00m")) as p:
            t = p.add_task("[ Missão Não é Possível ] -- Bateria Adicional Necessária: ",total=100)
            p.update(t,advance=missing_battery)
else:
    pass
