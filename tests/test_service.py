from app.services.receipt_service import ReceiptService
from datetime import date,time
from app.models.item import Item

import pytest

receipt_service = ReceiptService()

@pytest.mark.parametrize("retailer,expected",
                         [("M&M Corner Market",14),("M-M Corner  Market&123",17),
                          ("",0)])
def test_points_for_retailer_name(retailer,expected):
    assert receipt_service.points_for_retailer_name(retailer) == expected


@pytest.mark.parametrize("total,expected",
                         [(17,75),(17.16,0),(17.25,25),(0,75)])
def test_points_for_total(total,expected):
    assert receipt_service.points_for_total(total) == expected

@pytest.mark.parametrize("purchase_date,expected",
                         [(date(2025,5,29),6),(date(2025,5,28),0)])
def test_points_for_purchase_date(purchase_date,expected):
    assert receipt_service.points_for_purchase_date(purchase_date) == expected


@pytest.mark.parametrize("purchase_time,expected",
                         [(time(14,0),0),(time(16,0),0),(time(15,0),10),(time(13,0),0),(time(17,0),0)])
def test_points_for_purchase_time(purchase_time,expected):
    assert receipt_service.points_for_purchase_time(purchase_time) == expected


@pytest.mark.parametrize("items,expected",
                         [([Item("   Klarbrunn 12-PK 12 FL OZ  ",12.00),
                            Item("Emils Cheese Pizza",12.25)],11),
                            ([],0)])
def test_points_for_items(items,expected):
    assert receipt_service.points_for_items(items) == expected


