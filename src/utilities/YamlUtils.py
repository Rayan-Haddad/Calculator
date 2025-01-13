import yaml
from rich import print

def StrToBool(x: str):
    if x in ["False", "FALSE", "false"]:
        x = False
        return x
    elif x in ["True", "TRUE", "true"]:
        x = True
        return x
    else:
        return x

def editYaml(filename:str, head:str, key:str, value:any):
    with open(f"{filename}", "r") as file:
        data = yaml.safe_load(file)
    if head in ["", " ", None]:
        data[key] = StrToBool(value)
    else:
        data[head][key] = StrToBool(value)
    with open(f"{filename}", "w") as file:
        yaml.dump(data, file)
    if head in ["", " "]:
        print(f'Succefully change the {key} in {filename} to {value} !')
    else:
        print(f'Succefully change the {key} of {head} in {filename} to {StrToBool(value)} !')
    