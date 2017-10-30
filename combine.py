import os
import sys
import shutil
import ast
def combine_dirs(wavdir, txtdir):
        wavsubdir = os.listdir(wavdir)
        if(wavdir[-1] != '/'):
                wavdir = wavdir + '/'
        if(not os.path.exists('wav')):
                os.mkdir('wav')
        for sub in wavsubdir:
                full_dir = wavdir + sub + '/'
                files = os.listdir(full_dir)
                for f in files:
                        full_file_name = os.path.join(full_dir, f)
                        if(os.path.isfile(full_file_name)):
                                shutil.copy(full_file_name, 'wav')
        txtsubdir = os.listdir(txtdir)
        if(txtdir[-1] != '/'):
                txtdir = txtdir + '/'
        if(not os.path.exists('txt')):
                os.mkdir('txt')
        for sub in txtsubdir:
                full_dir = txtdir + sub + '/'
                files = os.listdir(full_dir)
                for f in files:
                        full_file_name = os.path.join(full_dir, f)
                        if(os.path.isfile(full_file_name)):
                                shutil.copy(full_file_name, 'txt')
if __name__ == '__main__':
        arguments = sys.argv[1:]
        if(len(arguments) > 2):
                raise IOError("Arguments must not be greater to %d" % 2)
        wav_files = arguments[0]
        txt_files = arguments[1]
        combine_dirs(wav_files)
