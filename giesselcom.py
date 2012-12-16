import markdown
from flask import Flask
from flask import render_template
from flask import Markup

import itertools
import yaml
import glob
import string
import os

application = Flask(__name__)
application.debug=True

# templates

# directories
#    templates/
#      page.html
#      post.html
#      research.html
#      404.html
#    blog/
#       year/
#          post-name-like-this/
#            post.md
#               title
#               slug
#               published (date | None)
#               blank line
#               md body
#             content/
#               pictures, pde files, etc.

@application.route('/')
def index():
    # post = most recent blog post
    #return     return render_template('index.html', post=post)
    return render_template('index.html')#, title=': index')

@application.route('/about/')
def about_index():
    return render_template('about.html')

@application.route('/research/')
def research_index():
    return render_template('research.html')

@application.route('/contact/')
def contact_index():
    return render_template('contact.html')


@application.route('/blog/')
def blog_index():

    # list of all years
    years = os.walk('./blog').next()[1]
    
    # build dictionary of lists
    # keys: years
    # values: post data, sorted by date
    blog_data = {}

    for year in years:
        post_dirs = os.walk(os.path.join('./blog', year)).next()[1]
        
        post_data = [parse_post_file(os.path.join('./blog', year, post, 'index.md')) for post in post_dirs]
        post_data = sorted(post_data, key=lambda post: post['published'])[::-1]   

        blog_data[year] = post_data

    return render_template('blog.html', blog_data=blog_data, years=years[::-1])

@application.route('/blog/<postname>')
def blog_post(postname=None):
    blog_dir = './gcom/blog'
    #    blog_dir = './blog'
    dirs = [name for name in os.listdir(blog_dir) if os.path.isdir(os.path.join(blog_dir, name))]
    for dir in dirs:
        index_file = os.path.join(blog_dir, name, postname, 'index.md')
        if os.path.isfile(index_file):
            post = parse_post_file(index_file)
            return render_template('post.html', post=post)

    # if we didn't find the post, throw a 404
    return render_template('404.html'), 404

def parse_post_file(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()

    post = {}

    # Read lines until an empty line is encountered, then build a dictionary with yaml
    
    # code jacked from flask-flatpages
    lines = iter(lines)
    meta = u'\n'.join(itertools.takewhile(string.strip, lines))
    post = yaml.safe_load(meta)

    # The rest is the content. `lines` is an iterator so it continues
    # where `itertools.takewhile` left it.
    post['filename'] = filename
    post['dirname'] = os.path.dirname(filename).split('/')[-1]
    post['body'] = u'\n'.join(lines)
    post['body'] = Markup(markdown.markdown(post['body']))

    return post

if __name__ == '__main__':
    application.run()
