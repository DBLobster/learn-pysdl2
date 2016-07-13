#!/usr/bin/env python3

import sdl2.ext

RESOURCES = sdl2.ext.Resources(__file__, 'res')

#TTF = 'C:\\Windows\\Fonts\\simkai.ttf' # Windows
#TTF = '/usr/share/fonts/truetype/unifont/unifont.ttf' # Debian
TTF = RESOURCES.get_path('unifont-8.0.01.ttf') # 自备字体

white = sdl2.ext.Color(255, 255, 255)
black = sdl2.ext.Color(0, 0, 0)

sdl2.ext.init()

fm = sdl2.ext.FontManager(TTF, color=black, bg_color=white)

window = sdl2.ext.Window('Hello World!', size=(320, 240))
window.show()

factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

#renderer = sdl2.ext.Renderer(window)
#factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)

sprite = factory.from_image(RESOURCES.get_path('hello.png'))
sprite_eng = factory.from_text('Hello World!', fontmanager=fm)
sprite_chs = factory.from_text('你好, 世界!', fontmanager=fm)

spriterenderer = factory.create_sprite_render_system(window)
spriterenderer.render(sprite)
spriterenderer.render(sprite_eng, 0, 16*4)
spriterenderer.render(sprite_chs, 0, 16*5)

processor = sdl2.ext.TestEventProcessor()
processor.run(window)

sdl2.ext.quit()
