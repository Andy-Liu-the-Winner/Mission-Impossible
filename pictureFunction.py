from cmu_graphics import *
from PIL import Image
import os, pathlib
import random
import math

def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))
def introPicture(app):
    # I learned importing image from https://piazza.com/class/lkq6ivek5cg1bc/post/2147
    # this picture is generated by ChatGPT, url is https://files.oaiusercontent.com/file-Rv4Svqcgs01hKaW0WJWqQL7Q?se=2023-11-20T04%3A06%3A32Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3D8bd0eff9-9343-4f63-865c-02a24fd589bf.webp&sig=PUmd99cfkgnt1eXOeALr7cJLczqu33HnqCPmKVbyC6w%3D
    app.image = Image.open("images/generatedPicture.webp")    
    app.image = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/generatedPicture.webp"))
    app.image = openImage("images/generatedPicture.webp")
    app.image = CMUImage(app.image)
    # url for my intro page cursor picture is: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSa9sKDptTne436PlNBygXBIcJvzUDOBe4wqT5P9Oec75KZKJlMzegD5u0oELqCIXfi-6c&usqp=CAU
    app.introCursor = Image.open("images/cursorForIntroPage.png")    
    app.introCursor = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/cursorForIntroPage.png"))
    app.introCursor = openImage("images/cursorForIntroPage.png")
    app.introCursor = CMUImage(app.introCursor)

