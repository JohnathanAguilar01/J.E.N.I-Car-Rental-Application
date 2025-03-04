from back_end.car_rental import CarRentalService as cr
from database.main_database import initialize_database
from tunnel import SSHTunnel

class api:
    '''
    A class that is used to set up an api object to connect the back end to the front end.
    '''
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(api, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        '''
        initializes the mysql info and the car rental object from the back end.
        '''
        if not hasattr(self, 'initialized'):
            # Mark that initialization is complete
            self.initialized = True              

            # Making a ssh tunnel
            # self.tunnel = SSHTunnel()

            # Need username and password at the beginning
            self.username = 'admin'
            self.password = 'jenipassword'
            self.host = '127.0.0.1' 
            self.port = 3307
            # Needs to happen every single time, this is how the connection
            # to MySQL is initiated
            
            # initialize_database(self.host, self.port, self.username, self.password)
            self.car_rental_obj = cr(self.host, self.port, self.username, self.password)
            
            self.car_rental_obj.connect_to_mysql()
