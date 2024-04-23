from cmu_graphics import *
from PIL import Image
import os, pathlib
import random
import math
from pictureFunction import *

def onAppStart(app):
    app.twentyBullets = False
    app.twentyBulletsOpacity = 30
    app.maxHealth = False
    app.maxHealthOpacity = 30
    reset(app)

def reset(app):
    app.intro = True
    app.playPage = False
    app.gameOver = False
    app.win = False
    
    # set the cursor initially out of page
    app.cursorX,app.cursorY = -30,-20
    app.stepsPerSecond = 5
    app.cursorCounter = 0
    app.angle = 0
    app.monsters = []
    # 5 fps, 40 * 2 sec
    app.generation = 5 * 35 * 2
    app.bullets = []
    # monster 1 2 3 generation corresponding robability
    app.p1 = 0.4
    app.p2 = 0.4
    app.p3 = 0.2
    app.limitPerRow = 0
    app.sniper = Sniper()
    app.bulletsLoc = []
    app.equip = True
    app.personX = 300
    app.orbsList = ['heal','fire','freeze']
    app.orbs = []
    app.orbLoc = []
    app.fire = False
    app.fireBuffOpacity = 50
    app.freeze = False
    app.freezeBuffOpacity = 50
    app.burnList = [1,2,3,4,5]
    app.orbsToBeAbsorbed = []
    app.stageOpacity1 = 100
    app.stageOpacity2 = 50
    app.bossStage = False
    app.boss= Boss(300,100)
    app.paused = False
    app.pressingQuestionMark = False
    app.bossSecs = 0
    app.aimCursorX = 0
    app.aimCursorY = 0
    app.bossOpacity = 100
    app.accuracy = 1
    app.totalHits = 0
    app.successfulHits = 0
    app.weightList = []
    app.tenSecs = 5 * 10
    app.timeElapsed = 0
    app.harder = None
    app.weightingList = []
    app.bossList = [app.boss]
    app.shieldOpacity = 30
    app.terrainList = []
    app.terrainKinds = ['stone','wood']
    app.terrainTime = 5 * 10
    app.score = 0
    app.track = False
    app.trackCD = 5 * (15+7)
    app.trackDuration = 7 * 5
    app.trackPressed = False
    app.trackOpacity = 30
    app.boomDuration = 3
    app.boomList = []


    # url is from https://pixabay.com/sound-effects/search/gun%20shooting/
    app.bulletshooting = loadSound("sounds/shootingbullet.mp3")
    # url is from https://www.myinstants.com/en/instant/monster-kill/?utm_source=copy&utm_medium=share
    app.monsterKilled = loadSound("sounds/monsterKilled.mp3")
    # url is from https://www.myinstants.com/en/instant/minecraft-explosion-84853/?utm_source=copy&utm_medium=share
    app.explosion = loadSound("sounds/explosion.mp3")
    # url is from https://www.myinstants.com/en/instant/sonic-gameover/?utm_source=copy&utm_medium=share
    app.gameoverSound = loadSound("sounds/gameoverSound.mp3")
    # url is from https://www.myinstants.com/en/instant/a-thousand-miles-63121/?utm_source=copy&utm_medium=share
    app.aThousandMile = loadSound("sounds/aThousandMile.mp3")
    # url is from https://www.myinstants.com/en/instant/fear-the-walking-dead-intro-56/?utm_source=copy&utm_medium=share
    app.playSound = loadSound("sounds/introSound.mp3")
    # url is from https://www.myinstants.com/en/instant/hamonhalil-yeah-73592/?utm_source=copy&utm_medium=share
    app.winSound1 = loadSound("sounds/winSound1.mp3")
    # url is from https://www.myinstants.com/en/instant/single-jojo-ora-3358/?utm_source=copy&utm_medium=share
    app.useShieldSound = loadSound("sounds/useShieldSound.mp3")
    # url is from https://www.myinstants.com/en/instant/absorb-18764/?utm_source=copy&utm_medium=share
    app.absorb = loadSound("sounds/absorb.mp3")
    # url is from https://www.myinstants.com/en/instant/harder-better-faster-stronger-/?utm_source=copy&utm_medium=share
    app.harderstrongerfaster = loadSound("sounds/harderstrongerfaster.mp3")

    introPicture(app)
    winPagePicture(app)
    playPagePicture(app)
    gameOverPagePicture(app)

def redrawAll(app):
    if app.intro:
        drawIntroPage(app)
        return
    if app.gameOver:
        drawGameOverPage(app)
        return
    elif app.win:
        drawWinPage(app)
        return
    else:
        if not app.pressingQuestionMark:
            drawPlayPage(app)
        else:
            drawHowtoPlay(app)
        
def onMouseMove(app, mouseX, mouseY):
    if app.intro:
        moveCursorIntro(app,mouseX,mouseY)
        if bottonPress(app.cursorX,app.cursorY,200,300,535,500):
            app.intro = False
            app.playPage = True
            if app.playPage:
                playPicture(app)
    else:
        if not app.gameOver and not app.win:
            app.angle = angle(app,mouseX,mouseY)
            app.aimCursorX = mouseX
            app.aimCursorY = mouseY
            
