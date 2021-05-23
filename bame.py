import pywhatkit as pywk

#user input
question = input("Enter the question here :")
answer = input("Enter the Answer here :")


'''
pywk.text_to_handwriting("variable or string here",
      "image_name.png ",   <--   image name including png extension or you can also specify complete path (example : C:\Users\User\Desktop\images\pywkimage.png)
      rgb=[0,0,255])       <-- color for the font
'''    



pywk.text_to_handwriting("Question " + "" + question + "\n" + "Answer " + "" + answer,"imagename.png",rgb=[0,0,255])