def playPagePicture(app):
    # pictures are for monsters 
    # monster1 is from url: https://techcrunch.com/wp-content/uploads/2019/09/monster-dot-com.jpg?w=1390&crop=1
    app.monster1Pic = Image.open("images/Monster1.png")    
    app.monster1Pic = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/Monster1.png"))
    app.monster1Pic = openImage("images/Monster1.png")
    app.monster1Pic = CMUImage(app.monster1Pic)

    # monster2 is from url: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSg0iFVPL66S8yPrEtKK-vIcp1e1ATsV2ZjGtI8T6gMpo3L88N_imDqrPvctrrU_2LveX4&usqp=CAU
    app.monster2Pic = Image.open("images/Monster2.png")    
    app.monster2Pic = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/Monster2.png"))
    app.monster2Pic = openImage("images/Monster2.png")
    app.monster2Pic = CMUImage(app.monster2Pic)

    # monster3 is from url: https://cdn.pixabay.com/photo/2014/08/25/09/26/monster-426995_1280.jpg
    app.monster3Pic = Image.open("images/Monster3.png")    
    app.monster3Pic = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/Monster3.png"))
    app.monster3Pic = openImage("images/Monster3.png")
    app.monster3Pic = CMUImage(app.monster3Pic)

    # monster from url: https://t4.ftcdn.net/jpg/02/46/18/65/360_F_246186594_W8zi1UoQ4YCXjMSPaWy1h76RTXWSqtQC.jpg
    app.BossPic = Image.open("images/Boss.png")    
    app.BossPic = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/Boss.png"))
    app.BossPic = openImage("images/Boss.png")
    app.BossPic = CMUImage(app.BossPic)

    
    # normal bullet is from url: https://cdn.mos.cms.futurecdn.net/YHVfbsDepWRfsnSVtPq65k-1200-80.jpg.webp
    app.bullet = Image.open("images/bullet.png")    
    app.bullet = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/bullet.png"))
    app.bullet = openImage("images/bullet.png")
    app.bullet = CMUImage(app.bullet)

    # fire Bullet is from url: https://files.oaiusercontent.com/file-gdh611EPhFijDklHHPyYfdgO?se=2023-11-28T01%3A42%3A40Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3D096d74d6-a32d-437b-88d6-ab2c9124b73a.webp&sig=%2BsHlfYWJFQ1vS%2Bd25qdoVHCN/WYOt58nZ2jdAk0bYCg%3D
    app.fireBullet = Image.open("images/fireBullet.png")    
    app.fireBullet = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/fireBullet.png"))
    app.fireBullet = openImage("images/fireBullet.png")
    app.fireBullet = CMUImage(app.fireBullet)
    
    # freeze Bullet is from url: https://files.oaiusercontent.com/file-R3GQdJDRpsj9oAhyWr3XOfA2?se=2023-11-28T01%3A48%3A47Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3Dcad7d3b0-9bf5-49d5-87c4-1d74366e36b4.webp&sig=htriF8hIjTIETUdhhhCVHJLRnMy2vAK4vDlm%2Bk5Db2k%3D
    app.freezeBullet = Image.open("images/freezeBullet.png")    
    app.freezeBullet = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/freezeBullet.png"))
    app.freezeBullet = openImage("images/freezeBullet.png")
    app.freezeBullet = CMUImage(app.freezeBullet)
    
    # fire & freeze Bullet is from url: https://files.oaiusercontent.com/file-bO8nj8Xc2YpaDbC2FjYOqrzu?se=2023-11-28T01%3A53%3A15Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3D952b2741-e82a-4519-8fb1-e97178e4a952.webp&sig=oStf4j0nA5yI9IgTfHMPTFb6mrwRMy7T/mWywx00VAM%3D
    app.firefreezeBullet = Image.open("images/firefreezeBullet.png")    
    app.firefreezeBullet = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/firefreezeBullet.png"))
    app.firefreezeBullet = openImage("images/firefreezeBullet.png")
    app.firefreezeBullet = CMUImage(app.firefreezeBullet)

    # draw boom effects, url: https://www.harrisburgu.edu/wp-content/uploads/Boom-1258x686.png
    app.boom = Image.open("images/Boom.png")    
    app.boom = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/Boom.png"))
    app.boom = openImage("images/Boom.png")
    app.boom = CMUImage(app.boom)

    # draw person back view: https://cdnb.artstation.com/p/assets/images/images/019/189/773/large/siserman-oana-alexandra-render-01111.jpg?1562413964
    app.personbackview = Image.open("images/personbackview.png")    
    app.personbackview = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/personbackview.png"))
    app.personbackview = openImage("images/personbackview.png")
    app.personbackview = CMUImage(app.personbackview)
    
    # draw three orbs. Url: https://openclipart.org/image/800px/179860
    app.heal = Image.open("images/heal.png")    
    app.heal = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/heal.png"))
    app.heal = openImage("images/heal.png")
    app.heal = CMUImage(app.heal)

    app.fireImage = Image.open("images/fire.png")    
    app.fireImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/fire.png"))
    app.fireImage = openImage("images/fire.png")
    app.fireImage = CMUImage(app.fireImage)

    app.freezeImage = Image.open("images/freeze.png")    
    app.freezeImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/freeze.png"))
    app.freezeImage = openImage("images/freeze.png")
    app.freezeImage = CMUImage(app.freezeImage)

    # draw battlefield, url: https://files.oaiusercontent.com/file-7iQDBBQQC1NavDoxQQpYhMoK?se=2023-11-28T00%3A38%3A13Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3Dd5a96a41-8882-4187-96f9-711fec20dcf3.webp&sig=hDsj7W7jRUCLnOHG93khjI%2BIMqh/1Rcrc9Cc1WjA6dI%3D
    app.battlefield = Image.open("images/battlefield.png")    
    app.battlefield = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/battlefield.png"))
    app.battlefield = openImage("images/battlefield.png")
    app.battlefield = CMUImage(app.battlefield)

    # buff Section picture is from url:https://files.oaiusercontent.com/file-qLV91SEvsMER0dhk2Lz1TMQu?se=2023-11-28T04%3A41%3A57Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3D9631d2ca-bf52-43ae-85aa-2527b0b5846d.webp&sig=WAmMpNgl453JP%2B7V7Rd6u8X1w4Zhtm%2BT0%2BY%2BYp/vjwE%3D
    app.fireBuff = Image.open("images/fireBuff.png")    
    app.fireBuff = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/fireBuff.png"))
    app.fireBuff = openImage("images/fireBuff.png")
    app.fireBuff = CMUImage(app.fireBuff)
    
    app.freezeBuff = Image.open("images/freezeBuff.png")    
    app.freezeBuff = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/freezeBuff.png"))
    app.freezeBuff = openImage("images/freezeBuff.png")
    app.freezeBuff = CMUImage(app.freezeBuff)

    # question mark is from url: https://files.oaiusercontent.com/file-bQM9VOc8VjQyl17KaFkNoPKr?se=2023-11-28T05%3A20%3A00Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3D5a2a8484-cdf4-49b8-9eb9-4e489abf84f9.webp&sig=P1VExNB3yLr0M%2BIDH3WWAuLMuftPKdbmFoLT9VDx6Ag%3D
    app.questionMark = Image.open("images/questionMark.png")    
    app.questionMark = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/questionMark.png"))
    app.questionMark = openImage("images/questionMark.png")
    app.questionMark = CMUImage(app.questionMark)

    # how to play page: I created by myself
    app.howtoplay = Image.open("images/howtoplay.png")    
    app.howtoplay = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/howtoplay.png"))
    app.howtoplay = openImage("images/howtoplay.png")
    app.howtoplay = CMUImage(app.howtoplay)

    # aimCursor here: https://files.oaiusercontent.com/file-jkmxpBxKIiJbGuzlYTJlIMA5?se=2023-12-05T00%3A53%3A39Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3Dd2422c42-7ec7-4328-934a-1af9655a4f37.webp&sig=dneDAK%2BCPPYfzoHaKJxGnft404z4Bsw2hsEJP1aFffo%3D
    app.aimCursor = Image.open("images/aimCursor.png")    
    app.aimCursor = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/aimCursor.png"))
    app.aimCursor = openImage("images/aimCursor.png")
    app.aimCursor = CMUImage(app.aimCursor) 

    # shield picture is from: https://files.oaiusercontent.com/file-ziAheRM59c3JYPD0WjlpqWdZ?se=2023-12-05T00%3A43%3A34Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3Db42056ad-8cba-4657-a890-b9b496609832.webp&sig=Q6NlTA0tj/X1KiY3/5xev6k/92dXnts//V8BOGWUvoY%3D
    app.shieldPic = Image.open("images/shieldPic.png")    
    app.shieldPic = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/shieldPic.png"))
    app.shieldPic = openImage("images/shieldPic.png")
    app.shieldPic = CMUImage(app.shieldPic) 

    # stone picture from here: https://files.oaiusercontent.com/file-g5Qf3YvVj3AS1rkZRzQszBV0?se=2023-12-05T03%3A04%3A35Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3D1213c13d-fb4a-47e6-a5b3-ee0763b3819c.webp&sig=bLvBlQewZ8Zkp91/eN4XtKyaf9UomZru1Q%2B4e24E1iw%3D
    app.stonePic = Image.open("images/stonePic.png")    
    app.stonePic = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/stonePic.png"))
    app.stonePic = openImage("images/stonePic.png")
    app.stonePic = CMUImage(app.stonePic) 

    # wood picture from here: https://files.oaiusercontent.com/file-oKJ6GrunUu0QQf8cmPpggMLT?se=2023-12-05T03%3A08%3A45Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3Ddef51a7e-4658-443c-bb2f-3a82247d018b.webp&sig=pySDjIPm6r1NoB5%2BY3E944tmM3vi3kvvAMr98JpS9Zc%3D
    app.woodPic = Image.open("images/woodPic.png")    
    app.woodPic = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/woodPic.png"))
    app.woodPic = openImage("images/woodPic.png")
    app.woodPic = CMUImage(app.woodPic)

    # twenty accuracy is from here: https://files.oaiusercontent.com/file-oJf56cZR9zwIyJNwwqLViHow?se=2023-12-05T08%3A01%3A14Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3D2752aa89-abd5-431e-bd0e-8f2dca914981.webp&sig=HD/6HChI8NSskzmUWnK92ePU3xwwjIkMFonwliL96XU%3D
    app.twentyBulletsPic = Image.open("images/twentyBulletsPic.png")    
    app.twentyBulletsPic = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/twentyBulletsPic.png"))
    app.twentyBulletsPic = openImage("images/twentyBulletsPic.png")
    app.twentyBulletsPic = CMUImage(app.twentyBulletsPic)

    # max health pic is from here: https://files.oaiusercontent.com/file-sJNB6SxjTsaXSLKauTsGC0qc?se=2023-12-05T08%3A07%3A26Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3Dc8053cf6-1f12-4188-b05f-2fc262f4bcaa.webp&sig=kv4k6/oUC67uQH9qHBJjnJN4nG3a2bHv4TKRbfbUkjo%3D
    app.maxHealthPic = Image.open("images/maxHealthPic.png")    
    app.maxHealthPic = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/maxHealthPic.png"))
    app.maxHealthPic = openImage("images/maxHealthPic.png")
    app.maxHealthPic = CMUImage(app.maxHealthPic)

