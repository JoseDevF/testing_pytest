class BankAPI:
    def authenticate(self, user, password):
        #Supongamos que realiza una autenticación real
        assert True


    def get_balance(self, account_id):
        # Supongamos que obtiene el balance de una cuenta de manera costosa
        pass



class BankAccount:
    def __init__(self, account_id, api):
        self.account_id =account_id
        self.api = api
        self._balance = None

    @property
    def balance(self):
        if self._balance is None:
            self._balance = self.api.get_balance(self.account_id)
        return self._balance


    def authenticate_get_balance(self, user, password):
        if self.api.authenticate(user, password):
            return self.balance
        else:
            raise PermissionError("Autenticación falló")


