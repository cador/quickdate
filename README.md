# quickdate
快捷处理日期的Python库，支持从字符串解析日期，灵活实现加减日、周、月、年、时、分、秒的时间操作

# 如何安装？
```shell
pip install quickdate
```

# 如何使用
qucickdate默认以今天的起点，开始定位日期，当然你也可以使用DateLocate.parse方法，从字符串解析一个日期，并以此为起点
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

# 使用案例

使用 today 获取当天日期 
```python
from quickdate.quickdate import today
today.format("%Y-%m-%d")
```

