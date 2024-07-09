#if-else
import webbrowser

chat = True
helloIntent = ["hello","hey","hi","wassup","hlo"]
while chat==True:
    msg = input("Enter Msg:").lower()
    if msg in helloIntent:
        print("Hey...")
    elif msg=="bye":
        print("Bye...")
        chat=False
    elif msg.startswith("open"):
        webbrowser.open("https://www."+msg.split()[-1]+".com")
    else:
        print("Sorry I don't Understand")