def angle(app,mouseX,mouseY):
    if mouseY != 600:
        return -math.atan((300-mouseX)/(600-mouseY) )*180/math.pi
    if mouseY > 600:
        return  math.atan((300-mouseX)/(600-mouseY) )*180/math.pi
    # if mouse is out of the page
    return 0

def moveCursorIntro(app,mouseX,mouseY):
    if app.cursorX!= mouseX and app.cursorY != mouseY:
        while app.cursorCounter != 0:
            if mouseX > app.cursorX:
                app.cursorX += 20
            elif mouseX < app.cursorX:
                app.cursorX -= 20
            if mouseY > app.cursorY:
                app.cursorY += 20
            elif mouseY < app.cursorY:
                app.cursorY -= 20
            app.cursorCounter -= 1

def onStep(app):
    app.cursorCounter += 1
    if app.playPage:
        app.playSound.play(loop=True)
        if not app.paused:
            if not app.win or app.sniper.health <=0 :
                app.timeElapsed += 1
                healthRegen(app)
                updateBullets(app)
                updateOrbs(app)
                monstersAttack(app)
                monstersMove(app)
                updateAccuracy(app)
                updateShield(app)
                updateTrackingBullets(app)
                updateGameOver(app)
                updateTerrain(app)
                weightTheGame(app)
                updateBoom(app)
                if app.sniper.health <= 0:
                    app.gameOver = True
                    app.playPage = False
                    app.gameoverSound.play()
                if not app.bossStage:
                    firstStage(app)
                if app.bossStage:
                    stageOpacityChange(app)
                    updateboss(app)
                    app.boss.move(app)
                if app.pressingQuestionMark:
                    app.paused = True 
                
    else:
        app.playSound.pause()       

def onKeyPress(app,key):
    if app.playPage:
        if key ==  'a':
            if app.personX > 80:
                app.equip = False
                app.personX -= 50
        if key == 'd':
            if app.personX < 570:
                app.personX += 50
                app.equip = False
        if key == 'f':
            if app.personX == 300:
                app.equip = True
        if app.pressingQuestionMark:
            if key !='tab':
                app.pressingQuestionMark = False
                app.paused = False
        if key == 'w':
            if app.sniper.shield:
                app.useShieldSound.play()
                app.sniper.pressedShield = True
        if key == 's':
            if app.track:
                app.trackPressed = True

def onMousePress(app, mouseX, mouseY):
    if app.pressingQuestionMark:
        app.pressingQuestionMark = False
        app.paused = False
    if app.playPage:
        if app.equip:
            if 50<mouseX<550:
                app.bulletshooting.play()
                app.totalHits += 1
                app.bullets.append(app.angle)
                app.bulletsLoc.append([300,600])
        # pressing question mark
        if ((mouseX-675)**2+(mouseY-97.5)**2)**0.5 <= 50:
            app.pressingQuestionMark = True
        # pressing shield
        elif ((mouseX-675)**2+(mouseY-275)**2)**0.5 <= 25:
            if app.sniper.shield:
                app.useShieldSound.play()
                app.sniper.pressedShield = True
        else:
            app.pressingQuestionMark = False
    if app.win or app.gameOver:
        if ((mouseX-372)**2+(mouseY-612)**2)**0.5 <= 25:
            reset(app)

def healthRegen(app):

    # regen 5 hp per 4 secs
    if app.generation != 0 and app.generation // 20 == app.generation / 20 and app.generation != 5 * 60 * 2:
        app.sniper.heal(app,3)
    else:
        if app.bossSecs// 20 == app.bossSecs / 20 and app.bossSecs != 0:
            app.sniper.heal(app,3)

