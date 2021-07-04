from DatabaseModel.OrderTabledbModel import OrderTable

def GetOrderTableData():
    orderTableData=OrderTable.query.all()
    for x in orderTableData:
        print(x.table_no)

    return