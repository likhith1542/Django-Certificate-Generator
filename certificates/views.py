from django.shortcuts import render

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse, FileResponse, Http404
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from django.template import Template, Context
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import pandas as pd
from termcolor import colored
from tqdm import tqdm_gui, tqdm
import os
from datetime import datetime
import shutil
import xlrd
from PIL import Image
import mmap

@login_required
def dashboard(request):
    email=request.user.email
    context = {}
    pEmail = email.lower()
    file = pd.read_csv('https://raw.githubusercontent.com/likhith1542/testcsv/main/event.csv')
    namet = ''
    b=False
    for emails in tqdm(file['Email']):
        if(pEmail == (emails.lower())):
            b=True
    if(b==True):
        return render(request,'account/dashboard.html',{'section':'dashboard'})
    else:
        return render(request,'account/dashboard1.html',{'section':'dashboard'})

@login_required
def dashboard1(request):
    email=request.user.email
    context = {}
    pEmail = email.lower()
    file = pd.read_csv('https://raw.githubusercontent.com/likhith1542/testcsv/main/event.csv')
    uniName = "Vellore Institute Of Technology,Andhra Pradesh"
    uniAcronym = "VIT-AP"
    eventName = 'CSI'
    leadName = "Muhammad Hamza"

    currentDate = datetime.date(datetime.now())
    fname = 'certificate/'
    if os.path.exists(fname):
        shutil.rmtree(fname)
    os.mkdir(fname)
    namet = ''

    # Getting 'Name' columns from 'file'
    i = 0
    nameslist = []
    for names in tqdm(file['Name']):
        nameslist.append(names)
    for emails in tqdm(file['Email']):
        i = i+1
        if(pEmail == (emails.lower())):
            image = Image.new('RGB', (1920, 1080), (255, 255, 255))
            
            colordev = 'rgb(128, 128, 128)'
            colorcert = 'rgb(89, 89, 89)'
            colorname = 'rgb(77, 148, 255)'
            colorNameDSCLead = 'rgb(229, 57, 53)'
            
            participation_message = f"is hereby awarded this Certificate of Participation on successfully attending \n{eventName} at {uniName} organized by\nCSI {uniAcronym}."

            draw = ImageDraw.Draw(image)
            
            with open('certificates/static/arial.ttf', 'rb') as f:
                m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) #File is open read-only
                draw.text((950, 300), eventName + ' Participant',font=ImageFont.truetype(m, 32),fill=colordev)
            
            with open('certificates/static/arial.ttf', 'rb') as f:
                m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) #File is open read-only
                draw.text((950, 920), 'Signing Authority', font=ImageFont.truetype(m, size=22), fill='rgb(128,128,128)')

            with open('certificates/static/arial.ttf', 'rb') as f:
                m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) #File is open read-only
                draw.text((950, 500), participation_message, font=ImageFont.truetype(m, size=25),fill='rgb(102, 102, 102)')

            with open('certificates/static/arial.ttf', 'rb') as f:
                m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) #File is open read-only
                draw.text((1040, 143), 'Computer Society Of India Club',font=ImageFont.truetype(m, size=35), fill=colordev)

            with open('certificates/static/arial.ttf', 'rb') as f:
                m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) #File is open read-only
                draw.text((1640, 950), 'Certificate ID:', font=ImageFont.truetype(m, size=20), fill=colorcert)

            with open('certificates/static/arial.ttf', 'rb') as f:
                m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) #File is open read-only
                draw.text((1640, 980), f'Issue Date: {currentDate}', font=ImageFont.truetype(m, size=20), fill=colorcert)
            
            
            with open('certificates/static/Almondita.ttf', 'rb') as f:
                m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) #File is open read-only
                draw.text((960, 650), leadName, font=ImageFont.truetype(m, 150),fill=colorNameDSCLead)

                
                      
            with open('certificates/static/arialbd.ttf', 'rb') as f:
                m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) #File is open read-only
                draw.text((950, 400), nameslist[i-1],font=ImageFont.truetype(m, 55),fill=colorname)
                
            with open('certificates/static/arialbd.ttf', 'rb') as f:
                m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) #File is open read-only
                draw.text((950, 820), f'Computer Society Of India Club, {uniAcronym} Lead',font=ImageFont.truetype(m, size=22), fill=colorcert)

            with open('certificates/static/arialbd.ttf', 'rb') as f:
                m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) #File is open read-only
                draw.text((950, 960), 'CSI ' + uniAcronym + ' Lead', font=ImageFont.truetype(m, size=25),fill='rgb(128,128,128)')

            with open('certificates/static/arialbd.ttf', 'rb') as f:
                m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) #File is open read-only
                draw.text((950, 200), 'Certificate of Participation',font=ImageFont.truetype(m, size=55), fill=colorcert)
                
                
                
                      
                      
            with open('certificates/static/arial_italic.ttf', 'rb') as f:
                m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) #File is open read-only
                draw.text((1640, 1020), '#Computer Society Of India Club', font=ImageFont.truetype(m, size=18),fill='rgb(211, 47, 47)')
            

            # colors for various writings
            

            # DSC logo
            dsc_logo = Image.open('certificates/static/logo.jpg')
            # Resizing the DSC Logo
            dsc_logo = dsc_logo.resize((75, 75))

            # Left Side style Image
            side_style = Image.open('certificates/static/leftSide.png')

            # Putting Logo & Left style Image
            image.paste(dsc_logo, (950, 125))
            image.paste(side_style, (0, 0))


            draw.line((950, 800, 1520, 800),
                      fill='rgb(128, 128, 128)', width=3)

            image.save('certificate/' + nameslist[i-1] + '.png')
            namet = 'certificate/' + nameslist[i-1] + '.png'

    try:
        return FileResponse(open(namet, 'rb'), content_type='application/png')
    except FileNotFoundError:
        return HttpResponse('Your participation was not available')
