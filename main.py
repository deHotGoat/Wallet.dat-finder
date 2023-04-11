import os
import concurrent.futures
import time

start_time = time.time()
def find_file(file_name, root_path):
    for dirpath, _, files in os.walk(root_path):
        if file_name in files:
            return os.path.abspath(os.path.join(dirpath, file_name))
    return None

def search_file(file_name, root_paths):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(find_file, file_name, root_path) for root_path in root_paths]
        for result in concurrent.futures.as_completed(results):
            file_path = result.result()
            if file_path:
                return file_path
    return None

if __name__ == '__main__':
    file_name = 'wallet.dat'
    root_paths = ["C:\\", "D:\\", "E:\\", "F:\\", "\\\\server\\share\\"]
    file_path = search_file(file_name, root_paths)
    print(f"File path: {file_path}")
    end_time = time.time()
    total_time = start_time - end_time
    print(total_time)
