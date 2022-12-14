import pdfkit
import sys
import fileinput
import os
from pdf2image import convert_from_path
from PIL import Image
import subprocess

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

command = 'wkhtmltopdf -L 30mm -R 30mm -T 25mm -B 25mm uusi.html ./test.pdf'
subprocess.Popen(command,shell=True)