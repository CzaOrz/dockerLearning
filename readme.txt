docker pull python:3.6.8
docker build -t flask_app:1.0 .
docker run -d -p 8866:8866 flask_app:1.0 --name flask_container
docker commit flask_container flask_app:1.0  # -a 'CzaOrz' -m 'pip install flask', 从容器创建一个新的镜像。
docker save flask_app:1.0 -o flask_app.tar  # 一般使用 -o 指定输出文件，或者 > 也是可以的
docker load -i flask_app.tar  # 一般使用 -i 指定输入，或者 < 也是可以的
docker import flask_app.tar new_app:v1  # 和load类似

docker container prune  # 批量删除已停止容器

docker ps
docker ps -a
docker rm ${容器id}  # -f 表示强制删除
docker images
docker rmi ${镜像id}  # -f 表示强制删除

docker exec -it ${容器id} bash  # 在运行的容器中执行命令

docker build -t ${镜像name} ${路径，通常为 . 即可}

docker run -d -p 8866:8866 -it ${镜像name}
# -d 表示后台运行
# -p 表示指定外部端口和内部的映射端口
docker commit ${container} ${image}

docker start ${container id}  # 开启容器
docker stop ${container id}  # 停止容器
docker kill -s KILL ${container id}  # 会强制杀掉容器
docker restart ${container id}  # 重启容器

docker pull python:3.6.8  # 拉取镜像

docker save ${image} > name.tar  # 将镜像压缩打包至tar
docker load < name.tar  # 从tar压缩包中加载镜像

docker pause  # 暂停容器的进程
docker unpause  # 回复容器的进程
Docker create --name myrunoob nginx:latest  # 创建一个新的容器不启动

docker ps -a -q  # 列出所有创建的容器ID
docker top ${container-id}  # 查看正在运行容器的进程信息
docker port ${container-id}  # 查看正在运行容器的端口信息
docker cp ./workplace ${container-id}:/workplace/server  # 将主机workplace下的资源拷贝到容器的路径下
docker cp ${container-id}:/workplace/server ./workplace  # 将容器的路径下的资源拷贝到主机workplace下
docker diff ${container-id}  # 查看容器文件结构的更改

docker login -u:登陆的用户名 -p:登陆的密码  #  登陆到一个Docker镜像仓库，如果未指定镜像仓库地址，默认为官方仓库 Docker Hub
docker logout  # 登出一
docker push ${image-id}  # 将本地的镜像上传到镜像仓库,要先登陆到镜像仓库



##### Dockerfile

FROM python:3.6.8  # 引用基础镜像

ARG temp_key[=default_value]  # 声明变量
ENV env_key=value  # 声明环境变量

COPY src dst  # 一个是当前路径，一个是虚拟环境的路径
ADD src dst  # add可以自动解压tar文件，也可以远程拉取url
RUN command1 && command2

WORKDIR ./  # 设置工作目录

ENTRYPOINT ["python"]  # 指定容器启动时默认执行的命令
CMD ["test.py"]  # 指定容器启动时默认命令的默认参数

MAINTAINER 指定维护者信息
VOLUME 创建数据挂载点


##### docker-compose
docker-compose –f docker-compose.yml –d up
运行多个容器，需要多次run来执行
对于整个项目而言，可以直接编写一个yml文件，可实现自动部署整个项目


##### k8s
kubectl get pods
kubectl get nodes
kubectl create -f kubernetes-dashboard.yaml












