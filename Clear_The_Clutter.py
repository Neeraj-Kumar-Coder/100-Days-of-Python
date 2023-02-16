import glob
import os

os.chdir("./Sample Images")

try:
    extention = input(
        "Enter the extension you want to rename in order(eg: txt, pdf, xls): ")
    count = 0
    for file in glob.glob(f"*.{extention}"):
        count += 1
        source = f"./{file}"
        destination = f"./Sample_Image_{count}.jpg"
        os.rename(source, destination)

    print(f"{count} file{'s' if count > 1 else ''} renamed successfully!")
except Exception as e:
    print(e)

print("Program exited...")
