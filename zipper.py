import os
import zipfile
import shutil
import fileinput

def zipDir(path, zipFile):
    for root, dirs, files in os.walk(path):
        for file in files:
            zipFile.write(os.path.join(root, file),
            os.path.relpath(os.path.join(root, file),
            os.path.join(path, "..")
            )
        )


source_path = './Images/PNG/'
source_files = os.listdir(source_path)
dest = './contents/word/media/'


for file in source_files:
    if file.endswith(".png"):
        shutil.move(os.path.join(source_path, file), os.path.join(dest, file))

file = open('./contents/word/_rels/document.xml.rels', 'r')
filedata=file.read()
file.close()

newdata = filedata.replace('wmf', 'png')

file = open('./contents/word/_rels/document.xml.rels', 'w')
file.write(newdata)
file.close()

file2 = open('./contents/[Content_Types].xml', 'r')
filedata2=file2.read()
file2.close()

newdata2 = filedata2.replace('wmf', 'png')

file2 = open('./contents/[Content_Types].xml', 'w')
file2.write(newdata2)
file2.close()



shutil.make_archive('./Docs/d1-png', 'zip', './contents/')
pre, ext = os.path.splitext('./Docs/d1-png.zip')
os.rename('./Docs/d1-png.zip', pre + '.docx')
