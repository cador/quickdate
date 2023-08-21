# quickdate
快捷处理日期的Python库，支持从字符串解析日期，灵活实现加减日、周、月、年、时、分、秒的时间操作

# 如何安装？
```shell
pip install quickdate
```

# 如何使用
qucickdate默认可通过today对象，以今天的起点，开始定位日期，当然你也可以使用DateLocate.parse方法，从字符串解析一个日期，并以此为起点
```python
>>> from quickdate.quickdate import today
>>> today.format("%Y-%m-%d")
2023-08-21
```

```python
>>> from quickdate.quickdate import DateLocate
>>> DateLocate.parse('20230821').format("%Y-%m-%d")
```

# 使用案例

使用 today 获取当天日期 
```python
from quickdate.quickdate import today
today.format("%Y-%m-%d")
```

