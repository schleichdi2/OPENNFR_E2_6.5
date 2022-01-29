from Plugins.Plugin import PluginDescriptor
import subprocess
cmd = ['python3','-O','/usr/lib/enigma2/python/Plugins/Extensions/FileLoad/upload.pyc']
cmd1 = ['python3','-O','/usr/lib/enigma2/python/Plugins/Extensions/FileLoad/delete.pyc']
extScript = subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE)
extScript = subprocess.Popen(cmd1,shell=False,stdout=subprocess.PIPE)

def Plugins(**kwargs):
    return PluginDescriptor()
