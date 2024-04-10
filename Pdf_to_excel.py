from PIL import Image
from pytesseract import image_to_string
import PyPDF2
import fitz
import pytesseract
import numpy as np
import pandas as pd
import PIL
from pdf2image import convert_from_path
import numpy as np
import cv2
from PIL import Image
import cv2
import pandas as pd
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pdf_file=r"C:\Users\RaJat sharma\Downloads\GRAD020071-3-1-10-1-10.pdf"
pdf_document = fitz.open(pdf_file)
pages = convert_from_path(pdf_file, poppler_path=r"C:\Users\RaJat sharma\Downloads\Release-24.02.0-0\poppler-24.02.0\Library\bin")

x=847
y=1885
s1=190
s2=577
e1=755
e2=256

s3=865
x1=500
ex1=603

a=1530
b=380
l=1240
w=165
er1=1400
er2=938


aa=1190
bb=430
ll=330
ww=120
err1=2310
err2=983




otherdetail = []

name = []
adress=[]
father = []
address_numbers = []
sex=[]
age=[]
number=[]
kk=2
makan=[]
serial=[]
sr=0
for kk in range(2,pdf_document.page_count):
    
    im = pages[kk]
    im = np.array(im)
    im = cv2.resize(im, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    _, im = cv2.threshold(im, 180, 255, cv2.THRESH_BINARY)
    
    im=Image.fromarray(im)
    a=1100
    x=850
    e=50
    for ttt in range(8):
        
        im1=im.crop((480,a,2400,a+x))
        
        headerp = pytesseract.image_to_string(im1, lang='eng')
        
        
        name.append(headerp)
    
        print(headerp)
        im2=im.crop((2400,a,4300,a+x))
        
        headerp = pytesseract.image_to_string(im2, lang='eng')
        b=headerp.split("\n\n")
        father.append(headerp)
        print(headerp)
        im2=im.crop((4300,a,6400,a+x))
        
        headerp = pytesseract.image_to_string(im2, lang='eng')
        c=headerp.split("\n\n")
        adress.append(headerp)
        print(c)
        a=a+x+e
        

        
        
        
im.show()  
name   
    
len(adress)
      im = pages[2]
      im = np.array(im)
      im = cv2.resize(im, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
      _, im = cv2.threshold(im, 180, 255, cv2.THRESH_BINARY)
      
      im=Image.fromarray(im)




im1=im.crop((480,a,480+1920,a+x))
im1.show()    
headerp = pytesseract.image_to_string(im1, lang='eng')
print(headerp)
a=a+x+e
name.append(headerp)


a=1100
x=850
e=50



# Assuming you have three lists: names, father_names, and numbers
data = {'Name': name, 'Father Name': father, 'adress': adress}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)




excel_file_path = 'freelancerpage2-last.xlsx'

# Save the DataFrame to the Excel file
df.to_excel(excel_file_path, index=False)

print(f'DataFrame saved to {excel_file_path}')


    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
    
    
    
text = """John
 Doe
Father: Mike

 Doe
Address: 123 Main St

Jane Smith
Father: David Smith
Address: 456 Oak Ave"""

data = text.split("\n\n")
print(data)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    head=im.crop((190,215,2000,350))
    
    headerp = pytesseract.image_to_string(head, lang='hin')
    print(headerp)
    if "घटक" not in headerp:
        
        
        
        
        
        for j in range(10):
            for i in range(3):
                cin = im.crop((s1,s2, s1+y, s2+x))
                entry = pytesseract.image_to_string(cin, lang='hin')
                
                lines = entry.split("\n")
                if len(lines) > 1:  # Check if there are at least 2 lines of text
                        g_name_line = lines[1].strip()
                        father_names.append(g_name_line)
                        name_line = lines[0].strip()
                        name = name_line.split(":")[-1].strip() if ":" in name_line else (name_line.split(";")[-1].strip() if ";" in name_line else name_line)

                        names.append(name)
                        cn1= im.crop((s1,s3,s1+y, s3+x1))
                        
                        text2 = pytesseract.image_to_string(cn1, lang='eng+hin')
                        
                        li = text2.split("\n")
                        sr+=1
                        serial.append(sr)
                        print(sr)
                        
                        
                        otherdetail.append(headerp)
                        
                        if len(li)>1:
                            first = li[0].strip()
                            makn = first.split(":")[-1].strip() if ":" in first else (first.split(";")[-1].strip() if ";" in first else first)

                            makan.append(makn)
                            second = li[1].strip()
                            ages = second.split(":")[1].strip() if ":" in second[:7] else (second.split(";")[1].strip() if ";" in second else second)

                            
                            sex.append(ages)
                            cn= im.crop((a,b, a+l, b+w))
                            
                            text2 = pytesseract.image_to_string(cn, lang='eng')
                            number.append(text2)
                            
                            
                            
                            
                        else:
                            names.pop()
                            father_names.pop()
                            serial.pop()
                            otherdetail.pop()
                        
                        s1=s1+y+e1
                        a=a+l+er1
                        aa=aa+ll+err1
                        
               #cin.show()
                #cn.show()
            s2=s2+x+e2
            b=b+w+er2
            s3=s3+x1+ex1
            bb=bb+ww+err2
            s1=190
            a=1530
            aa=1190
            
            
        s1=190
        a=1530
        x=847
        y=1885
        s1=190
        s2=577
        e1=755
        e2=256
        a=1530
        b=380
        l=1240
        w=165
        er1=1400
        er2=938
        s3=865
        x1=500
        ex1=603
        bb=430
    else:
 
         
        for j in range(10):
            for i in range(3):
                cin = im.crop((s1,s2, s1+y, s2+x))
                entry = pytesseract.image_to_string(cin, lang='hin')
                
                lines = entry.split("\n")
                if len(lines) > 1:  # Check if there are at least 2 lines of text
                        g_name_line = lines[1].strip()
                        father_names.append(g_name_line)
                        name_line = lines[0].strip()
                        name = name_line.split(":")[-1].strip() if ":" in name_line else (name_line.split(";")[-1].strip() if ";" in name_line else name_line)

                        names.append(name)
                        cn1= im.crop((s1,s3,s1+y, s3+x1))
                        
                        text2 = pytesseract.image_to_string(cn1, lang='eng+hin')
                        
                        li = text2.split("\n")
                        sr+=1
                        serial.append(sr)
                        print(sr)
                        sb=im.crop((aa,bb,aa+ll,bb+ww))
                        
                        sbt= pytesseract.image_to_string(sb,config='--psm 6 outputbase digits')
                        otherdetail.append(sbt)
                        
                        if len(li)>1:
                            first = li[0].strip()
                            makn = first.split(":")[-1].strip() if ":" in first else (first.split(";")[-1].strip() if ";" in first else first)

                            makan.append(makn)
                            second = li[1].strip()
                            ages = second.split(":")[1].strip() if ":" in second[:7] else (second.split(";")[1].strip() if ";" in second else second)

                            ages=ages.split(" ")[0]
                            
                            sex.append(ages)
                            
                            
                            cn= im.crop((a,b, a+l, b+w))
                            
                            text2 = pytesseract.image_to_string(cn, lang='eng')
                            number.append(text2)
                            sb=im.crop((aa,bb,aa+ll,bb+ww))
                            
                            
                            
                            
                        else:
                            names.pop()
                            father_names.pop()
                            serial.pop()
                            otherdetail.pop()
                        
                        s1=s1+y+e1
                        a=a+l+er1
                        aa=aa+ll+err1
                        
               #cin.show()
                #cn.show()
            s2=s2+x+e2
            b=b+w+er2
            s3=s3+x1+ex1
            bb=bb+ww+err2
            s1=190
            a=1530
            aa=1190
            
            
        s1=190
        a=1530
        x=847
        y=1885
        s1=190
        s2=577
        e1=755
        e2=256
        a=1530
        b=380
        l=1240
        w=165
        er1=1400
        er2=938
        s3=865
        x1=500
        ex1=603
        bb=430
        
 
otherdetail
len(otherdetail) 
    

cn1.show()
text2
li[0]
print(
len(number),
len(names),
len(father_names),
len(sex),
len(makan))

father_names
number
names
makan


# Assuming you have three lists: names, father_names, and numbers
data = {'sr':serial,'Name': names, 'Father Name': father_names, 'Number': number,'age': sex,'makan': makan,'od':otherdetail}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)




excel_file_path = '3voteriddatam.xlsx'

# Save the DataFrame to the Excel file
df.to_excel(excel_file_path, index=False)

print(f'DataFrame saved to {excel_file_path}')











