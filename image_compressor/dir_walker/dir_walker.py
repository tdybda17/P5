import os


def walk_dir(path, files_extensions=[]):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if files_extensions:
                for ex in files_extensions:
                    if ex in file:
                        files.append(os.path.join(r, file))
            else:
                files.append(os.path.join(r, file))
    return files
