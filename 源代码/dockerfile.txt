# 将官方 Python 运行时用作父镜像
FROM python:server
# 定义变量
ENV DIR_WEBAPP /usr/local/Server/
# 将工作目录设置为
WORKDIR $DIR_WEBAPP
# 将当前目录内容复制容器中
ADD ./server.py server.py
#ADD ./requirements.txt requirements.txt
# 暴露接口
EXPOSE 8401
# 安装 requirements.txt 中指定的任何所需软件包
#RUN #pip install -r requirements.txt
# 在容器启动时运行 tset.py
CMD ["python", "./server.py"]
