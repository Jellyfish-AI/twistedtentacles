from models.models import Company, Product, User

users = {
    'alice@robot.com': User(1, 'Alice', 'alice@robot.com'),
    'bob@robot.com': User(2, 'Bob', 'bob@robot.com'),
    'charlie@robot.com': User(3, 'Charlie', 'charlie@robot.com'),
    'alice@robot_cloud.com': User(4, 'Alice', 'alice@robot_cloud.com'),
    'bob@robot_cloud.com': User(5, 'Bob', 'bob@robot_cloud.com'),
    'charlie@robot_cloud.com': User(6, 'Charlie', 'charlie@robot_cloud.com'),
    'grace@cupcakefactory.com': User(7, 'Grace', 'grace@cupcakefactory.com'),
    'heidi@cupcakefactory.com': User(8, 'Heidi', 'heidi@cupcakefactory.com'),
    'ivan@cupcakefactory.com': User(9, 'Ivan', 'ivan@cupcakefactory.com'),
    'judy@aiinnovation.com': User(10, 'Judy', 'judy@aiinnovation.com'),
    'mallory@aiinnovation.com': User(11, 'Mallory', 'mallory@aiinnovation.com'),
    'niaj@aiinnovation.com': User(12, 'Niaj', 'niaj@aiinnovation.com'),
    'olivia@acmeconcrete.com': User(13, 'Olivia', 'olivia@acmeconcrete.com'),
    'peggy@acmeconcrete.com': User(14, 'Peggy', 'peggy@acmeconcrete.com'),
    'sybil@acmeconcrete.com': User(15, 'Sybil', 'sybil@acmeconcrete.com')
}

companies = {
    1: Company(1, 'robot', 'Robot Inc.', 150000, '1234 Robot St.', users['charlie@robot.com']),
    2: Company(2, 'robot_cloud', 'Robot Inc.', 150000, '1234 Robot St.', users['charlie@robot_cloud.com']),
    3: Company(3, 'cupcake_factory', 'Cupcake Factory', 200000, '5678 Cupcake Ave.', users['grace@cupcakefactory.com']),
    4: Company(4, 'ai_innovation', 'AI Innovation', 300000, '9101 AI Blvd.', users['mallory@aiinnovation.com']),
    5: Company(5, 'acme_concrete', 'Acme Concrete', 72500, '1122 Concrete Rd.', users['peggy@acmeconcrete.com'])
}

products = {
    1: Product(1, 'Widget', 'A basic widget', 20),
    2: Product(2, 'Gadget', 'A useful gadget', 30),
    3: Product(3, 'Doodad', 'A fancy doodad', 10),
    4: Product(4, 'Thingamajig', 'An advanced thingamajig', 50),
    5: Product(5, 'Whatchamacallit', 'A versatile whatchamacallit', 100)
}