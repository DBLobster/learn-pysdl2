硬件加速版 Hello World!
=======================
不能免俗, 上来先 Hello World! 吧.


准备资源 (素材)
---------------
本节素材与 "Hello World!"(:ref:`hello-label`) 相同, 如果不明白请参考第一节.

.. _`hello.png`: _static/src/res/hello.png


编码说明
--------
与 "Hello World!" 的代码也是基本相同的, 只需将精灵工厂从软件::

  factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

换成基于硬件的材质, 当然要初始化一个硬件画笔 Render::

  renderer = sdl2.ext.Renderer(window)
  factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)

Render 是在 SDL 2.0 引入的, 可以认为是硬件画笔.

其他说明
--------
* 源码下载: `hello_hard.py`_.

.. _`hello_hard.py`: _static/src/hello_hard.py
