class Stock:
    def __init__(self, ticker, company_name, current_price, change_percent, volume):
        self._ticker = ticker
        self._company_name = company_name
        self._current_price = current_price
        self._change_percent = change_percent
        self._volume = volume

    # Getter and Setter for ticker
    @property
    def ticker(self):
        return self._ticker

    @ticker.setter
    def ticker(self, value):
        self._ticker = value

    # Getter and Setter for company_name
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value

    # Getter and Setter for current_price
    @property
    def current_price(self):
        return self._current_price

    @current_price.setter
    def current_price(self, value):
        self._current_price = value

    # Getter and Setter for change_percent
    @property
    def change_percent(self):
        return self._change_percent

    @change_percent.setter
    def change_percent(self, value):
        self._change_percent = value

    # Getter and Setter for volume
    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value
