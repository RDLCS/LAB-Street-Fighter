from typing import Optional,Set,List,Tuple,NamedTuple,Dict,DefaultDict
from datetime import date,time,datetime,timedelta
import csv

partida = NamedTuple("Partida", [("pj1", str),("pj2", str),("puntuacion", int),("tiempo", float),("fecha_hora", datetime),
    ("golpes_pj1", List[str]),("golpes_pj2", List[str]),("movimiento_final", str),("combo_finish", bool),("ganador", str),])

def lee_partidas(ruta:str)->List[partida]:
    lista=list()
    with open(ruta,'rt',encoding='utf-8') as f:
        iter=csv.reader(f)
        next(iter)
        for pj1,pj2,puntuacion,tiempo,fecha_hora,golpes_pj1,golpes_pj2,movimiento_final,combo_finish,ganador in iter:
            puntuacion=int(puntuacion)
            tiempo=float(tiempo)
            fecha_hora=datetime.strptime(fecha_hora,'%Y-%m-%d %H:%M:%S')
            golpes_pj1=parseo_golpes(golpes_pj1)
            golpes_pj2=parseo_golpes(golpes_pj2)
            combo_finish=(combo_finish=='1')
            lista.append(partida(pj1,pj2,puntuacion,tiempo,fecha_hora,golpes_pj1,golpes_pj2,movimiento_final,combo_finish,ganador))
    return lista

def parseo_golpes(txt:str)->List[str]:
    limpio=txt.strip('[]')
    lista=limpio.split(', ')
    return lista

def victora_mas_rapida(partidas:List[partida])->Tuple[str,str,float]:
    nombre1=''
    nombre2=''
    tiempo=0
    for p in partidas:
        if tiempo==0:
            nombre1=p.pj1
            nombre2=p.pj2
            tiempo=p.tiempo
        elif p.tiempo<tiempo:
            nombre1=p.pj1
            nombre2=p.pj2
            tiempo=p.tiempo
    return (nombre1,nombre2,tiempo)

def top_ratio_medio_personajes(partidas:List[partida],n:int)->List[str]:
    dicc=DefaultDict(list)
    for p in partidas:
        dicc[p.ganador].append(p.puntuacion/p.tiempo)
    for c,v in dicc.items():
        dicc[c]=sum(v)/len(v)
    return sorted(dicc,key=dicc.get)[:n]

def enemigos_mas_debiles(partidas:List[partida],personaje:str)->Tuple[List[str],int]:
    dicc=DefaultDict(int)
    lista=list()
    for p in partidas:
        if p.ganador==personaje:
            if p.pj1!=personaje:
                dicc[p.pj1]+=1
            else:
                dicc[p.pj2]+=1
    maximo_victorias=max(dicc.items(),key=lambda e:e[1])[1]
    for c,v in dicc.items():
        if v==maximo_victorias:
            lista.append(c)
    return (lista,maximo_victorias)

def movimientos_comunes(partidas:List[partida],p1:str,p2:str)->Set[str]:
    c1=set()
    c2=set()
    for p in partidas:
        if p1==p.pj1:
            for m in p.golpes_pj1:
                c1.add(m)
        elif p1==p.pj2:
            for m in p.golpes_pj2:
                c1.add(m)
        elif p2==p.pj1:
            for m in p.golpes_pj1:
                c2.add(m)
        elif p2==p.pj2:
            for m in p.golpes_pj2:
                c2.add(m)
    return c1&c2

def dia_mas_combo_finish(partidas:List[partida])->str:
    dicc=DefaultDict(int)
    for p in partidas:
        if p.combo_finish==True:
            dia=parseo_dia_semana(p.fecha_hora.weekday())
            dicc[dia]+=1
    return max(dicc,key=dicc.get)

def parseo_dia_semana(num:int)->str:
    dias=['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
    return dias[num]