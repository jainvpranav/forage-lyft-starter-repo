class spindler:
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date

    def battery_should_be_serviced(self):
        if self.last_service_date > 2:
            return True
        else:
            return False