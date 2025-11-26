# CODE::RED Sentinel Configuration
# Rename this file to config.py before execution

# --- Exchange Settings ---
API_KEY = "YOUR_BINANCE_API_KEY"
API_SECRET = "YOUR_BINANCE_API_SECRET"

# --- Target Specs ---
# Format depends on exchange (e.g. BTC/USDT:USDT for Binance Futures)
SYMBOL = 'BTC/USDT' 

# --- Risk / Sizing ---
TRADE_SIZE = 0.005  # Base trade unit
MAX_POSITION = 0.02 # Hard cap
LEVERAGE = 5

# --- System Latency Targets ---
# Warning: Python execution may lag behind compiled OCaml modules.
LATENCY_TOLERANCE_MS = 50