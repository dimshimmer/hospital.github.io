# test.py
import yaml

# 读取 YAML 文件
with open('_config.yml', encoding='utf-8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

# 输出数据
for dept in data['doctors']:
    print(dept)

