"""
ACPs 智能体互联网实训营 - 个人代码提交

Author: Aurora
Date: 2026-04-24
Description: 实现 ACPs 协议中智能体互联的核心交互模型
"""

from datetime import datetime
from typing import Dict, List


class Agent:
    """智能体类 - 模拟 ACPs 协议中的基本智能体单元"""
    
    def __init__(self, name: str, capabilities: List[str]):
        self.name = name
        self.capabilities = capabilities
        self.message_history: List[Dict] = []
        self.status = "online"
        self.created_at = datetime.now()
    
    def send_message(self, target: 'Agent', content: str) -> Dict:
        """ACPs 核心功能：智能体间消息发送"""
        message = {
            "from": self.name,
            "to": target.name,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "protocol": "ACPs/1.0"
        }
        target.receive_message(message)
        self.message_history.append(message)
        return message
    
    def receive_message(self, message: Dict) -> None:
        """接收并记录消息"""
        self.message_history.append(message)
        print(f"[{self.name}] 收到来自 {message['from']} 的消息: {message['content']}")
    
    def get_status(self) -> Dict:
        """ACPs 标准接口：返回智能体状态"""
        return {
            "agent_name": self.name,
            "status": self.status,
            "capabilities": self.capabilities,
            "message_count": len(self.message_history),
            "protocol_version": "ACPs/1.0",
            "online_since": self.created_at.isoformat()
        }


def main():
    """演示 ACPs 智能体互联通信流程"""
    print("=" * 50)
    print("ACPs 智能体互联协议 - 基础交互演示")
    print("=" * 50 + "\n")
    
    # 创建两个智能体
    agent_a = Agent("Agent-Alice", ["send", "receive", "query"])
    agent_b = Agent("Agent-Bob", ["send", "receive", "query"])
    
    # 模拟互联通信
    print("📡 智能体互联通信中...\n")
    agent_a.send_message(agent_b, "Hello Bob，ACPs 连接已建立")
    agent_b.send_message(agent_a, "Hello Alice，协议互通成功")
    
    # 输出状态
    print("\n" + "=" * 50)
    print("智能体最终状态：")
    print(f"\n{agent_a.get_status()}")
    print(f"\n{agent_b.get_status()}")
    print("\n✅ ACPs 智能体互联演示完成")


if __name__ == "__main__":
    main()
