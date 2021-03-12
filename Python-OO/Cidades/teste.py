from cidades import Cidade
from estado import Estado

recife = Cidade("Recife", 100)
olinda = Cidade("Olinda", 200)

estadoPE = Estado("Pernambuco", "PE")

estadoPE.adicionaCidade(recife)
estadoPE.adicionaCidade(olinda)

estadoPE.populacaoEstado()