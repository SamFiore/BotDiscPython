class Heroe(): #Plantilla de los jugadores
                def __init__(self,Nhero,vida,ataque,defensa,magia,mana):
                    self.Nhero = Nhero
                    self.vida = vida
                    self.ataque = ataque
                    self.defensa = defensa
                    self.magia = magia
                    self.mana = mana

class Enemigo: #Plantilla de enemigos
                def __init__(self,name,vida,damage,distancia):
                    self.name = name
                    self.vida = vida
                    self.damage = damage
                    self.distancia = distancia