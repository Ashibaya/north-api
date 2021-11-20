from sqlalchemy import create_engine, select
from navigation.nav.models.dicts import Base

engine_lite = create_engine('sqlite:///north.db')
engine_cloud = create_engine(
    'postgresql://bbpcwcvyjazdcm:ff8df7bba28207eb19ab3f814f9dee7785b96e01fd62b2def45c8cf3ab173340@ec2-54-210-226-209.compute-1.amazonaws.com:5432/d6d55r1q43igua')

with engine_lite.connect() as conn_lite:
    with engine_cloud.connect() as conn_cloud:
        for table in Base.metadata.sorted_tables:
            if table in ['orgs', 'regions', 'rivals', 'units', 'boats', 'cargos', 'localities', 'points', 'storages']:
                continue
            data = [dict(row) for row in conn_lite.execute(select(table.c))]
            conn_cloud.execute(table.insert().values(data))
