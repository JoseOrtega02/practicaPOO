def dias(dia:str):
    diasDic = {
        "lunes":1,
        "martes":2,
        "miercoles":3,
        "jueves":4,
        "viernes": 5,
        "sabado":6,
        "domingo":7
    }
    diaSelec = diasDic[dia]
    return diaSelec-1