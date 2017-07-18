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
# directories

#    static/
#      js/
#      css/
#      img/
#    templates/
#      blog.html
#      blog_post.html
#      research.html
#      about.html
#      contact.html
#      404.html
#    blog/
#       year/
#          post-name-like-this.md
#               title
#               published (date | False)
#               blank line
#               md body

@application.route('/about/')
def about_index():
    return render_template('about.html')

@application.route('/research/')
def research_index():
    return render_template('research.html')

@application.route('/contact/')
def contact_index():
    return render_template('contact.html')

@application.route('/')
def index():
    return render_template('research.html')

@application.route('/blog/')
def blog_index():
    # get sorted list of years (newest first) and dictionary of all blog data
    years, blog_data = parse_blog_directory()

    return render_template('blog.html', blog_data=blog_data, years=years)

@application.route('/blog/<postname>')
def blog_post(postname=None):
    years, blog_data = parse_blog_directory(drafts_ok = True)

    for year in years:
        posts = blog_data[year]
        for post in posts:
            if post['url'] == postname:
                return render_template('blog_post.html', post=post, change_title=True, show_comments=True)

    # if we didn't find the post, throw a 404
    return render_template('404.html'), 404

def parse_blog_directory(drafts_ok = False):
    blog_dir = './giessel.com/blog/'

    all_years = os.walk(blog_dir).next()[1]

    # build dictionary of lists
    # year: [sorted post data]
    blog_data = {}

    for year in all_years:
        post_data = [parse_post_file(md_file) for md_file in glob.glob(blog_dir + year + '/*.md')]

        # remove any post where "published" is False (aka a draft)
        # and then sort
        if not drafts_ok:
            post_data = [post for post in post_data if post['published']]
            post_data = sorted(post_data, key=lambda post: post['published'])[::-1]
            
        if post_data:
            blog_data[year] = post_data

    # can get valid sorted years from the reverse sorted keys of the blog_data dict
    valid_years = sorted(blog_data)[::-1]
    
    return valid_years, blog_data

def parse_post_file(filename):
    lines = open(filename).readlines()
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

    post['filename'] = filename
    post['url'] = os.path.basename(filename).split('.')[0]
    return post

if __name__ == '__main__':
    application.run()


