# Generated by Django 4.1.1 on 2022-09-12 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
            insert into shop_good (id, name) values (1, 'Apple');
            insert into shop_good (id, name) values (2, 'Bread');
            insert into shop_good (id, name) values (3, 'Chicken');
            insert into shop_good (id, name) values (4, 'Flour');
            insert into shop_good (id, name) values (5, 'Chocolate');
        ""","""
            delete from shop_good
            where id <= 5;
        """)
    ]

