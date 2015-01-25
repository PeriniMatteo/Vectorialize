import Image, ImageDraw
import numpy as np

global n,xp,yp,m, start

start=False

imm=Image.open('Bea.jpg').convert('L')
#imm.show()

b=np.asarray(imm)
xm,ym=b.shape
print xm,ym

n=10
xp=range(0,xm,n)
yp=range(0,ym,n)
print len(xp),len(yp)
m=np.zeros((len(xp)-1,len(yp)-1))
#mx=np.zeros((len(xp)-1,len(yp)-1))
#my=np.zeros((len(xp)-1,len(yp)-1))
print m.shape
for i in range(len(xp))[:-1]:
    for j in range(len(yp))[:-1]:
        m[i,j]=int(b[xp[i]:xp[i+1],yp[j]:yp[j+1]].mean())

im= Image.fromarray(m)
im.convert('L').save('t.jpg')

def writeLine(X0,Y0,W,H,filedest):
    filedest.write('        <path\n')
    filedest.write('       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"\n')
    filedest.write('       d="m %.3f,%.3f %.3f,%.3f"\n'%(X0,Y0,W,H))
    filedest.write('       inkscape:connector-curvature="0" />\n')

def draw_horizontal():
    global start
    for j in range(len(xp))[:-1]:
        for i in range(len(yp))[:-1]:
            if m[j,i]<= 200 and not(start):
                start=i
            elif m[j,i]>200 and start:
                stop=i
                writeLine(start*n,j*n,(stop-start)*n,0,out_file)
                start=False
            else:
                pass
                
def draw_vertical():
    global start
    for j in range(len(yp))[:-1]:
        for i in range(len(xp))[:-1]:
            if m[i,j]<= 150 and not(start):
                start=i
            elif m[i,j]>150 and start:
                stop=i
                writeLine(j*n,start*n,0,(stop-start)*n,out_file)
                start=False
            else:
                pass
                
def draw_obl1():
    global start
    
    for j in range(1,len(xp[:-1])):
        i=j
        j=0
        while i<len(xp[:-1]):
            print j,i
            if j==len(xp[:-1]):
                start=False
                break
            if m[i,j]<= 100 and not(start):
                print "1"
                start_i=i
                start_j=j
                i+=1
                j+=1
                start=True
            elif m[i,j]>100 and start:
                print "2"
                stop_i=i
                stop_j=j
                writeLine(start_j*n,start_i*n,(stop_j-start_j)*n,(stop_i-start_i)*n,out_file)
                start=False
                i+=1
                j+=1
            else:
                #print "else"
                #pass
                i+=1
                j+=1

    for j in range(len(yp[:-1])):
        i=0
        while i<len(xp[:-1]):
            #print j,i
            if j==len(yp[:-1]):
                start=False
                break
            if m[i,j]<= 100 and not(start):
                #print "1"
                start_i=i
                start_j=j
                i+=1
                j+=1
                start=True
            elif m[i,j]>100 and start:
                #print "2"
                stop_i=i
                stop_j=j
                writeLine(start_j*n,start_i*n,(stop_j-start_j)*n,(stop_i-start_i)*n,out_file)
                start=False
                i+=1
                j+=1
            else:
                #print "else"
                #pass
                i+=1
                j+=1

def draw_obl2():
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
