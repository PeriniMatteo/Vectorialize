import Image, ImageDraw
import numpy as np

global n,xp,yp,m, start

start=False
LEVELS=[200,150,100,50]
imm=Image.open('don.jpg').convert('L')
#imm.show()

b=np.asarray(imm)
xm,ym=b.shape
print xm,ym

n=5
xp=range(0,xm,n)
yp=range(0,ym,n)
print "len(xp) = ",len(xp)
print "len(yp) = ",len(yp)
m=np.zeros((len(xp),len(yp)))
#mx=np.zeros((len(xp)-1,len(yp)-1))
#my=np.zeros((len(xp)-1,len(yp)-1))
print m.shape
for i,xx in enumerate(xp):
    for j,yy in enumerate(yp):
        #print i,j
        m[i,j]=int(b[xx:xx+n-1,yy:yy+n-1].mean())

#m[10:20,30:100]=0
#b=(m>200)*255
#im= Image.fromarray((m>LEVELS[3])*255.0)
im= Image.fromarray(m)
im.convert('L').save('t.jpg')

def writeLine(X0,Y0,W,H,filedest):
    filedest.write('        <path\n')
    filedest.write('       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"\n')
    filedest.write('       d="m %.3f,%.3f %.3f,%.3f"\n'%(X0,Y0,W,H))
    filedest.write('       inkscape:connector-curvature="0" />\n')

def draw_horizontal():
    global start
    #start=False
    for j,yy in enumerate(xp):
        start=False
        stop=False
        for i,xx in enumerate(yp):
            if m[j,i]<= LEVELS[0] and not(start):
                start=xx
            elif m[j,i]<= LEVELS[0] and xx==max(yp) and start:
                stop=xx
                writeLine(start,yy,(stop-start),0,out_file)
            elif m[j,i]>LEVELS[0] and start:
                stop=xx
                writeLine(start,yy,(stop-start),0,out_file)
                #print "writeLine("+str(start*n)+","+str((j-1)*n)+","+str((stop-start)*n)+",0,out_file)"
                start=False
                stop=False
            else:
                pass
                
def draw_vertical():
    global start
    for j,yy in enumerate(yp):
        start=False
        stop=False
        for i,xx in enumerate(xp):
            if m[i,j]<= LEVELS[1] and not(start):
                start=xx
            elif m[i,j]<= LEVELS[1] and xx==max(xp) and start:
                stop=xx
                writeLine(yy,start,0,(stop-start),out_file)
            elif m[i,j]>LEVELS[1] and start:
                stop=xx
                writeLine(yy,start,0,(stop-start),out_file)
                start=False
                stop=False
            else:
                pass
                
def draw_obl1():
    global start
    
    for j,yy in enumerate(xp):
        i=j
        j=0
        while i<len(xp):
            if m[i,j]<= LEVELS[2] and not(start):
                #print "1"
                start_i=i
                start_j=j
                i+=1
                j+=1
                start=True
            elif m[i,j]>LEVELS[2] and start:
                #print "2"
                stop_i=i
                stop_j=j
                writeLine(start_j*n,start_i*n,(stop_j-start_j)*n,(stop_i-start_i)*n,out_file)
                start=False
                stop_i=False
                stop_j=False
                i+=1
                j+=1
            else:
                i+=1
                j+=1
        else:
            if start:
                stop_i=i
                stop_j=j
                writeLine(start_j*n,start_i*n,(stop_j-start_j)*n,(stop_i-start_i)*n,out_file)
                start=False
                stop_i=False
                stop_j=False
            else:
                start=False
                stop_i=False
                stop_j=False

    for j in range(1,len(yp[:-1])):
        i=0
        while i<len(xp) and j<len(yp):
            if m[i,j]<= LEVELS[2] and not(start):
                #print 
                start_i=i
                start_j=j
                i+=1
                j+=1
                start=True
            elif m[i,j]>LEVELS[2] and start:
                #print "2"
                stop_i=i
                stop_j=j
                writeLine(start_j*n,start_i*n,(stop_j-start_j)*n,(stop_i-start_i)*n,out_file)
                start=False
                stop_i=False
                stop_j=False
                i+=1
                j+=1
            else:
                i+=1
                j+=1
        else:
            if start:
                stop_i=i
                stop_j=j
                writeLine(start_j*n,start_i*n,(stop_j-start_j)*n,(stop_i-start_i)*n,out_file)
                start=False
                stop_i=False
                stop_j=False
            else:
                start=False
                stop_i=False
                stop_j=False

def draw_obl3():
    global start
    
    for j in range(1,len(xp[:-1])):
        i=j
        j=len(xp[:-1])
        while i<len(xp[:-1]):
            print j,i
            if j>len(xp[:-1]):
                start=False
                break
            if m[i,j]<= 50 and not(start):
                print "1"
                start_i=i
                start_j=j
                i+=1
                j-=1
                start=True
            elif m[i,j]>50 and start:
                print "2"
                stop_i=i
                stop_j=j
                writeLine(start_j*n,start_i*n,(stop_j-start_j)*n,(stop_i-start_i)*n,out_file)
                start=False
                i+=1
                j-=1
            else:
                #print "else"
                #pass
                i+=1
                j-=1

    for j in range(len(yp[:-1])):
        i=0
        while i<len(xp[:-1]):
            #print j,i
            if j<0:
                start=False
                break
            if m[i,j]<= 50 and not(start):
                #print "1"
                start_i=i
                start_j=j
                i+=1
                j-=1
                start=True
            elif m[i,j]>50 and start:
                #print "2"
                stop_i=i
                stop_j=j
                writeLine(start_j*n,start_i*n,(stop_j-start_j)*n,(stop_i-start_i)*n,out_file)
                start=False
                i+=1
                j-=1
            else:
                #print "else"
                #pass
                i+=1
                j-=1
