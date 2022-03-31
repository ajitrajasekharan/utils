import pdb
import os
import shutil
from PIL import Image
import argparse
import torchvision.transforms as transforms


def rescale(input_file,output_file,height,width):
    trans = transforms.Compose([
        transforms.Resize(width),
        transforms.CenterCrop(width)
      ])
    transformed_sample = trans(Image.open(input_file)).convert('RGB')
    transformed_sample.save(output_file)

def get_size(input_file):
    Img = Image.open(input_file)
    width = Img.width
    height = Img.height
    Img.close()
    return width,height

def batched_rescale(input_dir,output_dir,height,width):
    try:
        os.mkdir(output_dir)
    except:
        print("Output directory:", output_dir," already exists") 
    log_info_file = output_dir +  "/conversion_log.txt"
    log_fp = open(log_info_file,"w")
    out_str = f"file_name|orig_width|orig_height|converted 1/0\n"
    log_fp.write(out_str)
    for file_names in os.listdir(input_dir):
        input_file = os.path.join(input_dir, file_names)
        if  os.path.isfile(input_file):
            if (input_file.endswith(".jpeg") or input_file.endswith(".jpg") or input_file.endswith(".png")):
                print(input_file)
                file_only = input_file.split("/")[-1]
                output_file =  output_dir + "/" +  file_only
                rescale(input_file,output_file,height,width)
                orig_width,orig_height = get_size(input_file)
                converted = "1" if (orig_width != width or orig_height != height) else "0"
                out_str = f"{file_only}|{orig_width}|{orig_height}|{converted}\n"
                log_fp.write(out_str)
                #shutil.copyfile(f,  output_dir + "/" +  file_only)
    log_fp.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image Rescale',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-input', action="store", dest="input",required=True,help='Input image file name or batch dir')
    parser.add_argument('-output', action="store", dest="output",required=True,help='Output image file name or batch dir')
    parser.add_argument('-width', action="store", dest="width",default=384,type=int,help='Width')
    parser.add_argument('-height', action="store", dest="height",default=384,type=int,help='Height')
    parser.add_argument('-batched', dest="batched", action='store_true',help='Is this batch convert')
    parser.add_argument('-no-batched', dest="batched", action='store_false',help='Is this not batch convert')
    parser.set_defaults(batched=False)
    
    results = parser.parse_args()
    if (results.batched):
        batched_rescale(results.input,results.output,results.height,results.width)
    else:
        rescale(results.input,results.output,results.height,results.width)

