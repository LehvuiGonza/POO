from ciclistas import Equipo, Velocista, Escalador, Contrarrelojista

equipo1 = Equipo("Sky", "Estados Unidos")

velocista1 = Velocista(123979, "Geraint Thomas", 320, 25)
escalador1 = Escalador(123980, "Egan Bernal", 25, 10)
contrarrelojista1 = Contrarrelojista(123981, "Jonathan Castroviejo", 120)

equipo1.añadir_ciclista(velocista1)
equipo1.añadir_ciclista(escalador1)
equipo1.añadir_ciclista(contrarrelojista1)

velocista1.set_tiempo_acumulado(365)
escalador1.set_tiempo_acumulado(385)
contrarrelojista1.set_tiempo_acumulado(370)

equipo1.calcular_total_tiempo()
equipo1.imprimir()
equipo1.listar_equipo()