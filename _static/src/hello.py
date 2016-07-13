#!/usr/bin/env python3

import sdl2.ext

RESOURCES = sdl2.ext.Resources(__file__, 'res')

sdl2.ext.init()

window = sdl2.ext.Window('Hello World!', size=(320, 240))
window.show()

factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

#renderer = sdl2.ext.Renderer(window)
#factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)

sprite = factory.from_image(RESOURCES.get_path('hello.png'))

spriterenderer = factory.create_sprite_render_system(window)
spriterenderer.render(sprite)

processor = sdl2.ext.TestEventProcessor()
processor.run(window)

sdl2.ext.quit()
