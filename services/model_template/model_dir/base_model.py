class BaseModel:
    def predict(self):
        raise NotImplementedError('You need to implement predict for use in the orchestration')

    def fit(self):
        raise NotImplementedError('You need to implement fit for use in the orchestration')

    def save(self):
        raise NotImplementedError('You need to implement save for use in the orchestration')

    def load(self):
        raise NotImplementedError('You need to implement load for use in the orchestration')
