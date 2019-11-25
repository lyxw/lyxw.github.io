---
layout: post
title:  "Windows下安装jupyter及增加kernel的方法"
date:   2019-11-25 13:25:30
categories: Windows jupyter python java php
permalink: /archivers/Windows下安装jupyter及增加kernel的方法
---

### 0x01 简介

Jupyter Notebook是一个开源的Web应用程序，允许创建和共享包含实时代码、方程式、可视化效果和叙述文本的文档，可以理解为加强版的网页交互式编译器。

![jupyterpreview.png](https://lyxw.github.io/images/jupyter/jupyterpreview.png)

### 0x02 安装jupyter

#### 1、首先需要安装python，建议选用最新的python3版本，安装完毕后设置好环境变量

下载地址： [https://www.python.org/downloads/windows](https://www.python.org/downloads/windows/)

![python_version.jpg](https://lyxw.github.io/images/jupyter/python_version.jpg)

#### 2、然后安装jupyter，安装过程可能会比较慢，等待执行完毕

```
pip3 install jupyter
```

![pip_install_jupyter.jpg](https://lyxw.github.io/images/jupyter/pip_install_jupyter.jpg)

### 0x03 使用jupyter

#### 1、在终端运行如下命令，会在默认浏览器中打开窗口

```
jupyter-notebook
```

![jupyter_run.jpg](https://lyxw.github.io/images/jupyter/jupyter_run.jpg)

![jupyter_browser.jpg](https://lyxw.github.io/images/jupyter/jupyter_browser.jpg)

#### 2、点击右上角，新建一个Python3项目

![jupyter_python3.jpg](https://lyxw.github.io/images/jupyter/jupyter_python3.jpg)

#### 3、新项目如下，其中每一行表示一个cell，代码在里边编写

![jupyter_cell.jpg](https://lyxw.github.io/images/jupyter/jupyter_cell.jpg)

#### 4、常用快捷键

- **Enter** : 本单元换行

- **Shift + Enter** : 运行本单元，选中下个单元

- **Ctrl + Enter** : 运行本单元

- **Alt + Enter** : 运行本单元，在其下插入新单元

### 0x04 安装java内核

#### 1、需要java版本不小于9，可使用java11

下载地址： [https://www.oracle.com/technetwork/java/javase/downloads/jdk11-downloads-5066655.html](https://www.oracle.com/technetwork/java/javase/downloads/jdk11-downloads-5066655.html)

#### 2、安装完毕后需配置好环境变量



#### 3、下载IJava

下载地址： [https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-1.3.0.zip](https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-1.3.0.zip)

#### 4、安装内核

```
python3 install.py --sys-prefix
```

#### 5、安装完毕



### 0x05 安装php内核

#### 1、需要php版本大于7.0，可使用7.2

下载地址： [https://windows.php.net/downloads/releases/php-7.2.25-Win32-VC15-x64.zip](https://windows.php.net/downloads/releases/php-7.2.25-Win32-VC15-x64.zip)

#### 2、安装完毕后需配置好环境变量



#### 3、安装composer，需要php启用openssl扩展

下载地址： [https://getcomposer.org/Composer-Setup.exe](https://getcomposer.org/Composer-Setup.exe)

#### 4、下载PHP-ZMQ扩展，解压到相应的位置，并在配置文件`php.ini`中添加

下载地址： [https://windows.php.net/downloads/pecl/releases/zmq/1.1.3/php_zmq-1.1.3-7.2-ts-vc15-x64.zip](https://windows.php.net/downloads/pecl/releases/zmq/1.1.3/php_zmq-1.1.3-7.2-ts-vc15-x64.zip)

#### 5、下载PHAR安装程序

下载地址： [https://litipk.github.io/Jupyter-PHP-Installer/dist/jupyter-php-installer.phar](https://litipk.github.io/Jupyter-PHP-Installer/dist/jupyter-php-installer.phar)

#### 6、安装内核，过程有点慢，`-vvv`可输出安装过程中的详细信息

```
php jupyter-php-installer.phar install -vvv
```

#### 7、安装完毕

