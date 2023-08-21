# quickdate
快捷处理日期的Python库，支持从字符串解析日期，灵活实现加减日、周、月、年、时、分、秒的时间操作

# 如何安装？
```shell
pip install quickdate
```

# 如何使用
qucickdate默认以今天的起点，开始定位日期，当然你也可以使用DateLocate.parse方法，从字符串解析一个日期，并以此为起点

支持的主要函数是 `add` 函数，可以动态传入 days、weeks、months、years、hours、minutes、seconds参数，并返回为 DateLocate对象本身

这意味着，可以链式定位日期，更为方便快捷

```python
>>> from quickdate.quickdate import DateLocate
>>> DateLocate().format("%Y-%m-%d")
2023-08-21
```

```python
>>> from quickdate.quickdate import DateLocate
>>> DateLocate.parse('20230821').format("%Y-%m-%d")
2023-08-21
```

其中， parse 函数还支持以下日期时间格式（不限于）
```python
>>> DateLocate.parse('22nd,July,2009').format("%Y-%m-%d")
2009-07-22
>>> DateLocate.parse('2018-04-20').format("%Y-%m-%d")
2018-04-20
>>> DateLocate.parse('2018').format("%Y-%m-%d")
2018-08-21
>>> DateLocate.parse('5,').format("%Y-%m-%d")
2023-08-05
>>> DateLocate.parse('9:10:8').format("%Y-%m-%d %H:%M:%S")
2023-08-21 09:10:08
>>> DateLocate.parse('02/11/2016').format("%Y-%m-%d %H:%M:%S")
2016-02-11 00:00:00
```

以下，将以今天为起点，说明 quickdate 库的用法
```python
# 按日定位日期 
>>> DateLocate().format("%Y-%m-%d")
2023-08-21
>>> DateLocate().add(days=-1).format("%Y-%m-%d")
2023-08-20
# 按周定位日期 
>>> DateLocate().add(weeks=-1).format("%Y-%m-%d")
2023-08-14
# 按月定位日期 
>>> DateLocate().add(months=-1).format("%Y-%m-%d")
2023-07-21
# 特别地，若当天为本月最后一天，获取上月日期时，会较正为准确上月最后一天的日期 
>>> DateLocate.parse("2023-03-31").add(months=-1).format("%Y-%m-%d")
2023-02-28
# 按年定位日期 
>>> DateLocate().add(years=-1).format("%Y-%m-%d")
2022-08-21
```

定位日期的方式，除了以上传一个参数以外，还可以复合传多个参数（但同一个参数仅能传一次）
```python
>>> DateLocate().add(weeks=-1, days=2, months=-2, years=-1).format("%Y-%m-%d")
2022-06-16
```

还可以进行链式定位
```python
>>> DateLocate().add(days=-1).add(weeks=-3).lastDay().format("%Y-%m-%d")
2023-07-31
```

可根据需求，直接设定年月日时分秒的值
```python
>>> DateLocate().year(2022).month(12).day(5).hour(10).format("%Y-%m-%d %H:%M:%S")
2022-12-05 10:41:47
```

通过 week 函数，可获取定位日期同周的周一至周日的日期 
```python
>>> DateLocate().week(5).format("%Y-%m-%d")
2023-08-25
```

通过 lastDay 函数，可获取定位日期当月最后一天的日期
```python
>>> DateLocate().lastDay().format("%Y-%m-%d")
2023-08-31
```

# 使用案例

获取当天日期 
```python
>>> from quickdate.quickdate import DateLocate
>>> DateLocate().format("%Y-%m-%d")
2023-08-21
```

获到昨天日期 
```python
>>> DateLocate().add(days=-1).format("%Y-%m-%d")
2023-08-20
```

获取上周三的日期 
```python
>>> DateLocate().add(weeks=-1).week(3).format("%Y-%m-%d")
2023-08-16
```

获取去年今日对应月份的最后一天
```python
>>> DateLocate().add(years=-1).lastDay().format("%Y-%m-%d")
2022-08-31
```

获取上个月的1号
```python
>>> DateLocate().add(months=-1).day(1).format("%Y-%m-%d")
2023-07-01
```

获取上上周六的日期 
```python
>>> DateLocate().add(weeks=-2).week(6).format("%Y-%m-%d")
2023-08-12
```
