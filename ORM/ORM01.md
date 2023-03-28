# TypeError: Object of type datetime is not JSON serializable

这个错误是因为datetime对象不能直接序列化为JSON字符串。您需要使用一个自定义的JSON编码器来将datetime对象转换为可序列化的类型。以下是一个例子：

```
import json
from datetime import datetime

from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker

# 创建Session类
from ORM_Da import Exposure, engineORM

Session = sessionmaker(bind=engineORM)

# 创建Session对象
session = Session()

# 自定义JSON编码器类
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

# 构建查询语句
query = session.query(Exposure).filter(
    and_(
        Exposure.imagetyp != None,
        Exposure.obs_date >= '20230327',
        Exposure.obs_date < '20230329'
    )
).distinct(Exposure.imagetyp)

# 执行查询并获取结果
results = query.all()

# 将结果转换为字典列表
result_dict_list = [row.__dict__ for row in results]

# 去掉'_sa_instance_state'键
for result_dict in result_dict_list:
    result_dict.pop('_sa_instance_state', None)

# 将字典列表转换为JSON字符串
json_string = json.dumps(result_dict_list, cls=CustomJSONEncoder, indent=4)

# 输出JSON字符串
print(json_string)
```

在这个例子中，我们首先创建了一个Session类，并通过调用query()方法和传递表对象来构建查询语句。我们使用filter()方法将多个条件组合在一起，并使用distinct()方法去重。然后，我们使用all()方法来执行查询，并获取所有结果。接下来，我们遍历结果并将它们转换为字典格式，并删除每个字典中的'_sa_instance_state'键。最后，我们定义了一个自定义的JSON编码器类，并使用json.dumps()函数将字典列表转换为JSON字符串，并使用cls参数指定自定义的JSON编码器类。