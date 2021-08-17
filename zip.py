import os
import zipfile
import shutil


def zipDir(path, zipFile):
    for root, dirs, files in os.walk(path):
        for file in files:
            zipFile.write(os.path.join(root, file),
            os.path.relpath(os.path.join(root, file),
            os.path.join(path, "..")
            )
        )


shutil.make_archive('DOCUMENT.zip', 'zip', 'Documents/')
