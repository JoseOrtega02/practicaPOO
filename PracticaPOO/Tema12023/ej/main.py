from man_eval import ManejadorEvaluaciones
from man_fed import ManejadorFederados
if __name__=='__main__':
    federados=ManejadorFederados()
    federados.cargaf()
    Evaluaciones=ManejadorEvaluaciones()
    Evaluaciones.cargaev()
    print('---Menu---\n1.Patinadores de un estilo\n2.Patinador con mayor puntaje\n3.Patinadores por estilo\n4.Buscar patinador')
    i=int(input('Ingrese opcion:'))
    while i==1 or i==2 or i==3 or i==4:
        match i:
            case 1:
                e=input('Ingrese estilo:')
                edad=int(input('Ingrese edad:'))
                Evaluaciones.busc(e,edad,federados)
            case 2:
                Evaluaciones.may(federados)
            case 3:
                Evaluaciones.buscaest(federados)
            case 4:
                dni=int(input('Ingrese dni:'))
                es=input('Ingrese estilo:')
                Evaluaciones.puntaje(dni,es)
        print('---Menu---\n1.Patinadores de un estilo\n2.Patinador con mayor puntaje\n3.Patinadores por estilo\n4.Buscar patinador')
        i=int(input('Ingrese opcion:'))
