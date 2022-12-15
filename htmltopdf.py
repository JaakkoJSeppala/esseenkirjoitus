import signal
import os
import subprocess


def compile_document():
    pro = subprocess.Popen(command, stdout=subprocess.PIPE,
                           shell=True, preexec_fn=os.setsid)
    os.killpg(os.getpgid(pro.pid), signal.SIGTERM)


leftmargin = '30mm'
rightmargin = '30mm'
topmargin = '25mm'
bottommargin = '25mm'

kurssikoodi = 'KTKP010'
kurssinimi = 'Oppiminen ja ohjaus'

replacements = {}
replacements.update({'ä': '&auml;'})
replacements.update({'Ä': '&Auml;'})
replacements.update({'ö': '&ouml;'})
replacements.update({'Ö': '&ouml;'})
replacements.update({'kurssikoodi': kurssikoodi})
replacements.update({'kurssinimi': kurssinimi})

with open('koe.html') as infile, open('uusi.html', 'w') as outfile:
    for line in infile:
        for src, target in replacements.items():
            line = line.replace(src, target)
        outfile.write(line)

command = f'wkhtmltopdf -L {leftmargin}'
command += '-R {rightmargin}'
command += '-T {topmargin}'
command += '-B {bottommargin}'
command += ' uusi.html ./test.pdf'
compile_document(command)
