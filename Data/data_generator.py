from faker import Faker

class Data: 

    def __init__ (self, faker = Faker()) :
      self.faker = faker

    def data_generator(self):
        #dictionnary
        val ={} 

        for i in range(0, 10): 
            val[i]={} 
            bith_date = self.faker.date_of_birth()
            reques_date = self.faker.date_time_this_year(before_now=False, after_now=True, tzinfo=None)
            val[i]['lastname']= self.faker.last_name()
            val[i]['firstname']= self.faker.first_name() 
            val[i]['Birth Date']= bith_date.strftime("%d/%m/%Y") 
            val[i]['Request Date']= reques_date.strftime("%d/%m/%Y%H:%M:%S") 
            val[i]['Request Date']= reques_date.strftime("%d/%m/%Y%H:%M:%S") 
            val[i]['Request Date']= reques_date.strftime("%d/%m/%Y%H:%M:%S")
            val[i]['Generation Date']= reques_date.strftime("%d/%m/%Y%H:%M:%S")

        return val