import math
import xlrd
import time

class KNN:
    def __init__(self):
        self.area = []
        self.floors = []
        self.market_demand = []
        self.age = []
        self.res_comm = []
        self.locality_rating=[]   ##
        self.prices = []

    # ecludean distance
    def ED(self,x1, x2, y1, y2, z1, z2, r1, r2, s1, s2,t1,t2):
        x = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2) + ((r1 - r2) ** 2) + ((s1 - s2) ** 2)+((t1 - t2) ** 2))  ##
        return x



    def KNN(self):
        distances = []

        input_area = int(input("Please enter the area of the property"))
        input_floors = int(input("Please enter the floors of the property"))
        input_demand = int(input("Please enter the demand rating of the property"))
        input_age = int(input("Please enter the age of the property"))
        input_res_or_comm = int(input("Please enter 0 for residential and 1 for commercial"))
        input_locality_rating=int(input("Please enter locality rating"))

        for i in range(1, len(self.area)):
            a = self.area[i]
            f = self.floors[i]
            dem = self.market_demand[i]
            age_ = self.age[i]
            res_comm = self.res_comm[i]
            locality_rating=self.locality_rating[i]

            result = self.ED(input_area, a, input_floors, f, input_demand, dem, input_age, age_, input_res_or_comm, res_comm,input_locality_rating,locality_rating)
            distances.append(result)
        print(distances)

        k=int(input("Please enter k value"))
        print("\nK nearest prices are: ")

        for i in range(0,k):
            print(self.prices[(distances.index(min(distances)))+1])
            distances.pop(distances.index(min(distances)))


        while True:
            time.sleep(10)



    def xlsx_reader(self):
        book = xlrd.open_workbook("Dataset.xlsx")
        sh = book.sheet_by_index(0)
        for col in range(sh.ncols):
            for row in range(sh.nrows):
                if col==0:
                    self.area.append(sh.cell_value(row,col))
                elif col==1:
                    self.floors.append(sh.cell_value(row,col))
                elif col==2:
                    self.market_demand.append(sh.cell_value(row,col))
                elif col==3:
                    self.age.append(sh.cell_value(row,col))
                elif col==4:
                    self.res_comm.append(sh.cell_value(row,col))
                elif col==5:
                    self.locality_rating.append(sh.cell_value(row,col))
                elif col==6:
                    self.prices.append(sh.cell_value(row,col))



if __name__ == '__main__':
    x=KNN()
    x.xlsx_reader()
    x.KNN()