def draw_obl2():
    global start
    for j,yy in enumerate(yp):
        i=j
        j=len(yp[:-1])
        while i<len(xp):
            if m[i,j]<= LEVELS[3] and not(start):
                #print "1"
                start_i=i
                start_j=j
                i+=1
                j+=-1
                start=True
            elif m[i,j]>LEVELS[3] and start:
                #print "2"
                stop_i=i
                stop_j=j
                writeLine(start_j*n,start_i*n,(stop_j-start_j)*n,(stop_i-start_i)*n,out_file)
                start=False
                stop_i=False
                stop_j=False
                i+=1
                j+=-1
            else:
                i+=1
                j+=-1
        else:
            if start:
                stop_i=i
                stop_j=j
                writeLine(start_j*n,start_i*n,(stop_j-start_j)*n,(stop_i-start_i)*n,out_file)
                start=False
                stop_i=False
                stop_j=False
            else:
                start=False
                stop_i=False
                stop_j=False

    for j in range(1,len(yp[:-1])):
        i=0
        while i<len(xp) and j<len(yp):
            if m[i,j]<= LEVELS[3] and not(start):
                #print 
                start_i=i
                start_j=j
                i+=1
                j+=-1
                start=True
            elif m[i,j]>LEVELS[3] and start:
                #print "2"
                stop_i=i
                stop_j=j
                writeLine(start_j*n,start_i*n,(stop_j-start_j)*n,(stop_i-start_i)*n,out_file)
                start=False
                stop_i=False
                stop_j=False
                i+=1
                j+=-1
            else:
                i+=1
                j+=-1
        else:
            if start:
                stop_i=i
                stop_j=j
                writeLine(start_j*n,start_i*n,(stop_j-start_j)*n,(stop_i-start_i)*n,out_file)
                start=False
                stop_i=False
                stop_j=False
            else:
                start=False
                stop_i=False
                stop_j=False

#im=Image.new("L",(ym,xm),color="black")
#draw = ImageDraw.Draw(im)
####im= Image.fromarray(m)
####im.show()

#for j in range(len(yp))[:-1]:
#    for i in range(len(xp))[:-1]:
#        draw.ellipse([(my[i,j],mx[i,j]),(my[i,j]+m[i,j]*n/255,mx[i,j]+m[i,j]*n/255)],fill='white')
#        #draw.point((my[i,j],mx[i,j]),fill='black')
#im.show()
out_file=open('Output.svg','w')
out_file.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
out_file.write('<svg\n')
out_file.write('   xmlns:dc="http://purl.org/dc/elements/1.1/"\n')
out_file.write('   xmlns:cc="http://creativecommons.org/ns#"\n')
out_file.write('   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n')
out_file.write('   xmlns:svg="http://www.w3.org/2000/svg"\n')
out_file.write('   xmlns="http://www.w3.org/2000/svg"\n')
out_file.write('   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"\n')
out_file.write('   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"\n')
out_file.write('   width="'+str(ym)+'"\n')
out_file.write('   height="'+str(xm)+'"\n')
out_file.write('   id="svg2"\n')
out_file.write('   version="1.1"\n')
out_file.write('   inkscape:version="0.48.4 r9939"\n')
out_file.write('   sodipodi:docname="cerchiotest.svg">\n')
out_file.write('  <sodipodi:namedview\n')
out_file.write('     id="base"\n')
out_file.write('     pagecolor="#ffffff"\n')
out_file.write('     bordercolor="#666666"\n')
out_file.write('     borderopacity="1.0"\n')
out_file.write('     inkscape:pageopacity="0.0"\n')
out_file.write('     inkscape:pageshadow="2"\n')
out_file.write('     inkscape:zoom="0.35"\n')
out_file.write('     inkscape:cx="375"\n')
out_file.write('     inkscape:cy="520"\n')
out_file.write('     inkscape:document-units="px"\n')
out_file.write('     inkscape:current-layer="layer1"\n')
out_file.write('     />\n')

# Drawing the horizontal lines
out_file.write('  <g\n')
out_file.write('     inkscape:label="Horizontal"\n')
out_file.write('     inkscape:groupmode="layer"\n')
out_file.write('     id="layer1">\n')
draw_horizontal()
out_file.write('  </g>\n')

# Drawing the vertical lines
out_file.write('  <g\n')
out_file.write('     inkscape:label="Vertical"\n')
out_file.write('     inkscape:groupmode="layer"\n')
out_file.write('     id="layer2">\n')
draw_vertical()
out_file.write('  </g>\n')

# Drawing the obliquos lines
out_file.write('  <g\n')
out_file.write('     inkscape:label="Obl1"\n')
out_file.write('     inkscape:groupmode="layer"\n')
out_file.write('     id="layer3">\n')
draw_obl1()
out_file.write('  </g>\n')

# Drawing the obliquos inverse lines 
out_file.write('  <g\n')
out_file.write('     inkscape:label="Obl2"\n')
out_file.write('     inkscape:groupmode="layer"\n')
out_file.write('     id="layer4">\n')
draw_obl2()
out_file.write('  </g>\n')


out_file.write('</svg>')
out_file.close()
