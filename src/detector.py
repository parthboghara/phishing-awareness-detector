import joblib
from features import extract_features

MODEL_PATH = "../model/phishing_model.pkl"

def main():
    try:
        model = joblib.load(MODEL_PATH)
    except FileNotFoundError:
        print("[-] Model not found. Please train the model first.")
        return

    print("=" * 60)
    print("🔐 Phishing Awareness Detector")
    print("=" * 60)

    while True:
        url = input("\nEnter URL (or 'exit'): ")
        if url.lower() == "exit":
            break

        prediction = model.predict([extract_features(url)])[0]
        print("⚠️ PHISHING URL DETECTED!" if prediction else "✅ Legitimate URL")

if __name__ == "__main__":
    main()
