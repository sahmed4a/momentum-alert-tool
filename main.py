
from datetime import datetime

def check_momentum(price, average_volume, current_volume):
    if average_volume <= 0:
        return False

    volume_ratio = current_volume / average_volume

    return price > 0 and volume_ratio >= 2.0


def main():
    print("Indian High-Volume Momentum Alert Tool")
    print("Market: NSE + BSE")
    print("Status: Setup test")
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Example test data only — not live market data.
    price = 500
    average_volume = 10000
    current_volume = 25000

    if check_momentum(price, average_volume, current_volume):
        print("TEST ALERT: High volume detected")
        print("Example price:", price)
    else:
        print("No momentum detected")


if __name__ == "__main__":
    main()
  
from datetime import datetime

def analyze_volume(price, average_volume, current_volume):
    if price <= 0 or average_volume <= 0 or current_volume < 0:
        return {"alert": False, "reason": "Invalid input"}

    ratio = current_volume / average_volume
    alert = ratio >= 2.0

    return {
        "alert": alert,
        "price": price,
        "average_volume": average_volume,
        "current_volume": current_volume,
        "volume_ratio": round(ratio, 2)
    }

def main():
    print("HIGH-VOLUME MOMENTUM SCANNER")
    print("Market: NSE + BSE")
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Sample values only; not live market data
    result = analyze_volume(
        price=500,
        average_volume=10000,
        current_volume=30000
    )

    print("Example price:", result["price"])
    print("Volume multiple:", result["volume_ratio"], "x")

    if result["alert"]:
        print("ALERT: High volume detected")
    else:
        print("No high-volume alert")

if __name__ == "__main__":
    main()

