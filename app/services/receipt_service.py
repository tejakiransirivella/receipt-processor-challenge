from dataclasses import dataclass
from typing import List
from app.models.receipt import Receipt
from app.models.item import Item
from datetime import date, time, datetime

import math

@dataclass(slots=True)
class ReceiptService:

    receipt: Receipt = None

    def points_for_retailer_name(self,retailer:str) -> int:
        points = 0
        for character in retailer:
            if character.isalnum():
                points += 1
        return points
            

    def points_for_total(self,total:float) -> int:
        points = 0
        if total.is_integer():
            points += 50
        if (total/0.25).is_integer():
            points += 25
        return points

    def points_for_items(self, items:List[Item]) -> int :
        points = 5*(len(items)//2)
        for item in items:
            item_length = len(item.short_description.strip())
            if item_length%3 == 0:
                points += math.ceil(item.price*0.2)
        return points

    def points_for_purchase_date(self,purchase_date:date) -> int:
        points = 0
        if purchase_date.day%2 == 1:
            points += 6
        return points

    def points_for_purchase_time(self,purchase_time:time) -> int:
        points = 0
        start = datetime.strptime("14:00","%H:%M").time()
        end = datetime.strptime("16:00","%H:%M").time()

        if start < purchase_time < end:
            points += 10
        return points

    def calculate_total_points(self) -> int:
        points = 0
        points += self.points_for_retailer_name(self.receipt.retailer)
        points += self.points_for_total(self.receipt.total)
        points += self.points_for_purchase_date(self.receipt.purchase_date)
        points += self.points_for_purchase_time(self.receipt.purchase_time)
        points += self.points_for_items(self.receipt.items)
        return points