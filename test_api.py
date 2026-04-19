import requests
import pytest

# 使用国内可访问的测试接口（JSONPlaceholder）
BASE_URL = "https://jsonplaceholder.typicode.com"

class TestAPI:
    
    # 测试1：获取所有帖子，返回200
    def test_get_posts_returns_200(self):
        response = requests.get(f"{BASE_URL}/posts")
        assert response.status_code == 200
        print("✓ 获取帖子列表成功")
    
    # 测试2：返回数据是列表格式
    def test_get_posts_returns_list(self):
        response = requests.get(f"{BASE_URL}/posts")
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        print(f"✓ 返回 {len(data)} 条帖子数据")
    
    # 测试3：获取单个帖子，验证字段存在
    def test_get_single_post_has_fields(self):
        response = requests.get(f"{BASE_URL}/posts/1")
        data = response.json()
        assert "id" in data
        assert "title" in data
        assert "body" in data
        assert "userId" in data
        print("✓ 帖子包含 id, title, body, userId 字段")
    
    # 测试4：创建新帖子（POST请求）
    def test_create_post(self):
        new_post = {
            "title": "测试标题",
            "body": "这是测试内容",
            "userId": 1
        }
        response = requests.post(f"{BASE_URL}/posts", json=new_post)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "测试标题"
        print("✓ 创建新帖子成功")
    
    # 测试5：访问不存在的资源，返回404
    def test_not_found_returns_404(self):
        response = requests.get(f"{BASE_URL}/posts/99999")
        assert response.status_code == 404
        print("✓ 不存在的资源返回404")
    
    # 测试6：超时处理
    def test_response_within_timeout(self):
        response = requests.get(f"{BASE_URL}/posts", timeout=5)
        assert response.status_code == 200
        print("✓ 接口在5秒内响应")