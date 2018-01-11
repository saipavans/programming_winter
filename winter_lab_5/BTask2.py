
def sed(pattern,replacement,in_file,out_file):
    fin = None
    fout = None
    try:
        fin = open(in_file)
        fout = open(out_file,'w')
        for line in fin:
            replaced_line = line.replace(pattern,replacement)
            fout.write(replaced_line)
    except IOError as e:
        print("Exception in handling the files: ", e)
    finally:
        if fin is not None : fin.close()
        if fout is not None: fout.close()


input_file = "./resources/cape_cod.txt"
output_file = "./resources/tmp.txt"
sed("the", "dal", input_file, output_file)