import fire
import os

def encode2cn(file_name: str) -> str:
    try:
        file_name.encode('gb2312')
    except UnicodeEncodeError:
        try:
            file_name.encode('Shift-JIS')
            return file_name
        except UnicodeEncodeError:
            try:
                return file_name.encode('gbk').decode('Shift-JIS')
            except(UnicodeDecodeError, UnicodeEncodeError):
                return file_name
    return file_name

def traverse_dir(root_path: str):
    dir_path_list = []
    level_count = 0
    for file_tuple in os.walk(root_path):
        if not level_count == 0:
            if file_tuple[0][-1] == '\\':
                dir_path_list.append(file_tuple[0][:-1])
            else:
                dir_path_list.append(file_tuple[0])

        for file_name in file_tuple[-1]:
            old_file_name = os.path.join(file_tuple[0], file_name)
            new_file_name = os.path.join(file_tuple[0], encode2cn(file_name))
            if not old_file_name == new_file_name:
                os.rename(old_file_name, new_file_name)
        level_count += 1

    count_map = {}
    for dir_path in dir_path_list:
        divider_count = 0
        for c in dir_path:
            if c == '\\':
                divider_count += 1
        count_map[dir_path] = divider_count
    sorted_dir_path_list = sorted(count_map.items(), key=lambda x: x[1], reverse=True)

    for dir_path in sorted_dir_path_list:
        last_index = dir_path[0].rfind('\\')
        new_dir_path = os.path.join(dir_path[0][:last_index + 1], encode2cn(dir_path[0][last_index + 1:]))
        if not dir_path[0] == new_dir_path:
            os.rename(dir_path[0], new_dir_path)

if __name__ == '__main__':
    fire.Fire(traverse_dir)