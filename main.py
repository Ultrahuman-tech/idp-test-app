from fastapi import FastAPI

app = FastAPI(title="IDP Test App")

@app.get("/healthz")
def health():
    return {"status": "ok", "app": "idp-test-app"}

@app.get("/")
def root():
    return {"message": "Hello from IDP test app on prod!"}
