Title: Setting up a GitHub Pages blog with Pelican - Part 2 
Date: 2016-10-20
Category: Getting Started
Tags: Python, Pelican
Slug: pelican-github-blog-finesse
Authors: Graham Chester 
Summary: How to setup a blog on GitHub with Pelican - Part 2

##Finessing the Blog 

So your blog looks good but your a perfectionist, so there's a few more things you can do to make it  a little more 'professional'


###Setup a nice 404 page 
You may like to show a more friendly and personalised 404 page. Pelican can generate one for you from a markdown file something like the example below. Note that this page should go in the ghpages/content/pages directory - if you put it in ghpages/content it will be interpreted by pelican as a blog article.
```
$ cat content/pages/404.md
Title: Sorry, cant find that page!
save_as: 404.html
status: hidden

<br><br>
####The page you requested cant be found on this site.
<br><br>
####Please click ***[here](http://blog.xxxxxxxx.com)*** to return
```

###Setup for Google indexing

You may also like to setup a robots.txt file specifying a sitemap file (configured in pelicanconf.py above) to make it easier for the google bots to index your site. Also you can set a favicon and include any custom css - all held in the static directory in pelicanconf.py

```
$ cat robots.txt
User-Agent: *
Disallow:
Sitemap: http://blog.xxxxxxxx.com/sitemap.xml
```

###Setup for Google Analytics

If you'd like to see stats on your website you can register for a google analytics id and specify it in your publishconf.py file as listed in the previous blog.

###Setting up a custom domain

While it's fine to host your blog at http://yourusername.github.io perhaps you would like to use your domain name, for example http://blog.yourdomain.com. To do this requires:

1) Setup a CNAME alias with your domain name provider that points blog.yourdomain.com to http://yourusername.github.io

2) Provide a file called CNAME file in the root directory of your repository to let GitHub know you are using a custom domain. Create a file CNAME with one line:

```
$ cat content/static/CNAME
blog.yourdomain.com
```

Add a line to *EXTRA_PATHS_METADATA* in pelicanconf.py to tell pelican to include the CNAME file without any processing - along with other static content.

```python
EXTRA_  PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'},
    'static/custom.css': {'path': 'custom.css'},
    'static/CNAME': {'path': 'CNAME'},
}
```

Then Add, Commit, and Push to GitHub as per the Deployment section in the previous article.

###You're Done!

Hopefully these two posts were helpful in setting up a great looking blog for not too much effort. 

Comments, suggestions, improvements more than welcome

