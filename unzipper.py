import os
import zipfile
import shutil



pre, ext = os.path.splitext('./Docs/d1.docx')
os.rename('./Docs/d1.docx', pre + '.zip')



with zipfile.ZipFile('./Docs/d1.zip', 'r') as zip_ref:
    zip_ref.extractall('./contents/')


source_path = './contents/word/media/'
source_files = os.listdir(source_path)
dest = './Images/WMF_EMF'

for file in source_files:
    if file.endswith('.wmf') or file.endswith('.emf'):
        shutil.move(os.path.join(source_path, file), os.path.join(dest, file))




