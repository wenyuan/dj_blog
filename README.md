# DJ Blog
> 基于django的开源博客系统。 </br>
> 包含一套个人博客应有的基本功能，可直接运行、部署、使用。 </br>
> 后期能很方便的进行UI个性化修改和功能扩展。 </br>

## 环境
* Linux
* Python 2.7或3.6

## 部署和运行方式
```
	Step1. gitclone https://github.com/winyuan/dj_blog.git</br>
	Step2. cd dj_blog
           pip install -r requirements.txt
           python manage.py makemigrations
           python manage.py migrate
           python manage.py compilemessages
           python manege.py createsuperuser
	Step3. python manage.py runserver
``` 

## 访问方式
* 前端页面：ip:8000
* 后台管理：ip:8000/admin

## 实现功能
* 博客编写
* 博客分类、tag、归档
* 站点地图
* rss

## 主要更新记录
* 2019.01.07
  * 部分重构，优化项目结构
* 2018.10.21
  * 提交代码
