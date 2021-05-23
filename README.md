# BAME
Boring Assignment Made Easy

### Requirements :
1. Python 3 or greater version
2. Python module : **pywhatkit**
  
   Install it by typing command in your command prompt:
   
   cmd : **`pip install pywhatkit`**


### Code :
```
#importing pywhatkit module
import pywhatkit as pywk

#user input
question = input("Enter the question here :")
answer = input("Enter the Answer here :")


#function
pywk.text_to_handwriting("Question " + "" + question + "\n" + "Answer " + "" + answer,"imagename.png",rgb=[0,0,255])
```

### Function Attributes :
```
pywk.text_to_handwriting(  
                 "string"   ,         <---  String value should be passed as first parameter                 
             "imagename.png"    ,                         <---  Image name with png extension or complete path where to save iamge
                   rgb=[0,0,255]    )                              <---   color of the font

                       
```

### File Directory :
When we execute this code we get two files are generated 
1. image file which is in png format and which is the main output we required.
2. And other is text document(pywhatkit_dbs.txt file) which has "--" into it as a content.

![image](https://user-images.githubusercontent.com/72031540/119261536-78066a00-bbf5-11eb-9bd2-50f759a12d0d.png)

### Final Output Looks something like this:
![Capture1](https://user-images.githubusercontent.com/72031540/119251832-5b067280-bbc6-11eb-8bd5-6eaadd418657.PNG)



