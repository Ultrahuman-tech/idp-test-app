from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="IDP Test App")

@app.get("/healthz")
def health():
    return {"status": "ok", "app": "idp-test-app"}

@app.get("/", response_class=HTMLResponse)
def root():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IDP Test App</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background: #0f1117; color: #e2e8f0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; min-height: 100vh; display: flex; align-items: center; justify-content: center; }
        .card { background: #1a1d27; border: 1px solid #2a2d3a; border-radius: 16px; padding: 48px; max-width: 480px; text-align: center; }
        .badge { display: inline-block; background: #6366f1; color: white; font-size: 12px; font-weight: 700; padding: 4px 12px; border-radius: 6px; margin-bottom: 24px; letter-spacing: 1px; }
        h1 { font-size: 28px; margin-bottom: 8px; }
        .sub { color: #94a3b8; font-size: 14px; margin-bottom: 32px; }
        .status { display: flex; gap: 16px; justify-content: center; margin-bottom: 32px; }
        .status-item { background: #21242f; border: 1px solid #2a2d3a; border-radius: 12px; padding: 16px 24px; }
        .status-dot { width: 8px; height: 8px; background: #10b981; border-radius: 50%; display: inline-block; margin-right: 6px; }
        .status-label { color: #94a3b8; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; }
        .status-value { font-size: 18px; font-weight: 600; margin-top: 4px; }
        .info { color: #64748b; font-size: 13px; line-height: 1.6; }
        .info code { background: #21242f; padding: 2px 8px; border-radius: 4px; font-size: 12px; color: #a78bfa; }
        .footer { margin-top: 32px; color: #475569; font-size: 12px; }
    </style>
</head>
<body>
    <div class="card">
        <div class="badge">PRODUCTION</div>
        <h1>IDP Test App</h1>
        <p class="sub">Deployed end-to-end via UH Platform IDP</p>
        <div class="status">
            <div class="status-item">
                <div class="status-label"><span class="status-dot"></span>Status</div>
                <div class="status-value">Running</div>
            </div>
            <div class="status-item">
                <div class="status-label">Cluster</div>
                <div class="status-value">uh-prod-app</div>
            </div>
        </div>
        <div class="info">
            Onboarded automatically via IDP &mdash; Terraform created ECR, IRSA, ArgoCD, GitHub Actions, DNS, and K8s secrets. Zero manual steps.
        </div>
        <div class="footer">
            <code>/healthz</code> &middot; Port 8000 &middot; arm64
        </div>
    </div>
</body>
</html>"""