def updateBullets(app):
    bulletsToRemove = set()
    for i in range(len(app.bullets)):
        if not app.trackPressed or app.monsters==[]:
            if app.bullets[i] > 0:
                app.bulletsLoc[i][0] += 35* math.sin(app.bullets[i]*math.pi/180)
                app.bulletsLoc[i][1] -= 35* math.cos(app.bullets[i]*math.pi/180)           
            else:
                app.bulletsLoc[i][0] -= 35* math.sin(-app.bullets[i]*math.pi/180)
                app.bulletsLoc[i][1] -= 35* math.cos(-app.bullets[i]*math.pi/180)
        if app.trackPressed:
            # find min monster or boss
            minD = 999
            m = None
            if app.monsters!=[]:
                for monster in app.monsters:
                    if distance(monster.x,monster.y,app.bulletsLoc[i][0],app.bulletsLoc[i][1]) <= minD:
                        minD = distance(monster.x,monster.y,app.bulletsLoc[i][0],app.bulletsLoc[i][1])
                        m = monster
            # change app.bullets[i]
            if m!= None and app.monsters!=[] and m.y != 0:
                app.bullets[i] = -math.atan((300-m.x)/(600-m.y) )*180/math.pi
                if app.bullets[i] > 0:
                    app.bulletsLoc[i][0] += 35* math.sin(app.bullets[i]*math.pi/180)
                    app.bulletsLoc[i][1] -= 35* math.cos(app.bullets[i]*math.pi/180)
                else:
                    app.bulletsLoc[i][0] -= 35* math.sin(-app.bullets[i]*math.pi/180)
                    app.bulletsLoc[i][1] -= 35* math.cos(-app.bullets[i]*math.pi/180)
    
        for monster in app.monsters:
            if app.bulletsLoc[i][0] - 30 < monster.x < app.bulletsLoc[i][0] + 30:
                if app.bulletsLoc[i][1] - 30 < monster.y < app.bulletsLoc[i][1] + 30:
                    app.sniper.attack(monster)
                    app.successfulHits += 1
                    # burn effect here
                    if app.fire:
                        monster.health -= app.burnList[i%5]
                    bulletsToRemove.add(i)

            if monster.health <= 0:
                # check if the orb is dropped
                selected = random.random()
                if selected <= monster. pOrb:
                    selected = True
                else:
                    selected = False
                if selected:
                    # drop orb
                    orb = random.choices(app.orbsList,[1/3,1/3,1/3])[0]
                    app.orbs.append(orb)
                    app.orbLoc.append(monster.x)
                app.monsters.pop(app.monsters.index(monster))
                app.boomList.append((monster,3))
                app.explosion.play()
                

        if app.terrainList != []:
            for j in range(len(app.terrainList)):
                terrain = app.terrainList[j]
                if terrain.kind == 'wood':
                    if app.bulletsLoc[i][0] - 15 < terrain.x < app.bulletsLoc[i][0] + 15:
                        if app.bulletsLoc[i][1] - 15 < terrain.y < app.bulletsLoc[i][1] + 15: 
                            app.sniper.attack(terrain)  
                            bulletsToRemove.add(i)
                elif terrain.kind == 'stone':
                    if app.bulletsLoc[i][0] - 25 < terrain.x < app.bulletsLoc[i][0] + 25:
                        if app.bulletsLoc[i][1] - 25 < terrain.y < app.bulletsLoc[i][1] + 25: 
                            app.sniper.attack(terrain)
                            bulletsToRemove.add(i)
        
        if app.bossStage:
            if app.boss.health <= 0:
                app.bossList = []
            else:
                if app.bulletsLoc[i][0] - 45 < app.boss.x < app.bulletsLoc[i][0] + 45:
                    if app.bulletsLoc[i][1] - 45 < app.boss.y < app.bulletsLoc[i][1] + 45:
                        if not app.boss.invisibility:
                            app.sniper.attack(app.boss)
                            # burn effect here
                            if app.fire:
                                app.boss.health -= app.burnList[i%5]
                        bulletsToRemove.add(i)
            if app.monsters == [] and app.boss.health <=0:
                app.win = True
                app.playPage = False
                app.winSound1.play()
                # eliminate all monsters
                app.bossStage = False
                app.monsters = []
                app.bossList = []
            
    # save some space (memory)
    for i in range(len(app.bulletsLoc)):
        if app.bulletsLoc[i][1] < 0:
            bulletsToRemove.add(i)

    if bulletsToRemove != set() and app.bullets != set():
        # this step is to avoid index error when popping
        bulletsToRemove = sorted(bulletsToRemove,reverse = True)
        for e in bulletsToRemove:
            app.bullets.pop(e)
            app.bulletsLoc.pop(e)

# this is to check if the person is absorbing the orb or not 
def updateOrbs(app):
    for x in app.orbLoc:
        if abs(app.personX - x) <= 25:
            orb = app.orbs[app.orbLoc.index(x)]
            app.orbsToBeAbsorbed.append(orb)
            app.orbs.remove(orb)
            app.orbLoc.remove(x)
    if app.orbsToBeAbsorbed != []:
        for orb in app.orbsToBeAbsorbed:
            app.absorb.play()
            app.sniper.useOrb(app,orb)
    app.orbsToBeAbsorbed = []
    # update the person's fire and freeze buffs
    if app.fire:
        # originally 10, now the attack attribute is 15
        # the burn effect is in the bullets section
        app.sniper.attackAttribute = 15
        app.sniper.fireDuration -= 1
        if app.sniper.fireDuration == 0:
            app.fire = False
            app.sniper.attackAttribute = 10
            app.sniper.fireDuration = 5 * 30
    # if fire then fire orb is being "light up"
        app.fireBuffOpacity = 100
    else:
        app.fireBuffOpacity = 30        
    
    if app.freeze:
        # freeze effect would be the monstersmove section
        app.sniper.freezeDuration -= 1
        if app.sniper.freezeDuration == 0:
            app.freeze = False
            app.sniper.freezeDuration = 5 * 30
    # if freeze then freeze orb is being "light up"
        app.freezeBuffOpacity = 100
    else:
        app.freezeBuffOpacity = 30

def stageOpacityChange(app):
    app.stageOpacity1 = 50
    app.stageOpacity2 = 100

