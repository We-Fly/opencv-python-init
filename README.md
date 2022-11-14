# opencv-python-init
自动配置python环境的初始工程

## 使用方法 Instructions

## 克隆本仓库

```bash
git clone https://github.com/We-Fly/opencv-python-init.git
# 通过https克隆

git clone git@github.com:We-Fly/opencv-python-init.git
# 通过ssh克隆
```

### 自动初始化 Auto setup

#### 方法1 method 1

cd到项目文件夹，在终端输入

```bash
python setup.py 
```

并回车运行，默认使用tuna镜像源下载所需软件包

如果你有代理服务器可以加上代理服务器地址，例如`python setup.py --proxy http://127.0.0.1:7890`

#### 方法2 method 2

cd到项目文件夹，在终端输入

```bash
pip install -r packages -i https://pypi.tuna.tsinghua.edu.cn/simple 
```

并回车运行，以使用tuna镜像源下载所需软件包

如果你有代理服务器可以加上代理服务器地址，例如`pip install -r packages --proxy http://127.0.0.1:7890`

## 运行程序

需要先安装和配置好Python环境，请参考[开飞机文档](https://we-fly.cd.al)

在终端里执行

```bash
conda activate your_conda_env_name
python demo.py
```

程序会显示开飞机图标，按任意按钮退出
