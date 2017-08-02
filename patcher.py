import os

def generate_batch(ids, files, dir, open_type='w'):
    base_command = 'ffdec.bat -replace'
    original_file = 'WhyAmIDeadAtSea.swf'
    batch = 'run.bat'

    f = open(batch, open_type)

    f.write('%s %s %s ' % (base_command, original_file, original_file))

    for i in range(len(ids)):
        f.write('%s %s%s ' % (ids[i], dir, files[i]))

    f.write('\n')
    f.close()

def main():
    script_dir = 'patch-data/'
    non_script_dir = 'non-dialogue-script/'

    files = os.listdir(script_dir)
    file_ids = []
    for file in files:
        file_ids.append(file.split('_')[0])

    generate_batch(file_ids, files, script_dir, open_type='w')

if __name__ == '__main__':
    main()