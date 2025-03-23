import asyncio
import logging
import os
from contextlib import asynccontextmanager

import dotenv
import uvicorn
from fastapi import FastAPI
from utils.log import setup_logger

from grageng.api.routers import health_router

dotenv.load_dotenv()
setup_logger()

logger = logging.getLogger("grageng")
WORKERS = os.getenv("UVICORN_WORKERS", 2)


# 定义 lifespan 上下文管理器
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 应用启动前的异步操作
    await asyncio.sleep(1)
    # 使用自定义日志记录器记录启动信息
    logger.info("Application is starting.")
    try:
        yield
    finally:
        # 应用关闭后的异步操作
        await asyncio.sleep(1)
        # 使用自定义日志记录器记录关闭信息
        logger.info("Application is shutting down.")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    # 使用自定义日志记录器记录请求信息
    logger.info("Received a request to the root endpoint.")
    return {"Hello": "World"}


app.include_router(health_router)


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True, log_config=None)