def updateboss(app):
    app.boss.rgb = convertTorgb(app.boss)
    app.bossSecs += 1
    # boss stage change
    if app.boss.health < 500 and app.boss.stage1 == True:
        app.bossOpacity = 50
        app.boss.heal()
        app.boss.stage1 = False
        app.boss.invisible()
    if app.boss.secs >0 and app.boss.invisibility:
        app.boss.secs -= 1
    else:
        app.boss.invisibility = False
        app.bossOpacity = 100
    # attack per 3 secs 
    if app.bossSecs / 15 == app.bossSecs // 15:
        app.boss.attack(app)
    if app.boss.stage1 == False:
        app.boss.summon(app)
    if app.boss.y >= 550 and app.bossList!=[]:
        app.gameOver = True
        app.playPage = False
    # destory all terrains it passing by
    for terrain in app.terrainList:
        if terrain.kind == 'wood':
            r = 15
        else:
            r = 25
        if terrain.x - r - 50  <= app.boss.x <= terrain.x + r + 50 :
            if terrain.y - r - 60 <= app.boss.y <= terrain.y + r + 60:
                app.terrainList.pop(app.terrainList.index(terrain))


def updateAccuracy(app):
    if app.totalHits != 0:
        app.accuracy = app.successfulHits / app.totalHits
        if app.totalHits >= 20 and app.accuracy == 1:
            app.twentyBullets = True
            app.twentyBulletsOpacity = 100
        

# shield for 2 secs, absorb 75 percent of the damage, CD is 10 secs
def updateShield(app):
    if not app.sniper.shield:
        app.sniper.shieldCD -= 1 
    if app.sniper.shieldCD == 0:
        app.sniper.shield = True
    if app.sniper.shield and app.sniper.pressedShield:
        app.sniper.shieldDuration -= 1
        app.shieldOpacity = 100
    else:
        app.shieldOpacity = 30
    if app.sniper.shieldDuration == 0:
        app.sniper.shieldDuration = 5 * 2
        app.sniper.shield = False
        app.sniper.pressedShield = False
        app.sniper.shieldCD = 5 * 10

def updateTrackingBullets(app):
    if app.trackCD > 0:
        app.trackCD -= 1
    if app.trackCD == 0:
        app.track = True
        app.trackCD = 5 * (15+7)
        app.trackDuration = 7 * 5
    if app.trackPressed:
        app.trackDuration -= 1
        app.trackOpacity = 100
    else:
        app.trackOpacity = 30
    if app.trackDuration == 0:
        app.trackDuration = 7 * 5
        app.track = False
        app.trackPressed = False
    
        

def updateGameOver(app):
    if app.gameOver:
        app.monsters = []
        app.bossList = []
        
def updateTerrain(app):
    app.terrainTime -= 1
    if app.terrainTime == 0:
        app.terrainTime = 5 * 10
        generateTerrainLoc(app)
    for terrain in app.terrainList:
        if terrain.health <= 0:
            app.terrainList.pop(app.terrainList.index(terrain))
        
def drawBoom(app):
    for monster,remainingFrames in app.boomList:
        if remainingFrames >= 0 :
            drawImage(app.boom,monster.x,monster.y,width = 10+1/(remainingFrames+1)*20,height = 10+1/(remainingFrames+1)*20,align = 'center')

def updateBoom(app):
    for i in range(len(app.boomList)):            
        app.boomList[i] = (app.boomList[i][0],app.boomList[i][1]-1)


def generateTerrainLoc(app):
    x = random.randrange(70,530)
    y = random.randrange(300,500)
    passed = False
    if app.terrainList != []:
        for terrain in app.terrainList:
            if terrain.x - 20 < x < terrain.x + 20:
                if terrain.y - 20 < y < terrain.y + 20:
                    passed = True
    if app.monsters != [] and passed:
        for monster in app.monsters:
            if monster.x - 20 < x < monster.x + 20:
                if monster.y - 20 < y < monster.y + 20:
                    app.terrainList.append(Terrain(app,x,y))
                    return
    else:
        app.terrainList.append(Terrain(app,x,y))
        return
    return generateTerrainLoc(app)

        

# adaptive AI weight the game! higher the number it returns, harder the game it should achieve
def weightTheGame(app):
    app.tenSecs -= 1
    if app.tenSecs == 0:
        app.weightingList.append(app.score)
        if average(app.weightingList) > app.score:
            app.harder = False
        else:
            if app.score > 0.71:
                if not app.harder:
                    app.harderstrongerfaster.play()
                app.harder = True
        # 5fps for 10 secs
        app.tenSecs = 5 * 10
    # weitingFactor1 considers accuracy
    wf1 = 0.2
    # weitingFactor2 considers time elapsed
    wf2 = 0.1
    # weitingFactor3 considers the remaining health character has
    wf3 = 0.5
    # weitingFactor4 (lame factor) considers the amount of monsters in the battlefield
    wf4 = 0.2
    # weight it!
    score1 = wf1 * app.accuracy 
    if app.timeElapsed >= 5 * 60:
        score2 = wf2 * 1
    else:
        score2 = wf2 * app.timeElapsed / (60 * 5) 
    score3 = wf3 * app.sniper.health / 400
    if len(app.monsters) >=3:
        score4 = 0
    else:
        score4 = wf4 * 1
    app.score = score1 + score2 + score3 + score4

