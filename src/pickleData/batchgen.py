import pickle
import numpy as np
from PIL import Image

dataset = {
    'data': [],
    'labels': []
}

def gendata(img,label,n=32):
    converteddata = []
    im = Image.open(img).convert("RGB")
    im = im.resize((n,n))
    r, g, b = im.split()
    r, g, b = list(r.getdata()), list(g.getdata()), list(b.getdata())
    converteddata.extend(r)
    converteddata.extend(g)
    converteddata.extend(b)
    dataset['data'].append(converteddata)
    dataset['labels'].append(label)
    #print(dataset)

def pickleData(file_Name):
    dataset['data'] = np.array(dataset['data'])
    print(dataset)
    fileObject = open(file_Name,'wb')
    pickle.dump(dataset,fileObject)
    fileObject.close()

def testObj(file_Name):
    fileObj = open(file_Name,'rb')
    b = pickle.load(fileObj)
    fileObj.close()
    if ((np.array_equal(dataset['data'],b['data'])) and (dataset['labels']==b['labels'])):
        return True
    return False

gendata("test.gif",2,2)
gendata("test.gif",3,2)
pickleData("try")
print(testObj("try"))