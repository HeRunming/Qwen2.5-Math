import os

def expand_jsonl(repeats=32):
    print("--- JSONL 文件倍增工具 (x32) ---")
    
    # 1. 获取输入路径
    while True:
        input_path = input("请输入源 .jsonl 文件路径 (可直接拖入文件): ").strip()
        # 处理可能的引号（例如 Windows 复制路径时带的引号）
        input_path = input_path.strip('"').strip("'")
        
        if os.path.exists(input_path) and os.path.isfile(input_path):
            break
        else:
            print("错误：文件不存在，请重新输入。")

    # 2. 获取输出路径
    default_output = os.path.splitext(input_path)[0] + "_x32.jsonl"
    output_path = input(f"请输入保存路径 (直接回车默认保存为: {default_output}): ").strip()
    output_path = output_path.strip('"').strip("'")
    
    if not output_path:
        output_path = default_output

    print(f"\n正在处理... 将源文件写入 32 次到目标文件。")

    try:
        # 使用 utf-8 编码打开文件
        with open(output_path, 'w', encoding='utf-8') as out_f:
            with open(input_path, 'r', encoding='utf-8') as in_f:
                
                for i in range(repeats):
                    # 读取每一行并写入
                    for line in in_f:
                        out_f.write(line)
                    
                    # 确保最后一行有换行符（防止文件拼接时两行并作一行）
                    # 注意：如果原始文件非常严谨，通常不需要这一步，
                    # 但为了安全起见，可以判断上一行末尾是否是 \n，这里简化处理直接写入流
                    
                    # 重要：将源文件的读取指针重置到开头
                    in_f.seek(0)
                    
                    # 打印简单进度条
                    print(f"进度: {i+1}/{repeats} 完成")

        print(f"\n✅ 成功！文件已保存在: {output_path}")

    except Exception as e:
        print(f"\n❌ 发生错误: {e}")

if __name__ == "__main__":
    expand_jsonl()