def monstersAttack(app):
    if app.generation != 0:
        # per five secs
        if app.generation // 25 == app.generation / 25 and app.generation != 5 * 60 * 2:
            for monster in app.monsters:
                if type(monster) == Monster2:
                    monster.attack(app)
                    if app.sniper.pressedShield:
                        app.sniper.heal(app,monster.attackAttri * 0.75)
        # per six secs
        if app.generation // 30 == app.generation / 30 and app.generation != 5 * 60 * 2:
            for monster in app.monsters:
                if type(monster) == Monster3:
                    monster.attack(app)
                    if app.sniper.pressedShield:
                        app.sniper.heal(app,monster.attackAttri * 0.75)
    else:
        if app.bossSecs // 25 == app.bossSecs / 25 and app.bossSecs != 5 * 60 * 2:
            for monster in app.monsters:
                if type(monster) == Monster2:
                    monster.attack(app)
                    if app.sniper.pressedShield:
                        app.sniper.heal(app,monster.attackAttri * 0.75)
        # per six secs
        if app.bossSecs // 30 == app.bossSecs / 30 and app.bossSecs != 5 * 60 * 2:
            for monster in app.monsters:
                if type(monster) == Monster3:
                    monster.attack(app)
                    if app.sniper.pressedShield:
                        app.sniper.heal(app,monster.attackAttri * 0.75)
                    
    
        
# use recursion to generate monster if a monster that is generated is not valid
def generateMonster(app):
    if app.bossStage:
        x,y = 50+30+randrange(500)+1,130
        Monsters = [Monster1(x,y),Monster2(x,y),Monster3(x,y)]
        randomMonster = random.choices(Monsters,[app.p1,app.p2,app.p3])[0]
        if not monsterValid(app,randomMonster):
            return generateMonster(app)
        app.monsters.append(randomMonster)
    else:
        if app.limitPerRow > 10:
            return
        x,y = 50+30+randrange(500)+1,130
        Monsters = [Monster1(x,y),Monster2(x,y),Monster3(x,y)]
        randomMonster = random.choices(Monsters,[app.p1,app.p2,app.p3])[0]
        if not monsterValid(app,randomMonster):
            return generateMonster(app)
        app.monsters.append(randomMonster)

def monsterValid(app,monster):
    app.limitPerRow += 1
    for m in app.monsters:
        if m.x-30*2 <=monster.x <= m.x+30*2:
            if m.y-30*2<=monster.y<=m.y+30*2:
                return False
    return True

# monster would not overlap with the terrain
def monstersMove(app):
    for monster in app.monsters:
        raycasted = False
        shortestDist = 1000
        monster.rgb = convertTorgb(monster)
        
        if monster.y <= 625:
            monster.move(app)
            # harder the game,faster they move
            if app.harder==True:
                monster.y += 1
                monster.attackAttri += 1
            # if the game is too hard
            if app.harder==False:
                monster.y -= 1
                monster.attackAttri -= 0.5
            # freeze effect here
            if app.freeze:
                monster.y -= 2
            # avoid terrain here
            shortestTerrain = None
            for terrain in app.terrainList:
                if terrain.kind == 'wood':
                    r = 15
                else:
                    r = 25
                x,y = terrain.x, terrain.y
                if x - r - 20 <= monster.x <= x +r + 20:
                    if y - r - 20 <= monster.y <= y + r + 20:
                        if not raycasted:
                            raycasted = True
                        if raycasted and shortestDist > distance(x,y,monster.x,monster.y):
                            shortestDist = distance(x,y,monster.x,monster.y)
                            shortestTerrain = terrain
            if raycasted:
                # if the terrain is in the left and in the range of "ray"
                if shortestTerrain.x <= monster.x:
                    monster.x += random.randint(20,25)
                # the terrain is in the right of the monster
                else:
                    monster.x -= random.randint(20,25)

        else:
            monster.contact(app)
            app.monsters.pop(app.monsters.index(monster))
            app.boomList.append((monster,3))
            app.explosion.play()

def firstStage(app):
    app.generation -= 1
    if app.generation //50 == app.generation / 50:
        app.limitPerRow = 0
        generateMonster(app)
    if app.generation == 0:
        app.bossStage = True

def drawGameOverPage(app):
    drawImage(app.gameOverPage,0,0,width = 700,height = 700)
    drawImage(app.homePageButton,372,612,width = 50,height = 50, align = 'center')

def drawWinPage(app):
    drawImage(app.winPage,0,0,width = 700,height = 700)
    drawImage(app.homePageButton,372,612,width = 50,height = 50, align = 'center')

# health attribute belongs to sniper, while it is the person receiving damage
class Sniper:
    def __init__(self):
        self.health = 200
        self.attackAttribute = 10
        self.bullets = 50
        self.bulletPerR = 5
        # 5fps for 30 secs
        self.fireDuration = 5 * 30
        self.freezeDuration = 5 * 30
        self.shield = False
        # CD per 10 sec
        self.shieldCD = 5 * 10
        self.shieldDuration = 5 * 2
        self.pressedShield = False

    def heal(self,app,n):
        self.health += n
        if self.health >= 400:
                self.health = 400
                app.maxHealth = True
                
    def damage(self,app,n):
        self.health -= n
        if self.health <= 0:
            self.health = 0
            app.gameOver = True
    
    def attack(self,monster):
        monster.health -= self.attackAttribute

    def useOrb(self,app,orb):
        if orb == 'heal':
            self.heal(app,110)
        if orb == 'fire':
            app.fire = True
        if orb == 'freeze':
            app.freeze = True
    

