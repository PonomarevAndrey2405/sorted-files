def sorted_files(files: list, path: str) -> None:
    text = {sum(1 for _ in open(file, encoding="windows-1251")): file for file in files}
    with open(path, "w") as file_write:
        file_write.write("")
    with open(path, "a") as file_write:
        for key in sorted(text.keys()):
            file_write.write(text[key] + "\n")
            file_write.write(str(key) + "\n")
            file_write.writelines(line for line in open(text[key], "r", encoding="windows-1251"))
            file_write.write("\n")

def main():
    files = ["1.txt", "2.txt", "3.txt"]
    sorted_files(files, "new_file.txt")

if __name__ == "__main__":
    main()
