


def semana(dia):

    semana = {
        'segunda':"Dia de Semana",
        'terca':"Dia de Semana",
        'quarta':"Dia de Semana",
        'quinta':"Dia de Semana",
        'sexta':"Dia de Semana",
        'sabado':"Fim de Semana",
        'domingo':"Fim de Semana"
  }

    return semana.get(dia, '**valo invalido') 

if __name__ == "__main__":
    dia = "sasd"

    print( semana(dia) )