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
#application.debug=True

# templates

# page.html
#   header
#   body
#   footer

# post.html
#   inherits from page
#   body = post stuff

# research.html
#   inherits from page
#   body = research.md
#        + publication listing
#        + listing of project posts

# blog
#    inherits from page
#    body = listing of blog posts

# bio
#    post.html w/bio.md

# directories
#    bio.md
#    static/
#      css stuff
#      non-post related images, other files
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
#    research/
#        project-name-like-this/
#            project.md
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
    return render_template('index.html', title=': index')

@application.route('/bio')
def bio_index():
    # build biodata from bio.md
    #return     return render_template('post.html', post=bio)
    return 'all about me'

@application.route('/blog/')
def blog_index():
    current_dir = './gcom/blog'
    #    current_dir = './blog'
    dirs = [name for name in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, name))]
    return dirs.__str__()
    files = glob.glob('blog/*.md')
    blog_files = [parse_post_file(file) for file in files]

    # return render of blog.html w/blogs = nested dir of years, and posts.  Date : Title - optional summary
    # filter by 'Published'
    return render_template('index.html', post=blog_files[0])
    return 'lots of blogs, so many blogs.'

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

@application.route('/research/')
def research_index():
    #return render of research.html w/front matter from research.md, publications a dict from pubmed, and list of project dirs w/titles, slugs.
    return 'lots of projects, so many projects.'

@application.route('/research/<projectname>')
def research_post(projectname=None):
    research_dir = './gcom/research'
    post = None
    index_file = os.path.join(research_dir, projectname, 'index.md')
    if os.path.isfile(index_file):
        post = parse_post_file(index_file)
        return render_template('post.html', post=post)
    else:
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
    post['body'] = u'\n'.join(lines)
    post['body'] = Markup(markdown.markdown(post['body']))

    return post

if __name__ == '__main__':
    application.run()
