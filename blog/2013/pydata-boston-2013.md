title: PyData Boston 2013
published: 2013-08-01

<center>
<img src="http://pydata.org/static/base/includes/images/pydatalogo-generic.png">
</center>

Last weekend I had the pleasure of attending and speaking at [PyData Boston](http://pydata.org/bos2013).  It was a great conference with a [wide range and variety of talks](http://pydata.org/bos2013/schedule/), all focusing on using Python for various sorts of data analysis, in many diverse fields.  There were talks about using Python for machine learning, text analysis, Bayesian statistics, energy analytics, and much more.  The talks were all captured on video and should be up online soon- I'll update this post when they are available.  Keynote talks were by Travis Oliphant and Cathy O'Neil - both touched on the need for sharing the analytical process and tools that facilitate that process.

I was happy to give not one, but two different talks at the conference.  The first was a tutorial on the python library NumPy- a core component of the Python stack for effeciently storing and manipulating array data.  All materials for the talk are on this [github repo](http://github.com/andrewgiessel/pydata_bos_2013_intro_to_numpy).  I did the whole presentation in an IPython notebook (a first for me).  If you want to take a look at the static version of the talk, it is [here](http://nbviewer.ipython.org/urls/raw.github.com/andrewgiessel/pydata_bos_2013_intro_to_numpy/master/Introduction%2520To%2520NumPy.ipynb).  I basically highlighted the parts of the NumPy API that I find most useful on a day-to-day basis.

On Sunday, I gave a second talk on various projects in [our lab](http://dattalab.org) and highlighted the similarities and differences between our data analysis needs for each project.  Like many new neuroscience labs, we have a real mix of projects going on- molecular, bioinformatics, in vivo imaging and even behavior!  These different types of projects all have unique constraints and use different tools, but we've found Python very flexible and it's our analysis language of choice.  Of note, I talked about how we're using a custom version of [MongoDB](http://mongodb.org) to store all our data.  MongoDB is a so-called 'schema-free' database, which means that as we change our experiments, we don't have to redesign our database.  This is a huge boost and helps us take advantage of a database system quickly and fluidly.

I had a really good time giving both presentations and had some great conversations all weekend long.  Thanks to everyone that make the conference happen- the planners, the speakers and the attendees!

Finally, I'll note that I haven't been posting here as much as I'd like.  Turns out having an infant takes a lot of time!  I'm hoping to have more frequent but shorter posts in the future.  We'll see how that goes.
