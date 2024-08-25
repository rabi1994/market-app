ROLE_CHOICES = [
        ('regular', 'Regular User'),
        ('business', 'Business Account'),
        ('delivery', 'Delivery User'),
    ]

DELIVERY_STATUS_CHOICES = [
   ('available', 'Available'),
        ('busy', 'Busy'),
        ('offline', 'Offline'),
]

DELIVERY_TYPE_CHOICES =  [
        ('standard', 'Standard'),
        ('scheduled', 'Scheduled'),
        ('same_day', 'Same-Day'),
    ]

DELIVERY_METHOD = [
    ('TA','TakeAway'),
    ('DE','Delivery')
]
PAYMENT_METHOD = [
    ('CA','Cash'),
    ('CC','Credit Card')
]