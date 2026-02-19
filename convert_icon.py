#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
将PNG或其他格式的图片转换为标准ICO格式
如果icon.ico已经是标准格式，此脚本会提示
"""

import os
from PIL import Image

def convert_to_ico(input_path, output_path, sizes=None):
    """
    将图片转换为ICO格式
    
    Args:
        input_path: 输入图片路径
        output_path: 输出ICO路径
        sizes: ICO文件包含的尺寸列表，默认包含常用尺寸
    """
    if sizes is None:
        sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    
    try:
        # 打开图片
        img = Image.open(input_path)
        
        # 如果是RGBA模式，确保有透明通道
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # 创建ICO文件，包含多个尺寸
        img.save(output_path, format='ICO', sizes=sizes)
        print(f"✓ 成功转换图标: {output_path}")
        print(f"  包含尺寸: {sizes}")
        return True
    except Exception as e:
        print(f"✗ 转换失败: {e}")
        return False

if __name__ == '__main__':
    input_file = 'logo/icon.ico'
    output_file = 'logo/icon_converted.ico'
    
    if not os.path.exists(input_file):
        print(f"✗ 文件不存在: {input_file}")
    else:
        print(f"正在转换: {input_file} -> {output_file}")
        if convert_to_ico(input_file, output_file):
            print("\n提示：")
            print("1. 如果转换成功，可以替换原文件:")
            print("   - 备份原文件: copy logo\\icon.ico logo\\icon.ico.bak")
            print("   - 替换文件: copy logo\\icon_converted.ico logo\\icon.ico")
            print("2. 然后重新运行 build.bat 进行打包")
