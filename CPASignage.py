#   CPA Digital Signage for project XCloud and Ecopanel
#   
#   Software bajo licencia, se prohibe todo uso no autorizado de esta aplicacion
#   Version inicial : v1.0
#   Producto : CPA python client
#   Fecha de Desarrollo : 17/11/2015
#   

# --------- importacion de librerias ----------
import pyglet
import time
# --------------------- Fin -------------------

#
#   Archivo : CPASignage.py
#   Descripcion : Archivo principal de la aplicacion
#
#

# --------- Declaracion de variables ----------
MODO_DEBUG = True
# --------------------- Fin -------------------




window = pyglet.window.Window()
window.height = 1080
window.width = 1920
window.set_fullscreen(True)




label2 = pyglet.text.Label('ECOPANELTV',font_name='Berlin Sans FB',font_size=15,x=1150, y=850,anchor_x='center', anchor_y='center')
label3 = pyglet.text.Label('www.tecnologiaquerespira.cl',font_name='Berlin Sans FB',font_size=8,x=1150, y=834,anchor_x='center', anchor_y='center')
txtVersion = pyglet.text.Label("EcoPanel Outdoor Signage v1.0 ",font_name='Cooper Black',font_size=12,x=1100, y=20,anchor_x='center', anchor_y='center')
imagen = pyglet.resource.image('src/video/br.jpg')
imagen2 = pyglet.resource.image('src/video/cab.jpg')


playlist = ["src/video/OutdoorTV-FLYFISHING.flv","src/video/Outdoor_teaserExploracionLippiCoyahique.flv"]

videoinit = pyglet.media.load(playlist[0])
itemplay = 1
player = pyglet.media.Player()
player.volume = 10
player.queue(videoinit)
player.play()

@window.event
def on_draw():
    global playlist, itemplay, player
    window.clear()
    imagen2.blit(0,0,0,1234,150)
    txtVersion.draw()
    imagen.blit(1234,0,0,308,870)
    
    if player.time >=player.source.duration-0.2:
        player.next_source()
        player = None
        player = pyglet.media.Player()
        video = pyglet.media.load(playlist[itemplay] )
        if(itemplay < len(playlist)-1):
            itemplay = itemplay + 1
        else:
            itemplay = 0
        player.queue(video)
        player.play()
    else:
        player.get_texture().blit(0, 150,0,1234,720)

    label2.draw()
    label3.draw()
    


pyglet.app.run()
