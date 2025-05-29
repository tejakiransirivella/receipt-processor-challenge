from dataclasses import dataclass

@dataclass(slots=True)
class Item:
    short_description : str
    price : float

    @staticmethod
    def create_item(item_json:str):
        item = Item(item_json['shortDescription'],float(item_json['price']))
        return item