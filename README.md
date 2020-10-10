# Django-Certificate-Generator
Certificate Generator developed using Django framework

# How this works?
* User will Log in using google sign in.
* This will extract email from the user information.
* This will check whether the email extracted presented in the excel sheet provided.
* If yes show options for Downoad Certificate and Logout.

# Installation of required packages
* Django `pip install django`
* social_django `pip install social-auth-app-django`
* prebase `pip install Pyrebase`
* matplotlib `pip install matplotlib`
* termcolor `pip install termcolor`
* tqdm `pip install tqdm`
* PIL/Pillow `pip install Pillow`
* pandas `pip install pandas`
* xlrd `pip install xlrd`
* django-extensions `pip install django-extensions`

# Pyrebase Installation Error Solution
Some Errors may be thrown while installing pyrebase. I have tested this in linux,ubuntu and windows archs. Linux and Ubuntu may/maynot have this issue. Windows had this issue. This can be solved
* Open git bash anywhere/terminal/cmd with git access
* Clone this repository to your system `git clone https://github.com/thisbejim/Pyrebase.git`
* Open the folder you just cloned and run the following command: `git fetch origin pull/249/head:upgrade-google-auth`
* `git checkout upgrade-google-auth`
* `python setup.py install --user`

# Errors using ImageFont.truetype()
Here we used `ImageFont.truetype()`.They won't be problem using `ImageFont.truetype()` in localhost/during developing stage.But during deploying there may be error using ImageFont.

The Error will be an OS(Resource) error.

**Why this issue rises?**

https://pillow.readthedocs.io/en/stable/reference/ImageFont.html#PIL.ImageFont.truetype

Load a TrueType or OpenType font from a file or file-like object, and create a font object. This function loads a font object from the given file or file-like object, and creates a font object for a font of the given size.

Pillow uses FreeType to open font files. If you are opening many fonts simultaneously on Windows, be aware that Windows limits the number of files that can be open in C at once to 512. If you approach that limit, an OSError may be thrown, reporting that FreeType “cannot open resource”.

**Solving the Issue**

We will try to save the font data to memory for every time we access them.

Ex:

```
with open('certificates/static/arial.ttf', 'rb') as f:
                m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
                draw.text((950, 920), 'Signing Authority', font=ImageFont.truetype(m, size=22), fill='rgb(128,128,128)')
```
