import tarfile
import zipfile
from google.cloud import storage


class UntarUtility:

    def untarfile(self, inpath):
        print "File Source : ", inpath
        storage_client = storage.Client.from_service_account_json("D:\Project Data\CableVision\GCP_credentials.json")
        bucket = storage_client.get_bucket("dm_demo_bucket")
        if inpath.endswith(".tar") | inpath.endswith(".tgz") | inpath.endswith(".tar.gz") | inpath.endswith(".gz"):
            try:
                tar = tarfile.open(inpath)
                for tarinfo in tar:
                    filename = tarinfo.name
                    print "--", filename
                    if filename is not None:
                        blob = bucket.blob(filename)
#                       Passing file object
                        blob.upload_from_file(tar.extractfile(tarinfo))

                        #Reading file contents and paasing as a string
                        #file = tar.extractfile(tarinfo)
                        #data = file.read()
                        #blob.upload_from_string(data)
                        #file.close()
                tar.close()
            except Exception, e:
                print("Upload Failed : ", e.args)
            else:
                print "Upload Successful"
        elif inpath.endswith(".zip"):
            try:
                zip = zipfile.ZipFile(inpath, "r")
                for name in zip.namelist():
                    print "--", name
                    blob = bucket.blob(name)
                    obj = zip.open(name, "r")
                    data = obj.read()
                    blob.upload_from_string(data)
                    obj.close()
                zip.close()
            except Exception, e:
                print "Upload Failed : ", e.message
            else:
                print "Upload Successful"


untar_utility = UntarUtility()
inpath = "C:\Users\Yogesh.Khopade\Desktop\Temp\sample.tar"
#inpath = "C:\Users\Yogesh.Khopade\Desktop\Temp\sample.gz"
#inpath = "C:\Users\Yogesh.Khopade\Desktop\Temp\sample.tar.gz"
#inpath = "C:\Users\Yogesh.Khopade\Desktop\Temp\sample.tgz"
#inpath = "C:\Users\Yogesh.Khopade\Desktop\Temp\sample.zip"
untar_utility.untarfile(inpath)
