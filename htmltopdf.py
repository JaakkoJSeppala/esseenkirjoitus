import pdfkit
import sys
import fileinput
import os
from pdf2image import convert_from_path
from PIL import Image
import subprocess

leftmargin= '30mm'
rightmargin = '30mm'
topmargin = '25mm'
bottommargin = '25mm'

kurssikoodi = 'KTKP010'
kurssinimi = 'Oppiminen ja ohjaus'

replacements={}
replacements.update({'ä':'&auml;'})
replacements.update({'Ä':'&Auml;'})
replacements.update({'ö':'&ouml;'})
replacements.update({'Ö':'&ouml;'})
replacements.update({'kurssikoodi':kurssikoodi})
replacements.update({'kurssinimi':kurssinimi})

with open('koe.html') as infile, open('uusi.html', 'w') as outfile:
    for line in infile:
        for src, target in replacements.items():
            line = line.replace(src, target)
        outfile.write(line)

command = f'wkhtmltopdf -L {leftmargin} -R {rightmargin} -T {topmargin} -B {bottommargin} uusi.html ./test.pdf'
pro = subprocess.Popen(command,shell=True, preexec_fn=os.setsid)
os.killpg(os.getpgid(pro.pid), signal.SIGTERM)  