from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import time
from dotenv import load_dotenv
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print("Starting the blockchain application...")

        print("Started the application successfully....")
    except Exception as e:
        print(f"Error during starting the application {str(e)}")

    finally:
        print("Shutting the application")
        print("Shutdown complete")



app = FastAPI(lifespan=lifespan)


load_dotenv()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

