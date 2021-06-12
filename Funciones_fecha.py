# FUNCIONES EN PYTHON - PREDEFINIDAS
'''funciones de fecha'''
from datetime import datetime,timedelta,date
hoy,fdia = datetime.now(),date.today()
futuro = hoy + timedelta(days = 30)
dif,aa,mm,dd = futuro - hoy, hoy.year, hoy.month, hoy.day
fecha = date(aa,mm,dd+2)
print(hoy,fdia,futuro,dif,fecha) 