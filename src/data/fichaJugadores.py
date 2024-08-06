async def fichaJugadores(channel, bot_wait_for, heroes,jugadores,heroesName):
    def checkClass(m): #Chequea la clase que elijan y manda una variable global con la clase elegida
                for x in heroesName:
                    contentMensaje = m.content
                    contentMensaje = contentMensaje.lower()
                    if contentMensaje == x and m.channel == channel:
                        global heroeElegido
                        heroeElegido = x
                        return True
    boolKey = True
    while boolKey:  # Recibe la clase elegida y lo guarda en la ficha del jugador
            await channel.send(f'Elegí tu clase: {heroesName} ')
            try:
                msg = await bot_wait_for('message', check=checkClass, timeout=10)
                if msg:
                    for heroe in heroes:
                        if heroeElegido == heroe[1].Nhero:
                            jugadores['heroe'] = heroe[1]
                            await channel.send(f'Elegiste {heroe[1].Nhero}')
            except:
                boolKey = False
