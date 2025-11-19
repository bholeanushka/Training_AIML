from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from dotenv import load_dotenv
from typing import Optional,List
import os

from langgraph_workflow import workflow
from portfolio_workflow import portfolio_workflow # your compiled graph

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

app = FastAPI(title="Stock Insights Chatbot API")

# Mount static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="templates")

# In-memory chat history
chat_history = []


# Request schema
class QueryRequest(BaseModel):
    user_query: str


# Response schema
class QueryResponse(BaseModel):
    query: str
    stock_symbol: str
    stock_data: list | None
    chart_base64: Optional[str] = None
    news_summary: str | None
    insights: str | None
    sentiment_results: list | None

class StockInput(BaseModel):
    symbol: str
    quantity: int

class PortfolioRequest(BaseModel):
    portfolio: List[StockInput]
    risk: str   # e.g. "Low", "Moderate", "High"


# Home route
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """
    Render the home page using Jinja2Templates
    """
    return templates.TemplateResponse("index.html", {"request": request})


# Dashboard route
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    """
    Render the dashboard page using Jinja2Templates
    """
    return templates.TemplateResponse("dashboard.html", {"request": request})

# Portfolio route
@app.get("/portfolio", response_class=HTMLResponse)
def dashboard(request: Request):
    """
    Render the dashboard page using Jinja2Templates
    """
    return templates.TemplateResponse("portfolio.html", {"request": request})


@app.post("/query", response_model=QueryResponse)
def run_query(request: QueryRequest):
    """
    Endpoint to process a stock query and return insights.
    """
    try:
        result = workflow.invoke({"user_query": request.user_query})

        response = {
            "query": request.user_query,
            "stock_symbol": result.get("stock_symbol", "N/A"),
            "stock_data": result.get("stock_data", []),
            "news_summary": result.get("news_summary", ""),
            "sentiment_results": result.get("sentiment_results", []),
            "insights": result.get("insights", ""),
            "chart_base64": result.get("chart_base64", "")
        }

        chat_history.append(response)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/history")
def get_history():
    return {"history": chat_history}


@app.delete("/history")
def clear_history():
    chat_history.clear()
    return {"message": "Chat history cleared"}


@app.post("/portfolio-analysis")
def analyze_portfolio(request: PortfolioRequest):
    try:
        result = portfolio_workflow.invoke({
            "portfolio": [s.dict() for s in request.portfolio],
            "risk": request.risk
        })

        return {
            "portfolio": result.get("portfolio", []),
            "sector_breakdown": result.get("sector_breakdown", {}),
            "sector_chart_base64": result.get("sector_chart_base64", ""),
            "ai_insights": result.get("ai_insights", ""),
            "recommendations": result.get("recommendations", {})
        }
    except Exception as e:
        raise HTTPException(e)
