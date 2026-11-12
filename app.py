from flask import Flask, render_template, request
from pathlib import Path
import json
import os

app = Flask(__name__)

OFFICIAL_TRACKER = "https://retrac.site/tracker"
SHOP_DATA = Path(__file__).with_name("shop_items.json")

def load_shop_items():
    """Load manually verified Retrac shop entries; never invent live stock."""
    try:
        data = json.loads(SHOP_DATA.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (OSError, json.JSONDecodeError):
        return []

@app.route("/")
def home():
    query = request.args.get("q", "").strip()
    # Retrac's public search interface is the source of truth.
    # This project does not invent player statistics or scrape private data.
    return render_template("index.html", query=query, official_tracker=OFFICIAL_TRACKER)

@app.route("/shop")
def shop():
    items = load_shop_items()
    return render_template("shop.html", items=items)

@app.route("/search")
def search():
    query = request.args.get("q", "").strip()
    if not query:
        return render_template("index.html", query="", official_tracker=OFFICIAL_TRACKER)
    return render_template(
        "index.html",
        query=query,
        official_tracker=OFFICIAL_TRACKER,
        searched=True
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
