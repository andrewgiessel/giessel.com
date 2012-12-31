This is the github repository for giessel.com.

The site is built using [Flask](http://flask.pocoo.org) for the backend, and [Twitter Bootstrap](twitter.github.com/bootstrap/) for the front-end (+ a lot of custom work).  The main three directories are as follows:

* static
  Contains all resources for the site- images, css, and js.

* templates
  Contains a series of [jinja2]() templates for the site.  The essential structure is that base.html has a block that is replaced by each of the sub-pages as needed.

* blog
  A directory containing the markdown files that are the content of the blog posts.  Inside of blog, there is a subdirectory for each year, and inside of that, simply named markdown files with YAML front-matter.  This directory and these files are parsed to generate the blog.

The final component is __init__.py - the single python file that uses Flask to power the site.  The file consists of 8 functions, 2 of which are for parsing the blog directory and individual files, and 6 to do the routing for the Flask application itself.  The main index page is by default the most recent blog post, and as such is very redudent with individual blog post pages.  The rest of the routing functions ( about_index(), research_index(), contact_index() )simply render relatively static templates.

That's basically it!  I wrote the blog engine in the winter of 2011 and finally found a designer, [Mike Stone](https://github.com/himikestone), to help me with the front end.  Feel free to fork this site, play around with it, or even use it to build your own blog.  The entire site is licensed under the [Creative Commons Attributuion License](http://http://creativecommons.org/licenses/by/3.0/), meaning you can do whatever you like with anything, just give me credit.

Pull requests welcome!