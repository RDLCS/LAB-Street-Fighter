from street_fighter import*

def test_lee_partidas(partidas:List[partida])->None:
    print(f"Total registros leídos: {len(partidas)}")
    print("Mostrando los tres primeros registros:")
    for p in partidas[:3]:
        print(f"\t\t{p}")

def test_victora_mas_rapida(partidas:List[partida])->None:
    tupla=victora_mas_rapida(partidas)
    print(f"La partida más rápida fue una entre {tupla[0]} y {tupla[1]} que duró {tupla[2]} segundos.")

def test_top_ratio_medio_personajes(partidas:List[partida],n:int)->None:
    lista=top_ratio_medio_personajes(partidas,n)
    print(f"El top {n} de ratios medios es: {lista}")

def test_enemigos_mas_debiles(partidas:List[partida],personaje:str)->None:
    tupla=enemigos_mas_debiles(partidas,personaje)
    print(f"Los enemigos más débiles de {personaje} son {tupla}")

def test_movimientos_comunes(partidas:List[partida],p1:str,p2:str)->None:
    conj=movimientos_comunes(partidas,p1,p2)
    print(f"Los movimientos repetidos entre {p1} y {p2} son: {conj}")

def test_dia_mas_combo_finish(partidas:List[partida])->None:
    res=dia_mas_combo_finish(partidas)
    print(f"El día que más Ultra Combo Finish ha habido es el {res}")

if __name__=='__main__':
    fight=lee_partidas('data/games.csv')
    #print("1. Test de lee_peliculas:")
    #test_lee_partidas(fight)
    #print("2. Test victora_mas_rapida")
    #test_victora_mas_rapida(fight)
    #print("3. Test de top_ratio_medio_personajes")
    #test_top_ratio_medio_personajes(fight,3)
    #print("4. Test de enemigo_mas_debil")
    #test_enemigos_mas_debiles(fight,'Ken')
    #print("5. Test de movimientos_comunes")
    #test_movimientos_comunes(fight,'Ryu','Ken')
    #print("6. Test de dia_mas_combo_finish")
    #test_dia_mas_combo_finish(fight)