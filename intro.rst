前言
====
前面我们已经简单的介绍了 PySDL2_, SDL_, Python_. 关于这些软件的详细信息,
还请自行翻阅对应的文章与网站.

本文讲解如何使用 PySDL2_ 来快速的制作游戏. 不过, 与其说是制作游戏,
不如说是讲解游戏制作的各个要素.

本文的目标对象是使用 Python_ 人群, 想做些能展示的, 很酷的东西,
而且不需要很多计算机知识.

本文假定你有一些 Python_ 的使用经验.

本文尽可能的通过简单的语言来表达不涉及专业知识的方法, 并给出进一步学习的链接,
所以不要指望本文面面俱到的给你讲解一个 3 维坐标变换使用矩阵求解的原理.

其实游戏制作者扮演的是一个上帝的角色, 是这个游戏的上帝. 游戏里有什么规则,
游戏里有什么人, 什么时间发生了什么事情, 都由制造者来创造,
所以游戏制作涉及的知识会比较广: 数学的, 物理的, 颜色的, 计算机的等等.
进一步来说, 做一个好游戏难度真的是非常之大的.

如果你碰到有些概念不明白, 有可能是你的年纪还不够, 没学到这些知识;
另一种可能就是都还给老师了, ^_^

`注解` 部分可能需要更多的知识来理解. 不过正文部分尽可能不涉及 `注解` 的知识,
通常情况下你可以忽略 `注解` 部分.

PySDL2_ 对于本人也是边学边用, 如果本文有任何疏漏和错误, 欢迎指正, 谢谢.

.. note::

  本文使用 reStructuredText_ 编写, 代码托管在 https://github.com/DBLobster/learn-pysdl2 .
  本文有任何疏漏和错误请在此反馈, 对本文有任何意见同样请在此反馈.

.. note::

  如果你了解一部分 C/C++ 那就更好了. PySDL2 封装的不错, 并且扩展库做的也挺漂亮,
  但是毕竟 SDL 是用 C 写的, 在调试和高级应用上, 还是有 C 的基础更加得心应手.

  如果你数学精通, 了解平面直角坐标系, 向量计算, 矩阵乘法等,
  那么对于 2D/3D 游戏来说是更加方便.

  如果你了解三原色, 加色, 减色, PhotoShop 等, 那么图像部分可能会更加容易.

  如果你了解计算机的基础架构 (内存, 显存, 声卡, CPU, 硬盘, 文件, 文件夹等等),
  那么你应该知道, 本文代码具体都做了些什么.


.. _PySDL2: https://bitbucket.org/marcusva/py-sdl2
.. _SDL: https://www.libsdl.org/
.. _Python: https://www.python.org/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
