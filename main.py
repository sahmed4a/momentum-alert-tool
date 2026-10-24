
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
  
