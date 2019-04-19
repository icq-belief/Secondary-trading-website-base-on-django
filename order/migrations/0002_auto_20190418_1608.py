# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-18 08:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('good', '0002_auto_20190418_1608'),
        ('order', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_buyer', to=settings.AUTH_USER_MODEL, verbose_name='买家'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Delivery', verbose_name='快递'),
        ),
        migrations.AddField(
            model_name='order',
            name='good',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='good.Good', verbose_name='订单对应商品'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_status', to='order.OrderStatusAndBillStatus', verbose_name='订单状态'),
        ),
        migrations.AddField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_seller', to=settings.AUTH_USER_MODEL, verbose_name='卖家'),
        ),
    ]