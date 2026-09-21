"""One call to OpenRouter. Key from /opt/secrets, never in the code.

    reply = ktor.ask("deepseek/deepseek-v4-pro-0813", prompt)
"""
import json
import subprocess
import time
import urllib.request

KEYFILE = "/opt/secrets/openrouter_api_key"


def key():
    try:
        return open(KEYFILE).read().strip()
    except PermissionError:
        return subprocess.check_output(["sudo", "cat", KEYFILE]).decode().strip()


def ask(model, prompt, temperature=0, tries=3):
    body = json.dumps({"model": model, "temperature": temperature,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    for i in range(tries):
        try:
            req = urllib.request.Request(
                "https://openrouter.ai/api/v1/chat/completions", data=body,
                headers={"Authorization": f"Bearer {key()}", "Content-Type": "application/json",
                         "HTTP-Referer": "https://oona13.com", "X-Title": "Rohonc tests"})
            r = json.load(urllib.request.urlopen(req, timeout=600))
            txt = r["choices"][0]["message"]["content"]
            if not isinstance(txt, str) or not txt.strip():
                raise RuntimeError("empty reply")   # thinking budget spent; try again
            return txt, r.get("usage", {})
        except Exception as e:
            if i == tries - 1:
                raise
            time.sleep(3 * (i + 1))
