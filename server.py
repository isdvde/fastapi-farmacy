import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app",
                host="farmacia.am",
                port=80,
                reload=True,
                log_level="debug")
