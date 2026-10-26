import argparse

def count_lines(path):
    with open(path,encoding='utf-8') as f:
        return sum(1 for _ in f)

def count_ips(path):
    counts = {}
    with open(path,encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            ip = line.split()[0]  
            if ip in counts:
                counts[ip] += 1
            else:
                counts[ip] = 1
    return counts

def top_n(counts, n=10):
    sorted_counts = sorted(counts.items(), key=lambda item:(-item[1],item[0]))
    return sorted_counts[0:n]

def parse_args():
    parse = argparse.ArgumentParser(description='Count lines in a file')
    parse.add_argument('path', type=str, help='Path to the file')
    parse.add_argument('--top','-n', type=int, default=10, help='Number of top IPs to display')
    return parse.parse_args()

def main():
    args = parse_args()
    try:
        line_count = count_lines(args.path)
    except OSError as e:
        raise SystemExit(f"无法读取文件：{args.path}. 错误信息: {e}")
    print(f"文件 {args.path} 的行数为: {line_count}")
    ip_counts = count_ips(args.path)
    top_ips = top_n(ip_counts, args.top)
    i=0
    sum_count = sum(ip_counts.values())
    print(f"总 IP 地址数: {len(ip_counts)}")
    print(f"总访问次数: {sum_count}")
    print(f"前 {args.top} 个最常出现的 IP 地址:")
    for ip, count in top_ips:
        i+=1
        print(f" {i}. {ip}: {count} {count/sum_count:.2%}")
if __name__ == '__main__':
    main()
