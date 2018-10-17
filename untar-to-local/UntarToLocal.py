import tarfile, zipfile, os
class UntarToLocal :

    def untarfile(self, inpath, outpath):
        print "File Source : ", inpath
        print "File Target : ", outpath
        if inpath.endswith(".tar.gz") | inpath.endswith(".tgz"):
            try:
                tar = tarfile.open(inpath)
                for member in tar.getmembers():
                    file = tar.extractfile(member=member)
                    if file is not None:
                        print "--", file.name
                        file_data = file.read()
                        new_file = open(outpath+file.name, "w")
                        new_file.write(file_data)
                        new_file.close()
                tar.close()
            except Exception, e:
                print("Untar Failed : ", e.args)
            else:
                print "Untar Successful"
        elif inpath.endswith(".zip"):
            try:
                zip = zipfile.ZipFile(inpath,"r")
                #zip.extractall(path=outpath)
                for name in zip.namelist():
                    print "--", name
                    #file = zip.extract(info)
                    zfile = zip.open(name)
                    contents = zfile.read()
                    new_file = open(outpath+name, "w")
                    new_file.write(contents)
                    new_file.close()
                zip.close()
            except Exception, e:
                print "Unzip Failed : ", e.args
            else:
                print "Unzipped Sucessfully"


UntarLocal = UntarToLocal()
inpath = "C:\Users\Yogesh.Khopade\Desktop\Temp\sample.tar.gz"
#inpath = "C:\Users\Yogesh.Khopade\Desktop\Temp\sample.tgz"
#inpath = "C:\Users\Yogesh.Khopade\Desktop\Temp\sample.zip"
outpath = "C:\Users\Yogesh.Khopade\Desktop\Temp\sample\\"
UntarLocal.untarfile(inpath, outpath)
