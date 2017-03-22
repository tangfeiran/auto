web 发布系统
===================================
    celery 异步调用 ansible playbook 执行任务
    自定义 playbook，实时显示日志

### 克隆
    git clone https://github.com/tangfeiran/auto.git
### 初始化数据库
     python manage.py makemigrations
     python manage.py migrate
### 启动站点（测试）
    python manage.py runserver 0.0.0.0:8000
### 启动celery worker
    celery -A auto worker -l info
### 测试url
    http://yourip:8000/send
### 错误
    AttributeError: 'Process' object has no attribute '_authkey'
    celery此报错，由于celery不支持 multiprocessing.Process
    暂时解决方法为修改ansible库文件 site-packages/ansible/executor/process/worker.py:
    增加 import billiard
    修改 class WorkerProcess(billiard.Process):