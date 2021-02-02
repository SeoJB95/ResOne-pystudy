from glob import glob
import shutil
import os

folderList = glob('./data/*')
for folder in folderList:
    folderName = os.path.basename(folder)
    fileList = glob(folder+'/*.dat')
    for file in fileList:
        fullName = os.path.basename(file).split('.')
        name = fullName[0]
        ext = fullName[1]
        if os.path.isdir('./data_result/'+name+'/'):
            shutil.copy(file,'./data_result/'+name+'/'+folderName+'-'+name+'.dat')
        else:
            os.mkdir('./data_result/'+name+'/')
            shutil.copy(file,'./data_result/'+name+'/'+folderName+'-'+name+'.dat')
