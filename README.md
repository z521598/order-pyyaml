# order-pyyaml
## 功能：  
> 封装pyyaml用于“有序”解析/生成yaml  

## 背景：  
> 在使用pyyaml时发现，当由字典dump成yaml文件时，顺序会被打乱.  
> 如果将字典改成OrderDict有序“字典”，则在dump的时候生成的结构会带入OrderDict的信息  

## 说明：
1. demo.py: demo测试代码
2. yamlparser.py: 工具类  
