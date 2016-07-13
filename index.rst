PySDL2 教程
===========
PySDL2_ 是 SDL_ 库 2.0 版本的 Python_ 封装, 使用 :mod:`ctypes` 模式,
纯粹 python 代码, 而且是许可证是公共域 (`Public Domain`_), 完全没有任何限制.

SDL_ 全称为 Simple DirectMedia Layer, 是一个跨平台的多媒体开发库. 很多视频软件,
游戏, 模拟器都使用 SDL_ 作为底层. SDL_ 2.0 主要优化了硬件绘画, 并且许可证从
`LGPL 2.1`_ 切换到了 zlib_, 更为宽松.

Python_ 是一种计算机编程语言, 整体上语法简单, 便于学习 (指的是英语为母语的国家
T_T).

使用 PySDL2, 本意是避免繁琐的 C/C++ 平台搭建. C 与系统联系过于紧密, 各个系统,
各个环境都不一样, 在平台上我们将花费很多的时间. 另外 C/C++ 学习难度要比 Python
高不少.


目录
====

.. toctree::
  :maxdepth: 1

  intro.rst
  install.rst
  01_hello.rst
  02_hello_ttf.rst
  99_pysdl2_c.rst
  copyright.rst
  faq.rst
  news.rst


索引
====

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


构建日期: |today|


.. _PySDL2: https://bitbucket.org/marcusva/py-sdl2
.. _SDL: https://www.libsdl.org/
.. _Python: https://www.python.org/
.. _`Public Domain`: https://zh.wikipedia.org/wiki/%E5%85%AC%E6%9C%89%E9%A2%86%E5%9F%9F
.. _`LGPL 2.1`: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
.. _zlib: http://zlib.net/
