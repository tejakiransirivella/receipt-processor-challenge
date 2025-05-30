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