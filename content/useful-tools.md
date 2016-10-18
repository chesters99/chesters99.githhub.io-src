Title: Getting Started - Python Environment 
Date: 2016-10-17
Category: Getting Started
Tags: Python, Getting Started 
Slug: useful-tools
Authors: Graham Chester 
Summary: Attempted Summary of the Python Ecosystem

###Python 
There are a number of Python run-times (interpreters and compilers) available. The one most used is called ***CPython*** (because it is written in C). It is installed by default on Linux and Macs, and can be installed on Windows (see below for Windows).

Unfortuantely there are two versions of Python (2 and 3). Python 3 was released as a replacement for Python 2 but due to the need to make some substantial improvements, they are not particularly compatible. Sure with a bit of effort you can write code that will run on both, but few developers seem to to that.  There is a very large code base on Python 2 which would require an enormous effort to migrate to 3, and yet 2 is planned to be de-supported by 2020.... is there an elephant in the room?  The latest release of Python 2 is Python 2.7 - there will be no more Python 2 releases apparently. As of the date of this blog, the latest release of Python 3 is Python 3.5 with Python 3.6 due soon.

There are a number of other Python run-times available such as:

***Numba*** - JIT (just in time) compiler offering massive speed improvements compared to CPython. Generally should be used to speed up problem code only, rather than be applied universally

***Cython*** - Python compiler with additional syntax to declare variable types. Compiles to C code, then to machine code. Also offers masive speed improvements compared to CPython - at the expense of compatible syntax. Generally should be used to speed up problem code only, rather than be applied universally. 

***Jython*** - Python interpreter that generates Java byte code to run on the Java virtual machine

***Iron Python*** - Python intepreter that runs on the Microsoft C# platform

Confused? Unless you have a very specific environment or a major performance issue, just use Python 3 (Cpython) if you can, or Python 2 (CPython) if you must.
<br><br>

###Python Editors/IDEs
There are a number of Python Editors/IDEs (Integrated Development Environments) available. Editors purely edit the code usually with some syntax checking, whereas IDE's provide a workbench covering debugging, database manipulation, command line access, etc etc.

Popular editors include Vim or Emacs (not that easy to learn. often used by those with a Linux/Unix background). Notepad++ for Windows or Sublime Text for Mac.

IDE include PyCharm (my favourite, but not cheap), and Spyder (Free). An IDE can be a lot to learn initially as there is so much going on on the screen, but once used to it they are my recommended option (see Books I recommend blog post for 'Mastering PyCharm'. 

But many people prefer a simpler setup using a sophisticated editor such as Sublime Text.
<br><br>

###Operating Systems
***Windows -*** has been something of a neglected platform in the Python world as 'serious' developers use Linux or Mac..... but I think it hasnt been a great idea to alienate used of the most popular OS by far. Anyway life is much better now for Windows users with the release of Anaconda by Continuum Analytics. It's a free download and I would suggest dont even think of any another approach if you ar a Windows user. Note though it does come with a LOT of packages pre-installed! Note also that some Python packages require a C compiler to install and Windows does not come with one pre-installed. Consider mingw for something lightweight, or Visual Studio for the gorilla approach.

***Mac OS -*** is well supported and in fact comes with Python 2 pre-installed. I suggest you install Homebrew, and then Python 3, or if you plan to do some data analysis/science then Anaconda is your friend. Personally I find the Mac provides the best combination of user-friendly GUI, and a unix-like system under the hood to support development.

***Linux -*** comes in many flavours, though Linux Mint and Ubuntu seem to be the leaders. Personally I found I needed a lot of Linux knowledge to figure out how to fix things when they went wrong. While Linux has made great strides in user-friendliness in recent years, due to past struggles I prefer to see it in the server-space rather than the desktop (personal opinion only!)
<br><br>

###Development Utilities
***Unittest or Pytest-*** for testing. Write tests as you go and run them frequently. It's painful and wastes time to let your code get to far ahead of your test scripts. 

TBC.......
