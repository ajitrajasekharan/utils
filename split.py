import pdb
import os
import shutil
import argparse
import random


def make_subdir(dest_dir,dir_name):
    try:
        os.mkdir(dest_dir + "/" + dir_name)
    except:
        pass

def split_data(input_dir,test,val):
    train_dir = "train"
    val_dir = "val"
    test_dir = "val"
#    test_dir = "test"
    try:
        os.mkdir(train_dir)
        os.mkdir(val_dir)
        os.mkdir(test_dir)
    except:
        print("Output directories:", train_dir,val_dir,test_dir," already exists") 
    total = 0
    train_count = 0 
    val_count = 0 
    for dir_name in os.listdir(input_dir):
        dir_name_full = os.path.join(input_dir, dir_name)
        for file_name in os.listdir(dir_name_full):
            input_file = os.path.join(dir_name_full, file_name)
            if  os.path.isfile(input_file):
                #if (input_file.endswith(".npy")):
                if (input_file.lower().endswith(".jpeg") or input_file.lower().endswith(".png") or input_file.lower().endswith(".jpg")):
                    value = random.randint(1,100)
                    if (value < test):
                        dest_dir = test_dir
                    else:
                        if (value < test + val):
                            dest_dir = val_dir
                            val_count += 1
                        else:
                            dest_dir = train_dir
                            train_count += 1
                    total += 1
                    output_file = dest_dir + "/" + dir_name + "/" +  file_name
                    make_subdir(dest_dir,dir_name)
                    print(input_file,output_file)
                    shutil.copyfile(input_file, output_file)
    print("percent train:", round(float(train_count)/total,2)*100, " validation ",round(float(val_count)/total,2)*100)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split data into train/validate and test dirs',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-input', action="store", dest="input",default="complete",help='orig dir')
    parser.add_argument('-test', action="store", dest="test",default=10,type=int,help='percent to split for test')
    parser.add_argument('-val', action="store", dest="val",default=10,type=int,help='percent to split for val/finetune')
    
    results = parser.parse_args()
    split_data(results.input,results.test,results.val)


