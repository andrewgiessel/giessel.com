title: Python for Neuroscientists - Overview
published: 2013-02-09

Every research project I've ever worked on has involved extensive programing (although this likely is a reflection of the way I like to approach science!).  Over the years, I've used Perl, C/C++, Fortran, DSLs, IgorPro, MATLAB, and Python all to various degrees for acquisition, analysis, processing, and visualization.  When I started work in my postdoc lab, there wasn't a culture of any particular language, and so I was in the interesting position to make a decision between several different options.  In our lab, we have choosen to primarily use the Python programming language as an alternative to MATLAB for several key reasons:

1. Python is a fantastic general purpose programming language, with comprehensive and well thought-out syntax and language features.  I much prefer to use a general programming language with good domain specific libaries than a domain specific langauge with awkward, legacy laden syntax.

2. Python is open source, and as such, free and cross-platform.  While I can easily get MATLAB via my university, I feel that using open source tools is in the general spirit of openness and scientific inquiry.

3. The libaries and packages for python are terrific.  Numpy + Scipy + Matplotlib are probably the core of what I use, but the IPython project and espescailly the IPython Noteboks are just amazing.  Reproducibility of analysis and sharing of results are extremely important and only becoming moreso.  The Ipython notebook system is an awesome way to facilitate this.  Other notable libraries include pymorph/mahotas and sklearn.

4. Python plays great with other languages - especially lower-level languages like C and Fortran.  The ability to mainly program in a high-level language like Python and call lower-level code for speed is huge for time-intensive operations.  Projects like numba are making this even easier.

-----

I am planning on working through the excellent "MATLAB for Neuroscientists" by Wallisch et al., and porting the topics and code to Python.  This is partially as an exercise for myself, but also to provide a resource for anyone out there who is interested in using Python for common tasks analyzing electrophysiological and two-photon imaging data. I am mostly using the text as a guide, and will add related information, topics and techniques if I deam them ipmortant.  In particular, I'm hoping to add a section on various machine learning techniques, but I'm not sure where it'll go exactly.

The text is broken into four parts: Fundamentals, Data Collection, Data Analysis, and Data Modeling.  I've decided to go lighter on the Fundamentals and skip the Data Collection sections.   I list below many great resourses for getting started and learning Python, and the Data Collection section is primarily focused on Psychophysics experiments, which lie outside of my field and interests.  I plan to write relatively long form posts (one per chapter) and have a lot of links to the appropriate libaries and functional Ipython notebooks.  

-----

Table Of Contents  (updated, edited, and subject to change as I go.  If you don't see a link- then I haven't gotten to it yet. Requests welcome ;) )


Part I - Fundamentals of Data Analysis with Python
--------------------------------------------------

* Basic Resources
* IPython Notebooks
* Numpy Guide
* Pandas
* Plotting
* Debugging and Profiling Python Code

Part II - Data Analysis with Python
-----------------------------------

* Frequency Analysis Part I: Fourier Decomposition
* Frequency Analysis Part I: Non-stational Signals and Spectrograms
* Wavelets
* Convolution
* Introduction to Phase Plane Analysis
* Exploring the Fitzhugh-Nagumo Model
* Neural Data Analysis: Encoding
* Principle Component Analysis
* Information Theory
* Neural Decoding Part I: Descrete Variables
* Neural Decoding Part II: Continous Variables

Part III - Data Modeling With MATLAB
------------------------------------

* Modeling Differential Equations in Python
* Voltage-Gated Ion Channels
* Models of a Single Neuron
* Models of the Retina
* Simplified Model of a Spiking Neuron
* Fitzhugh-Nagoumo Model: Traveling Waves
* Decision Theory
* Markov Models
* Modeling Spike Trains as a Poisson Process
* Synaptic Transmission
* Neural Networks Part I: Unsupervised Learning
* Neural Networks Part II: Supervised Learning


