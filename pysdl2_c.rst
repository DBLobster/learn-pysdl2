pysdl2 与 C
===========

说明
----

``pysdl2`` 是 SDL2 的一个 ``ctypes`` wrapper, 纯 Python 代码. 使用 ``pysdl2``
可以免去配置 C 语言环境, 免去编译, 免去配置 lib 和编写 Makefile.

pysdl2 把 SDL2 进行了完整封装, 使用起来与 C/C++ 调用 SDL2 差别并不大,
具体可以看下面的两个例子.

注意字符串, 送给 SDL2 的时候, 需要用 ``bytes("srt", 'utf-8')`` 转换成 UTF-8;
使用 SDL2 送过来的 bytes, 需要进行 ``decode``, ``object.decode('utf-8'))``; C 的
NULL, 在 Python 中是 None.

缺点: 不是很适合移动环境, 虽然原则上是可以.
不过移动环境的产品级构建本身也比较复杂.


两个例子
--------

1. 来自 pysdl2 文档: PySDL2Link_

2. 修改的来自 SDL Wiki 的一段例子: SDL2WiKiLink_

.. code:: python

    # https://wiki.libsdl.org/SDL_CreateWindow

    # Example program:
    # Using SDL2 to create an application window

    import sys
    from sdl2 import *

    def run():

        SDL_Init(SDL_INIT_VIDEO)              # Initialize SDL2

        # Create an application window with the following settings:
        window = SDL_CreateWindow(
            bytes("An SDL2 window", 'utf-8'),  # window title
            SDL_WINDOWPOS_UNDEFINED,           # initial x position
            SDL_WINDOWPOS_UNDEFINED,           # initial y position
            640,                               # width, in pixels
            480,                               # height, in pixels
            SDL_WINDOW_OPENGL                  # flags - see below
        )

        # Check that the window was successfully created
        if window == None:
            # In the case that the window could not be made...
            print("Could not create window: %s", SDL_GetError().decode('utf-8'))
            return 1

        # The window is open: could enter program loop here (see SDL_PollEvent())

        SDL_Delay(3000)  # Pause execution for 3000 milliseconds, for example

        # Close and destroy the window
        SDL_DestroyWindow(window)

        # Clean up
        SDL_Quit()
        return 0

    if __name__ == "__main__":
        sys.exit(run())


参考文档
--------

* https://pysdl2.readthedocs.io/en/latest/modules/sdl2.html
* https://wiki.libsdl.org/SDL_CreateWindow

.. _PySDL2Link: https://pysdl2.readthedocs.io/en/latest/modules/sdl2.html#usage
.. _SDL2WiKiLink: https://wiki.libsdl.org/SDL_CreateWindow