def winPagePicture(app):
    # url from: https://files.oaiusercontent.com/file-bV9PIu97DtKEFzSzuWB78nLF?se=2023-11-30T22%3A13%3A29Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3Dbd88d455-ad33-486d-80e5-dd7772043310.webp&sig=f1RrEvdXgeDYllpjx2E8WYHRJJZayXDtfdXdFoxtuBo%3D
    app.winPage = Image.open("images/winPage.png")    
    app.winPage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/winPage.png"))
    app.winPage = openImage("images/winPage.png")
    app.winPage = CMUImage(app.winPage)
    
    # url from: https://files.oaiusercontent.com/file-TvEPSV6PUTHKLqfLD007NwwK?se=2023-11-30T23%3A26%3A22Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3Df22538ee-a6ad-44cb-ab73-e26f06c45abe.webp&sig=KqyfmITrrmQyWl2QOvAblzkJwqPOw6M2MgKkJ6wlHSs%3D
    app.homePageButton = Image.open("images/homePageButton.png")    
    app.homePageButton = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/homePageButton.png"))
    app.homePageButton = openImage("images/homePageButton.png")
    app.homePageButton = CMUImage(app.homePageButton)

def gameOverPagePicture(app):
        # url from: https://files.oaiusercontent.com/file-eW46J1pG3LNMn0LjRlXUa9W9?se=2023-11-30T23%3A12%3A15Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3D5214a310-927f-4b94-b609-0f90396d2321.webp&sig=4Ilwm/YlJg6BekSrc6jq4WTxd4piU5RXckQdkMz1Y/0%3D
    app.gameOverPage = Image.open("images/gameOverPage.png")    
    app.gameOverPage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/gameOverPage.png"))
    app.gameOverPage = openImage("images/gameOverPage.png")
    app.gameOverPage = CMUImage(app.gameOverPage)

