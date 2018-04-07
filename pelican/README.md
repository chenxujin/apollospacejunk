# Apollo Space Junk Bot Flock - Web Page

This folder contains the source code for the Apollo Space Junk bot flock web page.

This page uses Pelican to generate static content. 

To install Pelican:

```
pip install Markdown
pip install pelican
```

## Instructions: Creating/Modifying Site Content

To create or modify site contents, check out the `master` branch of the apollospacejunk repository on Github.

The `pelican/` directory in the top level of this branch will contain all of the website content, blog posts,
and other materials used to construct the website.

To create new blog posts or modify the existing contents of the site, you can create or modify markdown files.

## Instructions: Updating Site

Once you have finished adding or modifying site contents, you will use Pelican to rebuild the site.

You will need to install the `coffin-spore-theme`, a custom pelican theme I wrote for these bots.

```
git clone https://github.com/charlesreid1/coffin-spore-theme
pelican-themes -i coffin-spore-theme
```

Now go to the `pelican/` directory in the Apollo Space Junk repository. 

When you run Pelican to generate site contents, it will put the static site into a directory called `output/`. 

If you check out a copy of the `gh-pages` brnach of Apollo Space Junk, and call it `output/`, it will check out 
a copy of the site's static content. If you then run Pelican to update the site's static content, it will 
update the content in-place, and you can update the static contents in Github directly from there.

In the pelicanconf.py file, you can use the SITEURL variable to set the site prefix. 

If you are building the site to test locally, use SITEURL = ''

Then go to the `output/` directory and run a simple HTTP server: `python -m SimpleHTTPServer 8080`

If you are building the site to deploy to Github Pages, use SITEURL = '/apollospacejunk'

Then go to the `output/` directory and update the gh-pages branch of the Apollo Space Junk repository.
