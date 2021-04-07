import io
import zipfile
import sys
s =0
c =0
for zz in zipfile.ZipFile(io.BytesIO(bytes.fromhex(sys.stdin.read()))).filelist:
    s += zz.file_size
    c += 0 if zz.is_dir() else 1
print(c,s)
