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
#               published (date | None)
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
    # get sorted list of years (newest first) and dictionary of all blog data
    years, blog_data = parse_blog_directory()

    most_recent_year = years[0]
    most_recent_post = blog_data[most_recent_year][0]
    
    # render the most recent post
    return render_template('blog_post.html', post=most_recent_post)

@application.route('/blog/')
def blog_index():
    # get sorted list of years (newest first) and dictionary of all blog data

    years, blog_data = parse_blog_directory()
    return render_template('blog.html', blog_data=blog_data, years=years)

@application.route('/blog/<postname>')
def blog_post(postname=None):
    years, blog_data = parse_blog_directory()
    for year in years:
        posts = blog_data[year]
        for post in posts:
            if post['url'] == postname:
                return render_template('blog_post.html', post=post, change_title=True)

    # if we didn't find the post, throw a 404
    return render_template('404.html'), 404

def parse_blog_directory():
    all_years = os.walk('./blog').next()[1]
    
    # build dictionary of lists
    # year: [sorted post data]
    blog_data = {}

    for year in all_years:
        post_data = [parse_post_file(md_file) for md_file in glob.glob('./blog/' + year + '/*.md')]
        sorted_post_data = sorted(post_data, key=lambda post: post['published'])[::-1]

        # remove any post where "published" is False (aka a draft)
        sorted_post_data = [post for post in sorted_post_data if post['published']]

        if sorted_post_data:
            blog_data[year] = sorted_post_data

    # can get this from the reverse sorted keys of the blog_data dict
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