# drone: explode when it reaches the sniper baseline.
# change direction when it reaches boundary or it collide with another monster
class Monster1:
    def __init__(self,x,y):
        self.health = 100
        self.const = 10
        self.pOrb = 0.5-self.const/100
        self.x,self.y = x,y
        self.rgb = convertTorgb(self)
        self.attackAttri = 0

        
    # 50 explosion damage, dont have attack method
    def contact(self,app):
        app.sniper.damage(app,20)
    
    def move(self,app):
        for monster in app.monsters:
            if not monsterValid(app,monster):
                pass
        self.y += self.const
        self.x += random.randint(min(-self.const,self.const),max(-self.const,self.const))
        if self.x - 30 < 150:
            self.x += random.randrange(self.const,self.const*2)
        if self.x + 30 > 550:
            self.x -= random.randrange(self.const,self.const*2)

    def __hash__(self):
        return hash(self.x)
        
# move towards the sniper baseline, and it can avoid bullets, when bullets approach, it can move to right/left a little bit
class Monster2:
    def __init__(self,x,y):
        self.health = 75
        self.const = 1
        self.pOrb = 0.7-self.const/100
        self.x,self.y = x,y
        self.rgb = convertTorgb(self)
        self.attackAttri = 15
            
    def move(self,app):
        for monster in app.monsters:
            if not monsterValid(app,monster):
                pass
        self.y += 7
        
        for bullet in app.bulletsLoc:
            if bullet[0] - 50 < self.x < bullet[0] + 50:
                if bullet[1] - 50 < self.y < bullet[1] + 50:
                    self.x += random.randrange(min(-self.const*40,self.const*40),max(-self.const*40,self.const*40))
                    break
        if self.x - 30 < 150:
            self.x += random.randrange(self.const*15,self.const*20)
        if self.x + 30 > 550:
            self.x -= random.randrange(self.const*10,self.const*20)
        
    def __hash__(self):
        return hash(self.x)

    # attack 15 per 5 secs
    def attack(self,app):
        app.sniper.damage(app,self.attackAttri)
        # make sound as well
    
    # 20 explosion damage
    def contact(self,app):
        app.sniper.damage(app,20)
       
class Monster3:
    def __init__(self,x,y):
        self.health = 150
        self.const = 10
        self.pOrb = 0.8-self.const/100
        self.x,self.y = x,y
        self.rgb = convertTorgb(self)
        self.attackAttri = 20
        
    def move(self,app):
        for monster in app.monsters:
                if not monsterValid(app,monster):
                    pass
        if app.equip:
            self.y += 5
            self.x += random.randrange(min(-self.const,self.const),max(-self.const,self.const))
            if self.x - 30 < 150:
                self.x += random.randrange(self.const,self.const*2)
            if self.x + 30 > 550:
                self.x -= random.randrange(self.const,self.const*2)
        else:
            self.y += 7
            if app.personX > self.x:
                self.x += random.randrange(self.const,self.const*2)
            elif app.personX < self.x:
                self.x -= random.randrange(self.const,self.const*2)

    # attack 20 per 6 secs
    def attack(self,app):
        app.sniper.damage(app,self.attackAttri)

    # 20 explosion damage
    def contact(self,app):
        app.sniper.damage(app,20)

    def __hash__(self):
        return hash(self.x)

# bosses inherit alien attribute and modify some functions of Monster3
class Boss:
    def __init__(self,x,y):
        self.health = 1000
        self.attackAttri = 10
        self.x,self.y = x,y
        self.invisibility = False
        self.stage1 = True
        self.secs= 20
        self.rgb = convertTorgb(self)

    def move(self,app):
        if not self.invisibility:
            self.y += 1
        if not app.boss.stage1 and not self.invisibility:
            self.y += 0.6
            for bullet in app.bulletsLoc:
                if bullet[0] - 70 < self.x < bullet[0] + 70:
                    if bullet[1] - 70 < self.y < bullet[1] + 70:
                        self.x += random.randrange(-70,70)
                        break
            if self.x - 30 < 150:
                self.x = 150 + random.randrange(40,70)
            if self.x + 30 > 550:
                self.x = 550 - random.randrange(40,70)

    # health regen here
    def heal(self):
        self.health += 300
        if self.health > 1000:
            self.health = 1000
    
    def attack(self,app):
        app.sniper.health -= self.attackAttri

    def increasingAttack(self):
        if self.attackAttri < 50:
            self.attackAttri += 10
    
    def invisible(self):
        self.invisibility = True

    def summon(self,app):
        # 1 monster per 4 secs
        if app.bossSecs // 20 == app.bossSecs / 20 and self.health > 0:
            generateMonster(app)


# wood needs two bullets to destroy. Stone need three bullets to destroy
class Terrain:
    def __init__(self,app,x,y):
        self.x = x
        self.y = y
        app.terrainList.append(self)
        self.kind = random.choices(app.terrainKinds,[1/2,1/2])[0]
        if self.kind == 'wood': 
            self.health = 15 * 2
        else:
            self.health = 25 * 2

    def damage(self,x):
        self.health -= x
        if self.health <= 0:
            self.health = 0

    def __hash__(self):
        return hash(self.x)
    
