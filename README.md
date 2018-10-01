# myRedis
Redis的安装好基本使用
## 环境
1. Python 3.6
2. Django 2.0.7
3. django-redis 4.9.0
4. Mac

## Redis 安装 使用
1. 在本地配置Redis
> a. 官网下载
```
https://redis.io/
```
> b. 安装,进入解压的redis文件夹中，编译安装

```
cd redis-3.0.7
sudo make install
make test #测试 redis 是否能使用
```
>c .启动redis服务端,进入src文件夹后执行启动命令

```
cd src
./redis-server
```

>d. 启动redis客服端,新开个终端,进入到src文件夹,执行命令

```
./redis-cli
```
>e. redis的基本使用

```
# 插入数据
SET key value
# 查询数据
get key
```
## Redis在 Django 项目中的使用
>a. 开启 redis 服务端和客服端

>b. 在 setting.py 中配置 redis

```
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",  # 这里设定了本机的redis数据
        # "LOCATION": "redis://:passwordpassword@47.193.146.xxx:6379/0", # 如果redis设置密码的话，需要以这种格式host前面是密码
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```
>c. 引入 cache

```
from django.core.cache import cache
```

>d.添加数据

```
cache.set("key1","value11",100) 
	#	key1 : key 值
	#	value11 : value 值
	#	100 : 过期时间
```
>e. 查看数据

```
cache.get("key1")
```
>f. 查看过期时间
	
```
cache.ttl(“key1”)
	# 返回剩余的时间(秒)
	# 0代表已经过期
	# None 代表没有设置过期时间
```
>g. 删除redis 中key 对应的数据
		ca
```
che.delete("key1")
	模糊删除
	cache.delete_pattern("foo_*")
	>>	返回删除的数量
```

>h. 模糊搜索(使用通配符搜索的例子)
```
cache.keys("foo_*")
	>>	["foo_1", "foo_2"]
2.8以上的版本,可以使用iter_keys取代 keys, 返回一个迭代器
cache.iter_keys("foo_*")
	>>	<generator object algo at 0x7ffa9c2713a8>
	>>	next(cache.iter_keys("foo_*"))
	>>	"foo_1"
```









