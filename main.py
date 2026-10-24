
from datetime import datetime

def analyze_volume(price, average_volume, current_volume):
    if price <= 0 or average_volume <= 0 or current_volume < 0:
        return None

    ratio = current_volume / average_volume

    return {
        "price": price,
        "volume_ratio": round(ratio, 2),
        "alert": ratio >= 2.0
    }

def main():
    print("INDIAN HIGH-VOLUME MOMENTUM SCANNER")
    print("Market: NSE + BSE")
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # TEST DATA ONLY - not live market data
    result = analyze_volume(
        price=500,
        average_volume=10000,
        current_volume=30000
    )

    if result is None:
        print("Invalid test data")
        return

    print("Example price:", result["price"])
    print("Volume multiple:", result["volume_ratio"], "x")

    if result["alert"]:
        print("ALERT: High volume detected")
    else:
        print("No high-volume alert")

if __name__ == "__main__":
    main()
