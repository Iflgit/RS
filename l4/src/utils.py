def prefilter_items(data_train, take_n_popular=5000):
    # Оставим только 5000 самых популярных товаров
    popularity = data_train.groupby('item_id')['quantity'].sum().reset_index()
    popularity.rename(columns={'quantity': 'n_sold'}, inplace=True)
    top_popular = popularity.sort_values('n_sold', ascending=False).head(take_n_popular).item_id.tolist()
    #добавим, чтобы не потерять юзеров
    data_train.loc[~data_train['item_id'].isin(top_popular), 'item_id'] = 999999
    
    
    
    # Уберем самые популярные 
    
    # Уберем самые непопулряные 
    
    # Уберем товары, которые не продавались за последние 12 месяцев
    
    # Уберем не интересные для рекоммендаций категории (department)
    
    # Уберем слишком дешевые товары (на них не заработаем). 1 покупка из рассылок стоит 60 руб. 
    
    # Уберем слишком дорогие товарыs
    
    # ...
    
    return data_train
def postfilter_items():
    pass