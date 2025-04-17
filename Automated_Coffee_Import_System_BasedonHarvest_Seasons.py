
#Region Abstraction Example
# Coffee beans are imported based on harvest seasons:
# - Columbia (Apr-Jul: months 4-7)
# - Sumatra (Aug-Nov: months 8-11)
# - South Africa (Jan, Feb, Dec: months 1, 2, 12)
# - No import in March (month 3)

from abc import ABC, abstractmethod

class BaseService(ABC):
    @abstractmethod
    def ship_from(self) -> str: pass


class SumatraService(BaseService):
    def ship_from(self) -> str:
        return 'importing coffee from Sumatra'

class ColumbiaService(BaseService):
    def ship_from(self) -> str:
        return 'importing coffee from Columbia'

class SouthAfricaService(BaseService):
    def ship_from(self) -> str:
        return 'importing coffee from SouthAfrica'

class NoShipment(BaseService):
    def ship_from(self) -> str:
        return 'No shipment this month'

class Shipment:
    @staticmethod
    def shipment_method(month: int) -> BaseService:
        if 4 <= month <= 7:
            return ColumbiaService()
        elif 8 < month <= 11:
            return SumatraService()
        elif month in [1, 2, 12]:
            return SouthAfricaService()
        elif month == 3:
            return NoShipment()
        else:
            raise ValueError('Month must be between 1 and 12.')

def main():
    try:
        month = int(input('Enter the import month (1-12): '))
        service = Shipment.shipment_method(month)
        print(service.ship_from())
    except ValueError as e:
        print(f'Error: {e}')

main()
