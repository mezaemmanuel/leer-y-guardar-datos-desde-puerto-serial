import pandas as pd
import random 
datos = pd.read_csv("2023-03-05.csv")
v=pd.DataFrame(datos)

print("Antes")
print(v)
nv=v.assign(Temperatura=random.randint(1, 4))
print("NUEVOS DATITOS")
print(nv)
nv.to_csv('2023-03-05.csv')
