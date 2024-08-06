async def first_games(message,bot, Hr, fj, En, random):
        game_on = True #Si pasa se activa el juego
        channel = message.channel
        await channel.send('empieza el juego')

        while game_on: #código del juego
            def check(m): #chequea quienes juegas
                return m.content == 'juego' and m.channel == channel
            jugadores = {}

            ciclo_while = True
            player_number = 0
            while ciclo_while:
                #recibe los jugadores
                player_number +=1
                await channel.send(f'Escribe "juego" para unirte a la partida (Quedan {5 if player_number==1 else 6-player_number} espacios)')
                msg = None
                try:
                    msg = await bot.wait_for('message',check=check,timeout=5.0)
                    if msg:
                        jugadores[player_number] = {'id':int(msg.author.id),'name':str(msg.author.name)}
                        await channel.send('Siguiente jugador')
                    else:
                        ciclo_while = False
                except:
                    ciclo_while = False
                
            msg = None

            heroes = [] # List, con las clases de heroes
            for hero in Hr.items():
                heroes.append(hero)
            heroesName = []

            for name in heroes:
                heroesName.append(name[1].Nhero) #Recibe los nombres de los jugadores

            

            cantHeroes = len(heroesName)
            
            await fj(channel=channel,bot_wait_for=bot.wait_for,heroes=heroes,jugadores=jugadores,heroesName=heroesName)
                    
            nombres_jugadores = []
            firstKey = list(jugadores)[0]
            print(f'Diccionario jugadores: {jugadores[firstKey]}')
            firstKey2 = list(jugadores[firstKey])[0]
            print(firstKey2)
            for i,o in jugadores[firstKey][firstKey2].items(): #Genera la lista de jugadores y la envia al chat
                print(f'Key: {i}')
                print(f'Value: {o}')
                users = await bot.fetch_user(o)
                nombres_jugadores.append(users.name)
            await channel.send(f'Los jugadores son: {nombres_jugadores}')

            mapa = {}

            for x in range(1,43): # Genera cada id del mapa (Cada punto o recuadro si viste el gráfico)
                mapa[x] = {}
            
            n = 'name'
            for site,o in mapa.items(): #A cada id le asigna su respectivo 'bioma'
                if site == 3 or site == 4 or site == 5 or site == 15 or site == 21 or site == 38 or site == 39 or site == 40:
                    mapa[site] = {n:'desierto'}
                elif site == 11 or site == 17 or site == 19 or site == 24 or site == 26 or site == 32:
                    mapa[site] = {n:'bosque'}
                elif site == 9 or site == 13 or site == 30 or site == 34:
                    mapa[site] = {n:'aldea'}
                elif site == 10 or site == 12 or site == 31 or site == 33:
                    mapa[site] = {n:'lago'}
                elif site == 1 or site == 7 or site == 36 or site == 42:
                    mapa[site] = {n:'spawn'}
                elif site == 18 or site == 25:
                    mapa[site] = {n:'final'}
                else:
                    mapa[site] = {n:'pradera'}

            for e,h in mapa.items():
                mapa[e].setdefault('id',e)

            listEnemy = []
            for enemy in En.items():
                listEnemy.append(enemy)

            def comprobarNumero(numero): #Dado un número random, comprueba zonas donde no puede aparecer el enemigo, en caso que el número sea alguna de estas zona, vuelve a generar otro
                if mapa[numero][n] == 'aldea':
                    numeroN = random.randrange(1,42)
                    return comprobarNumero(numeroN)
                elif mapa[numero][n] == 'spawn':
                    numeroN = random.randrange(1,42)
                    return comprobarNumero(numeroN)
                elif mapa[numero][n] == 'final':
                    numeroN = random.randrange(1,42)
                    return comprobarNumero(numeroN)
                elif mapa[numero][n] == 'lago':
                    numeroN = random.randrange(1,42)
                    return comprobarNumero(numeroN) 
                else:
                    return numero
 
            def generarEnemigos(enemigo): #Comprueba la zona para que no se generen en el mismo punto y genera el enemigo en la zona
                numeroAleatorio = random.randrange(1,43)
                numero = comprobarNumero(numeroAleatorio)
                if mapa[numero].get('enemigo') == None:
                    mapa[numero]['enemigo'] = enemigo
                else:
                    return generarEnemigos(enemigo)
            
            for e in range(1,6): #Se llama a la función generarEnemigos y se le asigna el enemigo
                generarEnemigos(listEnemy[0])

            spawns = [1,7,36,42]

            t = 1

            for a in jugadores.items(): # Spawnea al jugador en una zona determinada, entre 4 puntos aleatorios
                while t < 5:
                    spawnAleatorio = random.choice(spawns)
                    if mapa[spawnAleatorio].get('jugador') == None:
                        mapa[spawnAleatorio]['jugador'] =  a
                        t = 5
                    else:
                        if t != 0:
                            t = t - 1
                        else:
                            t = 1

            # Programar movimiento jugador

            teclado = ['w','a','s','d']

            def checkMov(m):
                for x in teclado:
                    if m.content == x and m.channel == channel:
                        global mov
                        mov = x
                        return True

            msg = None
            
            def encontrarPj(diPj):
                for qw,ew in mapa.items():
                    if ew['jugador'] != None:
                        hayPj = qw
                        if mapa[hayPj]['jugador'].id == diPj:
                            global pjEncontrado
                            pjEncontrado = hayPj


                    
                

            for jug,obj in jugadores.items():
                q = 1
                while q < 2:
                    msg = await bot.wait_for('message',check=checkMov,timeout=30)
                    encontrarPj(msg.author.id)
                    for po,pa in mapa.items:
                        if pjEncontrado == po:
                            pa.pop('jugador')
                            for i in teclado:
                                if i == x:
                                    if x == 'w':
                                        newPjNum = pjEncontrado
                                        newPjNum = newPjNum + 7
                                        


                        
                     


            # Programar encuentros con enemigos y una funcion para multiplicar el daño por el número aleatorio y para restarlo (Mismo con los enemigos)

            game_on = False