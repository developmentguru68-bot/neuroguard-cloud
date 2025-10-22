def predict_outcome(data_bytes):
    # Beispielhafte Dummy-Logik (ersetzbar durch echtes ML)
    if len(data_bytes) % 2 == 0:
        return "Low risk (mRS ≤ 3)"
    else:
        return "High risk (mRS ≥ 6)"
