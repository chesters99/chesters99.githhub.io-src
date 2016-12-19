Title: Installing Theano with GPU support on Windows 10 / Python 3.5
Date: 2016-12-19
Category: Data Science
Tags: Python, Data Science
Slug: install-theano-on-windows10
Authors: Graham Chester
Summary: How to install Theano Python Neural Network package on Windows 10 with Python 3.5

Installing Theano on windows ***without*** GPU support is just about as simple as:
```bash
pip install theano 
# or go to gihub to get the bleeding edge version and then:
pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git
```
<br>
However installing with GPU support on Windows 10 can be a nightmare mainly due to Windows not providing a C compiler as standard. For me it took a very frustrating whole day to get it all working. I found that existing tutorials didnt cover many of the issues I faced and it seems there a small differences in Windows systems that result in what works for one person, doesnt work for others. Unless you're a Windows C developer it's probably going to be painful, but hopefully these steps save you a lot of messing around!
<hr><br>

####1) Install Anaconda, or python 3.5 with numpy, scipy etc
Install Anaconda with Python 3.5 from https://www.continuum.io/downloads

You may be able to install Python 3.5 and Theanos various dependencies using pip, but Anaconda makes the process a whole lot easier. Hopefully one day they will package Theano as well to reduce pain for Windows users in particular.
<br><br>

####2) Install CUDA 7.5 
Download and install from https://developer.nvidia.com/cuda-75-downloads-archive

The latest version, CUDA 8.0, might work but I havent tried it - with all the effort to get GPU support working I've been reluctant to fiddle too much...
<br><br>

####3) Install Microsoft Visual Studio 2013 
Download and install (with no extras) from:
https://www.microsoft.com/en-gb/download/details.aspx?id=44921
<br><br>

####4) Install Windows 10 SDK
Download this to get required include and lib files from:
https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk
<br><br>

####5) Customise nvcc.profile
Modify CUDA complier config file to add INCLUDES and LIBRARIES paths
```
TOP              = $(_HERE_)/..

NVVMIR_LIBRARY_DIR = $(TOP)/nvvm/libdevice

PATH            += $(TOP)/open64/bin;$(TOP)/nvvm/bin;$(_HERE_);$(TOP)/lib;

INCLUDES += "-I/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v7.5/include" "-I/Program Files (x86)/Microsoft Visual Studio 12.0/VC/include" "-I/Program Files (x86)/Windows Kits/10/Include/10.0.14393.0/shared" "-I/Program Files (x86)/Windows Kits/10/Include/10.0.14393.0/um" $(_SPACE_)

LIBRARIES        =+ $(_SPACE_) "/LIBPATH:$(TOP)/lib/$(_WIN_PLATFORM_)" "/LIBPATH:/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64" "/LIBPATH:/Program Files (x86)/Windows Kits/10/lib/10.0.14393.0/um/x64" "/LIBPATH:/Program Filesr/Anaconda/libs"


CUDAFE_FLAGS    +=
PTXAS_FLAGS     +=
```
<br><br>

####6) Modify .theanorc config file
with flags, compiler_bindir and cxxflags set to resole issues with the default config. Experiment with cnmem setting for your graphics card to use as much graphics card memory as possible without hitting memory errors.
```ini
[global]
floatX = float32
device = gpu

[nvcc]
fastmath = True
flags=--cl-version=2013
compiler_bindir=C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\amd64

[lib]
cnmem = 0.80

[gcc]
cxxflags = -D_hypot=hypot
```
<br><br>

####7) Install theano dependencies
```bash
pip install mingw libpython numpy
```
<br><br>

####8) Download pycuda
Download pre-complied wheel file from this site to avoid having to compile on Windows 10
from http://www.lfd.uci.edu/~gohlke/pythonlibs/#pycuda
```bash
pip install ~/Downloads/"pycuda-2016.1.2+cuda7518-cp35-cp35m-win_amd64.whl"
```
<br><br>

####9) Generate libpython35 and install
make temp directory, copy python35.dll to temp directory and do the following
```bash
gendef python35.dll
dlltool --as-flags=--64 -m i386:x86-64 -k --output-lib libpython35.a --input-def python35.def
copy libpython35 and python35 to Anaconda/libs
```
<br><br>

####10) Create and run theano test script
This will generate CUDA code and run a test. Save script as theanotest.py 
```python
from theano import function, config, shared, sandbox
import theano.tensor as T
import numpy
import time

vlen = 10 * 30 * 768  # 10 x #cores x # threads per core
iters = 1000

rng = numpy.random.RandomState(22)
x = shared(numpy.asarray(rng.rand(vlen), config.floatX))
f = function([], T.exp(x))
print(f.maker.fgraph.toposort())
t0 = time.time()
for i in range(iters):
    r = f()
    t1 = time.time()
    print("Looping %d times took %f seconds" % (iters, t1 - t0))
    print("First 5 results are %s" % (r[:5]))
    if numpy.any([isinstance(x.op, T.Elemwise) for x in f.maker.fgraph.toposort()]):
        print('Used the cpu')
	else:
	    print('Used the gpu')
```
and then: 
```bash
python -m theanotest 
```
<br>

####11) Create and run pycuda test script
Save the following script as pycudatest.py
```python
import pycuda.autoinit
import pycuda.driver as drv
import numpy

from pycuda.compiler import SourceModule
mod = SourceModule("""
__global__ void multiply_them(float *dest, float *a, float *b)
{
    const int i = threadIdx.x;
            dest[i] = a[i] * b[i];
	    }
	    """)

	    multiply_them = mod.get_function("multiply_them")

	    a = numpy.random.randn(400).astype(numpy.float32)
	    b = numpy.random.randn(400).astype(numpy.float32)

	    dest = numpy.zeros_like(a)
	    multiply_them(
	        drv.Out(dest), drv.In(a), drv.In(b),
		    block=(400,1,1), grid=(1,1))

		    print (dest-a*b)
```
and then:
```bash
python -m pycudatest
```
<br>

####12) Final check
At Python REPL prompt type:
```python
import theano
```
You should get a response similar to:

`Using gpu device 0: GeForce GTX 970 (CNMeM is enabled with initial size: 75.0% of memory, cuDNN not available)`{: .red}

**And if you get this response, you're done. Nice job!**


