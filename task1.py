import os
import shutil
import argparse
from pathlib import Path

def get_unique_filename(dest_dir, filename):
    base_name, ext = os.path.splitext(filename)
    counter = 1
    unique_name = filename

    while os.path.exists(os.path.join(dest_dir, unique_name)):
        unique_name = f"{base_name}({counter}){ext}"
        counter += 1

    return unique_name

def copy_and_sort_files(src_dir, dest_dir):
    try:
        for item in os.listdir(src_dir):
            src_item_path = os.path.join(src_dir, item)

            if os.path.isdir(src_item_path):
                copy_and_sort_files(src_item_path, dest_dir)

            elif os.path.isfile(src_item_path):
                file_extension = Path(item).suffix.lower() or "unknown"
                dest_subdir = os.path.join(dest_dir, file_extension[1:] if file_extension.startswith('.') else file_extension)
                os.makedirs(dest_subdir, exist_ok=True)

                unique_filename = get_unique_filename(dest_subdir, item)
                dest_file_path = os.path.join(dest_subdir, unique_filename)

                shutil.copy2(src_item_path, dest_file_path)
    except Exception as e:
        print(f"Error processing {src_dir}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Recursive file sorter.")
    parser.add_argument("source", type=str, help="Path to the source directory.")
    parser.add_argument("destination", type=str, nargs="?", default="dist", help="Path to the destination directory.")

    args = parser.parse_args()
    src_dir = args.source
    dest_dir = args.destination

    if not os.path.exists(src_dir):
        print(f"Error: Source directory '{src_dir}' does not exist.")
        return

    os.makedirs(dest_dir, exist_ok=True)

    copy_and_sort_files(src_dir, dest_dir)

    print(f"Files from '{src_dir}' have been successfully copied and sorted into '{dest_dir}'.")


if __name__ == "__main__":
    main()
