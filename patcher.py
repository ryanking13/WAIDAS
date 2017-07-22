import os

def generate_batch(ids, files, dir):
    base_command = 'ffdec.bat -replace'
    original_file = 'WhyAmIDeadAtSea.swf'
    batch = 'run.bat'

    f = open(batch, 'w')

    f.write('%s %s %s ' % (base_command, original_file, original_file))

    for i in range(len(ids)):
        f.write('%s %s%s ' % (ids[i], dir, files[i]))

def main():
    script_dir = 'patch-data/'

    files = os.listdir(script_dir)
    file_ids = []
    for file in files:
        file_ids.append(file.split('_')[0])

    generate_batch(file_ids, files, script_dir)

if __name__ == '__main__':
    main()