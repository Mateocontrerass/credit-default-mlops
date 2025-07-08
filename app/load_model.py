import pickle


def load_model(path="models/model_lr.pkl"):
    with open(path, "rb") as f:
        model = pickle.load(f)

    return model
