import pdfkit
import sys
import fileinput
import os

kurssikoodi = 'KTKP010'
kurssinimi = 'Oppiminen ja ohjaus'

replacements = {'ä':'&auml;', 'Ä':'&Auml;', 'Ö':'&ouml;', 'ö':'&ouml;', 'kurssikoodi':kurssikoodi, 'kurssinimi':kurssinimi}

with open('koe.html') as infile, open('uusi.html', 'w') as outfile:
    for line in infile:
        for src, target in replacements.items():
            line = line.replace(src, target)
        outfile.write(line)

pdfkit.from_url('uusi.html','essee.pdf')
