

#students= ['ana','marge','layla','ruby']
#grades=[77,88,90,92]
#s=' '.join(students)

#for i in range(0,4):
 #   entry=students[i]+"-"+str(grades[i])+'\n'
 #   file.write(s)
    

#file.close()
 
#!/usr/bin/python3

import cgi
import random

def htmlTop():
    print ('''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
            <title>My first server-side script. </title>
        </head>
        <body>''')


def htmlTail():
    print ('''</body>
        </html>''')

def sub(*args):
    result_place=Element('output')
    result_place.write(f"<p>Hi {Element('FullName').value}, thanks for submitting your question.</p>")
    target=document.getElementById("output")
    target.style.backgroundColor="gainsboro"


form = cgi.FieldStorage()
    
question = form.getvalue('question')
print( "<html>")
print ("<head>")
print("<title> Hello - Second CGI Program</title>") 
print( "</head>" )
print( "<body>")
text = open('form.txt', 'a')
text.write('test')
text.close()
print( "</body>")
print ("</html>")



