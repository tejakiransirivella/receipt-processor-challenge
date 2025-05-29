from dataclasses import dataclass
from typing import List
from app.models.item import Item
from datetime import date, datetime,time

@dataclass(slots=True)
class Receipt:
   retailer : str
   purchase_date: date
   purchase_time : time
   items : List[Item]
   total : float

   @staticmethod
   def create_receipt(receipt_json:str):
      purchase_date = datetime.strptime(receipt_json['purchaseDate'],"%Y-%m-%d").date()
      purchase_time = datetime.strptime(receipt_json['purchaseTime'],"%H:%M").time()
      total = float(receipt_json["total"])
      items_json:List = receipt_json['items']
      items = []
      for item_json in items_json:
         item = Item.create_item(item_json)
         items.append(item)
      return Receipt(receipt_json['retailer'],purchase_date,purchase_time,items,total)
   
if __name__ == "__main__":
   receipt_json = {
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },{
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    },{
      "shortDescription": "Knorr Creamy Chicken",
      "price": "1.26"
    },{
      "shortDescription": "Doritos Nacho Cheese",
      "price": "3.35"
    },{
      "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
      "price": "12.00"
    }
  ],
  "total": "35.35"
}
   
   receipt = Receipt.create_receipt(receipt_json)
   print(receipt)
