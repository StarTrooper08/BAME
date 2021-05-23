import pywhatkit as pywk

#user input
question = input("Enter the question here :")
answer = input("Enter the Answer here :")

    


#function
pywk.text_to_handwriting("Question " + "" + question + "\n" + "Answer " + "" + answer,"imagename.png",rgb=[0,0,255])
