第一课 Hello World!
===================
不能免俗, 上来先 Hello World! 吧.


准备资源 (素材)
---------------
首先在 `工作目录` 建立一个叫 res (resource) 的文件夹, 将 `hello.png`_
下载到此处.

.. _`hello.png`: _static/src/res/hello.png


编码说明
--------
第一步要加入 pysdl2 引用, 我们这里为了简单, 直接引用了扩展库::

  import sdl2.ext

之后, 我们要初始化资源加载工具, 参数 'res' 就是上一节我们讲到的 res 文件夹::

  RESOURCES = sdl2.ext.Resources(__file__, 'res')

再之后, 我们初始化 SDL 库::

  sdl2.ext.init()

再之后, 我们创建窗体并展示, 第一个参数是窗体标题, 第二个参数是窗体大小
(长, 宽)::

  window = sdl2.ext.Window('Hello World!', size=(320, 240))
  window.show()

再之后, 我们创建一个软件的精灵工厂::

  factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

硬件的精灵工厂重绘机制略有不同, 我们此处略过.

再之后, 我们使用精灵工厂加载图片并创建一个精灵::

  sprite = factory.from_image(RESOURCES.get_path('hello.png'))

再之后, 我们使用经理工厂为窗体创建一个精灵渲染系统, 用它去渲染精灵::

  spriterenderer = factory.create_sprite_render_system(window)
  spriterenderer.render(sprite)

这时, 图像就可以显示在窗体上了. 但是窗体现在是不听使唤的, 点什么都不管用.

所以, 我们要调用一个测试的事件循环, 使用它来侦听窗体的事件::

  processor = sdl2.ext.TestEventProcessor()
  processor.run(window)

这个测试的事件循环是一个死循环, 它一直在侦听窗体接收到的事件, 除非发生了退出事件
(SDL_QUIT, 就是点击窗体右上角的那个 X, 或者 Alt+F4), 则跳出循环.

最后, 在程序退出前, 我们要销毁 SDL 库, 释放我们之前使用的资源::

  sdl2.ext.quit()

.. note::

  在老式的 2D 游戏中, 活动块被叫做精灵, 与之对应的就是背景层.

.. note::

  `RESOURCES.get_path('hello.png')` 返回 `hello.png`_ 的实际路径.

  pysdl2 扩展库中的资源管理加载工具只关心文件名. 注意, 将来如果你游戏做的很大,
  资源中有重名文件时, 这可能是出现问题的一个点.

  当然, 我们也可以利用这个机制, 制作更新包或者 mod.


其他说明
--------
* 源码下载: `hello.py`_.

本章节基本上是完全照抄的 pysdl2 文档的 hello world.
(http://pysdl2.readthedocs.io/en/latest/tutorial/helloworld.html)

.. _`hello.py`: _static/src/hello.py