# draw Intro Page and Play Page
def drawIntroPage(app):
    # this picture is generated by ChatGPT, url is https://files.oaiusercontent.com/file-Rv4Svqcgs01hKaW0WJWqQL7Q?se=2023-11-20T04%3A06%3A32Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3D8bd0eff9-9343-4f63-865c-02a24fd589bf.webp&sig=PUmd99cfkgnt1eXOeALr7cJLczqu33HnqCPmKVbyC6w%3D
    drawImage(app.image,-170,-70)
    drawImage(app.introCursor,app.cursorX,app.cursorY,width = 20, height = 30)
    drawLabel('hint: move the Alien into the middle button',340,50,fill = 'red', size = 20, font = 'monospace')
    drawRect(200,300,335,200,fill = None, border = 'gold',borderWidth = 20)
    drawRect(220,320,335-20-20,200-20-20,fill = 'grey', border = None,borderWidth = 10)
    drawLabel('START',365,400,size = 65,font = 'monospace',fill = 'red',bold = True)
    
def drawPlayPage(app):
    drawGreyBoard(app)
    drawBattleFields(app)
    drawSniper(app)
    drawPerson(app)
    drawMonsters(app)
    drawBullets(app)
    drawOrbs(app)
    drawquestionMark(app)
    drawAchievementBadges(app)
    drawStage(app)
    drawBuff(app)
    drawDifficultLvl(app)
    drawTerrain(app)
    if app.bossStage:
        drawBoss(app)
    drawShield(app)
    drawTrackBullets(app)
    drawHP(app)
    drawAim(app)
    drawBoom(app)

def drawGreyBoard(app):
    drawRect(0,0,700,700,fill = 'Grey')
    
def drawBattleFields(app):
    drawImage(app.battlefield,50,100,width = 500,height = 500)
    
def drawSniper(app):
    # url for sniper https://a0.anyrgb.com/pngimg/1608/1686/spaceship-sprite-star-destroyer-starship-top-view-destroyer-2d-computer-inkscape-spacecraft-sprite-ship.png
    drawImage(app.sniperPic,300,600,width = 20, height = 30,rotateAngle = -90 + app.angle,align = 'center')

def drawPerson(app):
    # if app.equip:
    drawImage(app.personbackview,app.personX,620,width = 20, height = 30,align = 'center')

def drawMonsters(app):
    for e in app.monsters:
        if type(e) == Monster1:
            if not e.y >= 610:
                drawImage(app.monster1Pic,e.x,e.y,width = 60, height = 60,align = 'center')   
        elif type(e) == Monster2:
            if not e.y >= 610:
                drawImage(app.monster2Pic,e.x,e.y,width = 60, height = 60,align = 'center')
        else:
            if not e.y >= 610:
                drawImage(app.monster3Pic,e.x,e.y,width = 60, height = 60,align = 'center')
        # explode BOOM effect: drawImage(app.Boom,e.x,e.y,width = 60, height = 60,align = 'center')

def drawBullets(app):
    if app.bullets != []:
        for i in range(len(app.bullets)):
            if app.fire:
                drawImage(app.fireBullet,app.bulletsLoc[i][0],app.bulletsLoc[i][1],width = 10,height = 30,rotateAngle = app.bullets[i],align = 'center')
                if app.freeze:
                    # this is a combo of freeze and fire bullet
                    drawImage(app.firefreezeBullet,app.bulletsLoc[i][0],app.bulletsLoc[i][1],width = 10,height = 30,rotateAngle = app.bullets[i],align = 'center')
            elif app.freeze:
                drawImage(app.freezeBullet,app.bulletsLoc[i][0],app.bulletsLoc[i][1],width = 10,height = 30,rotateAngle = app.bullets[i],align = 'center')
            else:
                drawImage(app.bullet,app.bulletsLoc[i][0],app.bulletsLoc[i][1],width = 10,height = 30,rotateAngle = app.bullets[i],align = 'center')

def drawOrbs(app):
    if app.orbs != []:
        for i in range(len(app.orbs)):
            if app.orbs[i] == 'heal':
                drawImage(app.heal,app.orbLoc[i],620, width = 30, height = 30, align = 'center')
            if app.orbs[i] == 'fire':
                drawImage(app.fireImage,app.orbLoc[i],620, width = 30, height = 30, align = 'center')
            if app.orbs[i] == 'freeze':
                drawImage(app.freezeImage,app.orbLoc[i],620, width = 30, height = 30, align = 'center')

def drawAim(app):
    drawImage(app.aimCursor,app.aimCursorX,app.aimCursorY,width = 20,height = 20,align = 'center')

def drawShield(app):
    drawLabel('W',635,275+75,font = 'montserrat',size = 15,align = 'center')
    drawImage(app.shieldPic,675,275+75,width = 50,height = 50, align = 'center',opacity = app.shieldOpacity)

