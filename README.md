# pytest-api-demo

## 项目简介
这是一个 API 接口自动化测试项目，使用 pytest + requests 对 JSONPlaceholder 免费测试 API 进行接口测试。

## 技术栈
- Python 3.14
- pytest（测试框架）
- requests（HTTP 客户端库）

## 测试覆盖
- ✅ GET 请求测试（获取帖子列表、单个帖子）
- ✅ POST 请求测试（创建新帖子）
- ✅ 状态码验证（200、201、404）
- ✅ 返回数据格式验证（JSON、列表、字段完整性）
- ✅ 异常场景测试（不存在的资源返回404）
- ✅ 超时处理测试

## 如何运行

### 1. 安装依赖
```bash
pip install pytest requests