def winPagePicture(app):
    # url from: https://files.oaiusercontent.com/file-bV9PIu97DtKEFzSzuWB78nLF?se=2023-11-30T22%3A13%3A29Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3Dbd88d455-ad33-486d-80e5-dd7772043310.webp&sig=f1RrEvdXgeDYllpjx2E8WYHRJJZayXDtfdXdFoxtuBo%3D
    app.winPage = Image.open("images/winPage.png")    
    app.winPage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/winPage.png"))
    app.winPage = openImage("images/winPage.png")
    app.winPage = CMUImage(app.winPage)
    
    # url from: https://files.oaiusercontent.com/file-TvEPSV6PUTHKLqfLD007NwwK?se=2023-11-30T23%3A26%3A22Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3Df22538ee-a6ad-44cb-ab73-e26f06c45abe.webp&sig=KqyfmITrrmQyWl2QOvAblzkJwqPOw6M2MgKkJ6wlHSs%3D
    app.homePageButton = Image.open("images/homePageButton.png")    
    app.homePageButton = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/homePageButton.png"))
    app.homePageButton = openImage("images/homePageButton.png")
    app.homePageButton = CMUImage(app.homePageButton)

    # url from: file:///Users/liuxuanting/Downloads/72a38180-59a4-42a8-a715-9ab6a766e23a.webp
    app.trackBulletsPic = Image.open("images/trackBulletsPic.png")    
    app.trackBulletsPic = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/trackBulletsPic.png"))
    app.trackBulletsPic = openImage("images/trackBulletsPic.png")
    app.trackBulletsPic = CMUImage(app.trackBulletsPic)

def playPicture(app):
    app.sniperPic = Image.open("images/sniperPic.png")    
    app.sniperPic = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/sniperPic.png"))
    app.sniperPic = openImage("images/sniperPic.png")
    app.sniperPic = CMUImage(app.sniperPic)
