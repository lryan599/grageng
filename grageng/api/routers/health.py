from fastapi import APIRouter

# 创建一个 APIRouter 实例
router = APIRouter()


@router.get("/health")
async def health():
    return {"status": "ok"}