def drawHP(app):
    drawRect(50,660,500,40,fill = None, border = 'gold')
    if app.sniper.health > 0:
        drawRect(50,660,500*app.sniper.health/400,40, border = 'green',fill = 'green')
    drawLabel(f'HP: {app.sniper.health}/400',300,680,align = 'center',font = 'montserrat',size = 20)

    # draw monsters HP here
    for monster in app.monsters:
        drawRect(monster.x,monster.y+30,50,10,align = 'center', fill = None, border= 'black')
        if monster.health > 0:
            if type(monster) == Monster1:
                h = 100
            if type(monster) == Monster2:
                h = 75
            if type(monster) == Monster3:
                h = 150
            drawRect(monster.x-25,monster.y+30-5,monster.health/h*50,10, fill = rgb(monster.rgb[0],monster.rgb[1],monster.rgb[2]))
    
    # boss here
    if app.bossStage:
        if app.boss.health >0:
            h = 1000
            drawRect(app.boss.x,app.boss.y+30,50,10,align = 'center', fill = None, border= 'black')
            drawRect(app.boss.x-25,app.boss.y+30-5,app.boss.health/h*50,10, fill = rgb(app.boss.rgb[0],app.boss.rgb[1],app.boss.rgb[2]))

def drawTrackBullets(app):
    drawLabel('Skills',675,310,font = 'montserrat',size = 15,align = 'center')
    drawLabel('S',635,275+125+25,font = 'montserrat',size = 15,align = 'center')
    drawImage(app.trackBulletsPic,675,275+125+25,width = 50,height = 50, align = 'center',opacity = app.trackOpacity)


def convertTorgb(monster):
    rgbList = [(153,0,0),(204,0,0),(255,0,0),(255,51,51),(255,102,102),(255,153,153),(255,204,204)]
    rgbList.reverse()
    if type(monster) == Monster1:
        health = 100
    if type(monster) == Monster2:
        health = 75
    if type(monster) == Monster3:
        health = 150
    if type(monster) == Boss:
        health = 1000
    index = int(monster.health/health*len(rgbList))- 1
    return rgbList[index]

def drawquestionMark(app):
    drawImage(app.questionMark,675,97.5,width = 50,height = 50,align = 'center')

def drawAchievementBadges(app):
    drawLabel('Badges',475,17.5,align = 'center',size = 15,font = 'montserrat')
    drawRect(400,0,150,70,fill = None,border = 'gold')
    drawImage(app.twentyBulletsPic,475-75/2,52.5-4,width = 35,height = 35,opacity = app.twentyBulletsOpacity if not app.twentyBullets else 100,align = 'center' )
    drawImage(app.maxHealthPic,475+75/2,52.5-4,width = 35,height = 35,opacity = app.maxHealthOpacity if not app.maxHealth else 100,align = 'center' )

def drawStage(app):
    drawRect(550,0,150,70,fill = None,border = 'gold')
    drawLabel('*Stage 1: kill monsters!',625,17.5,align = 'center',size = 15,font = 'montserrat',opacity = app.stageOpacity1)
    drawLabel('*Stage 2: kill the boss!',625,52.5,align = 'center',size = 15,font = 'montserrat',opacity = app.stageOpacity2)

def drawBuff(app):
    drawRect(650,125,50,125,fill = None, border = 'gold')
    drawLabel('Buffs',675,137.5,size = 15,font = 'montserrat')
    drawImage(app.fireBuff,650,150,width = 50,height = 50,opacity = app.fireBuffOpacity)
    drawImage(app.freezeBuff,650,200,width = 50,height = 50,opacity = app.freezeBuffOpacity)

def drawBoss(app):
    # the fill is from cmu graphics image tutorial
    for boss in app.bossList:
        drawImage(app.BossPic,app.boss.x,app.boss.y,align = 'center',width = 100,height = 120,opacity = app.bossOpacity,fill= None if not app.boss.invisibility else gradient('red', 'orange', 'yellow'))

def drawDifficultLvl(app):
    drawLabel(f'adaptive difficulty: {int(app.score*1000)/1000}',250,30,align='right',font = 'montserrat')
    if app.harder:
        drawLabel(f'''It's getting harder''',250,60,align='right',font = 'montserrat')
    elif app.harder==None:
        drawLabel(f'''It's not increasing/decreasing difficulty''',250,60,align='right',font = 'montserrat')
    else:
        drawLabel(f'''It's not getting harder''',250,60,align='right',font = 'montserrat')
def drawTerrain(app):
    for terrain in app.terrainList:
        if terrain.kind == 'wood':
            drawImage(app.woodPic,terrain.x,terrain.y,width = 30,height = 30,align = 'center')
        else:
            drawImage(app.stonePic,terrain.x,terrain.y,width = 50,height = 50,align = 'center')

def drawHowtoPlay(app):
    drawImage(app.howtoplay,0,0,width = 700,height = 700)

# helper functions
def bottonPress(mouseX,mouseY,x1,y1,x2,y2):
    return x1<=mouseX<=x2 and y1<=mouseY<=y2
def average(list):
    return sum(list)/len(list)
def distance(x,y,a,b):
    return ((x-a)**2+(y-b)**2)**0.5

# openImage and loadSound is from piazza:https://piazza.com/class/lkq6ivek5cg1bc/post/2147
def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))
def loadSound(relativePath):
    # Convert to absolute path (because pathlib.Path only takes absolute paths)
    absolutePath = os.path.abspath(relativePath)
    # Get local file URL
    url = pathlib.Path(absolutePath).as_uri()
    # Load Sound file from local URL
    return Sound(url)

def main():
    runApp(width = 700,height = 700)

main()








