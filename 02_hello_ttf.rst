第二节 绘制汉字的 Hello World!
==============================
在上一课我们学习了如何绘制一张图片, 现在我们要绘制文字.


准备资源 (素材)
---------------
我们使用 SDL_ttf 来绘制 TTF 字体.

在 Windows 下, 我们使用 `楷体` (simkai.ttf).

在 Debian 下, 我们使用 unifont, 如果没有安装, 你需要使用如下命令安装::

  aptitude install ttf-unifont

或者你可以使用任何一个系统内已存在的字体, 只要你知道如何取得完整的文件名.

注意, 字体文件要支持中文, 否则中文那里, 你会看到一堆 `口`.

另外, 我们可以自备字体, 来避免不同操作系统的问题, 当然会导致资源文件变大. 在
`工作目录` 下已经有一个 res 的文件夹了, 将 `unifont-8.0.01.ttf`_ 下载到此处.

.. _`unifont-8.0.01.ttf`: http://unifoundry.com/pub/unifont-8.0.01/font-builds/unifont-8.0.01.ttf

.. note::

  unifont-8.0.01.ttf 的许可证是 GPLv2 附带字体嵌入例外.


编码说明
--------
重复的地方我们就不讲了, 我们直接设置一个 TTF 变量来代替实际的字体::

  TTF = 'C:\\Windows\\Fonts\\simkai.ttf' # Windows
  TTF = '/usr/share/fonts/truetype/unifont/unifont.ttf' # Debian
  TTF = RESOURCES.get_path('unifont-8.0.01.ttf') # 自备字体

之后我们准备两个颜色, 白色 white, 黑色 black::

  white = sdl2.ext.Color(255, 255, 255)
  black = sdl2.ext.Color(0, 0, 0)

在 SDL 库初始化完毕后, 我们需要创建一个字体管理器 fm, 来加载字体::

  fm = sdl2.ext.FontManager(TTF, color=black, bg_color=white)

在精灵工厂创建完毕后, 我们用精灵工厂生成 2 个精灵, sprite_eng 是英文, sprite_chs
是中文, 指定使用 fm 的默认字体::

  sprite_eng = factory.from_text('Hello World!', fontmanager=fm)
  sprite_chs = factory.from_text('你好, 世界!', fontmanager=fm)

在精灵渲染系统创建完毕后, 我们去渲染这 2 个精灵::

  spriterenderer.render(sprite_eng, 0, 16*4)
  spriterenderer.render(sprite_chs, 0, 16*5)

注意, 渲染的时候, 我们多指定了 2 个参数 (0, 16*4), 这是 sprite_eng
绘制位置的坐标, 代表在绘图区域左上角向右 0 个像素, 向下 16*4 个像素处, 绘制
sprite_eng, 坐标 (0, 16*4) 也是 sprite_eng 的左上角. sprite_chs 需要再向下 16
个像素, 所以我们用 16*5.

为什么用 16, 因为 `sdl2.ext.FontManager` 的默认字体大小是 16, 具体参数看 `注解`.

.. note::

  计算机中的平面直角坐标系 (笛卡尔坐标系) 与数学中的有所不同, 原点 (0, 0)
  在左上角, 而数学中的原点在左下角. 这导致 y 轴 (纵坐标) 计算方式的不同,
  向上为负, 向下为正.

  可以参考: http://fex.baidu.com/blog/2014/05/coordinate-and-transform/

.. note::

  计算机中常用的颜色格式是 RGBA. R 是红色. G 是绿色. B 是蓝色. A 是透明度.
  按照叠加型原色显示 32 位的颜色. R, G, B, A 各占 8 位. 有时我们省略为 RGB,
  是完全不透明.

.. note::

  `sdl2.ext.FontManager` 完整的初始化参数为:

  ========= ====== ============================== ====
  font_path 路径名 str
  alias     别名   None                           可选
  size      大小   默认 16                        可选
  color     前景色 默认 白色 Color(255, 255, 255) 可选
  bg_color  背景色 默认 黑色 Color(0, 0, 0)       可选
  ========= ====== ============================== ====


其他说明
--------
* 源码下载: `hello_ttf.py`_.
* 字体下载: `unifont-8.0.01.ttf`_.

.. _`hello_ttf.py`: _static/src/hello_ttf.py
