from glob import glob
import math
import os
import pandas as pd
import matplotlib.pyplot as plt

class Folder():
    def __init__(self,dir):
        self.folder_directory = dir
        self.filelist = {}
        self.File_reading()
    def File_reading(self):
        filelist = glob(self.folder_directory)
        for filedirectory in filelist:
            #print(filedirectory)
            F = File(filedirectory)
            if F.velocity == 'initial':
                self.initial = F
            else:
                self.filelist[F.velocity] = F
    # def Plotting(self):
    #     for i in self.filelist:
    #         file = self.filelist[i]
    #         file.data.plot(x='t')
    #         plt.title(i)
    #         plt.show()
    def plotting_powering(self):
        for i in self.filelist:
            file = self.filelist[i]
            plt.plot(float(i)/100,file.power,'ro')
        plt.show()

class File():
    def __init__(self,dir):
        self.directory = dir
        self.parsing()
        self.analysis()
    def parsing(self):
        result = pd.read_csv(self.directory,sep='\t',skiprows=1,names=['t','V','I','deg','torque','tmp'])
        result = result.drop(columns=['tmp'])
        result = result.apply(FileHandling_tool.Outlier_filter)
        self.data = result.apply(FileHandling_tool.Moving_averaging,window=10)
        filename = os.path.basename(self.directory).split('.')
        self.velocity = filename[0]
    def analysis(self):
        self.ohm = 10000
        self.Vrms = math.sqrt(sum([i**2 for i in self.data.V])/len(self.data.V))
        self.power = self.Vrms**2/self.ohm
class FileHandling_tool():
    def Outlier_filter(series):
        mean = series.mean()
        std = series.std()
        tmp =[]
        for i in series:
            if i>mean-3*std and i<mean+3*std:
                tmp.append(i)
            else:
                tmp.append(0)
        tmp_series = pd.Series(tmp)
        return tmp_series
    def Moving_averaging(series,window):
        tmp = []
        window_value_list= []
        if series.name=='t':
            return series
        else:
            for i in series:
                window_value_list.append(i)
                if len(window_value_list)<window:
                    tmp.append(i)
                elif len(window_value_list)==window:
                    mean = sum(window_value_list)/len(window_value_list)
                    tmp.append(mean)
                else:
                    #longer than 'window'
                    window_value_list.pop(0) # eliminate first value in list
                    mean = sum(window_value_list)/len(window_value_list)
                    tmp.append(mean)
            return tmp

if __name__ == '__main__':
    Folder = Folder('../cylinder_test/data/C-S5-W047/*.dat')
    Folder.plotting_powering()

    #Folder.Plotting()
    #print(Folder.filelist)
    #FH = File('../cylinder_test/data/C-S5-W047/110.dat')
    #FH.parsing()
    #print(FH)
    # print(FH.data)
    # FH.data.plot(x='t')
    # plt.title(FH.velocity)
    # plt.show()

    # FH.parsing()
    # FileHandler.parsing()
