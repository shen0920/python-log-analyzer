import argparse
def count_lines(path):
    with open(path,encoding='utf-8') as f:
        return sum(1 for _ in f)

def parse_args():
    parse = argparse.ArgumentParser(description='Count lines in a file')
    parse.add_argument('path', type=str, help='Path to the file')
    return parse.parse_args()
def main():
    args = parse_args()
    try:
         line_count = count_lines(args.path)
    except OSError as e:
        raise SystemExit(f"无法读取文件：{args.path}. 错误信息: {e}")
    print(f"文件 {args.path} 的行数为: {line_count}")
if __name__ == '__main__':
    main()
