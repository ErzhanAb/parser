# Import modules
from bs4 import BeautifulSoup


def get_main_info(soup: BeautifulSoup) -> dict:
    data = {}
    car_name = soup.find('div', class_='head-left').h1
    raised_added = soup.find('div', class_='subblock upped-at')
    views = soup.find('div', class_='subblock counters').find('span', class_='listing-icons views')
    likes = soup.find('div', class_='subblock counters').find('span', class_='listing-icons heart')
    comments = soup.find('div', class_='subblock counters').find('span', class_='listing-icons comments')
    if car_name:
        data['Brand'] = car_name.text.replace('Продажа ', '').strip()
    if raised_added:
        data['Updated'] = raised_added.text.strip().replace('\n                  \n\n                  ', ' - ')
    if views:
        data['Views'] = views.text.strip()
    if likes:
        data['Likes'] = likes.text.strip()
    if comments:
        data['Comments'] = comments.text.strip()
    return data


def get_price(soup: BeautifulSoup) -> dict:
    dollar = soup.find('div', class_='price-dollar')
    som = soup.find('div', class_='price-som')
    data = {}
    if dollar:
        data['Price in dollars'] = dollar.text.strip()
    if som:
        data['Price in soms'] = som.text.strip()
    return data


def get_user_info(soup: BeautifulSoup) -> dict:
    main_dir = soup.find('div', class_='personal-info details-phone-wrap clr')
    name = main_dir.find('span', class_='i-name')
    activity = main_dir.find('div', class_='i-counter')
    number = main_dir.find('div', class_='number')
    data = {}
    if name:
        data["Name"] = name.text.strip()
    if activity:
        data["Activity"] = activity.text.strip()
    if number:
        data["Phone number"] = number.text.strip()
    return data


def get_announcement_info(soup: BeautifulSoup) -> dict:
    main_dir = soup.find('div', class_='tab-pane fade in active')
    l = main_dir.find_all('div', class_='field-row clr')
    data = {}
    if len(l) > 0:
        for el in l:
            if el.find('div', class_='field-label') and el.find('div', class_='field-value'):
                data[el.find('div', class_='field-label').text] = el.find('div', class_='field-value').text.strip().replace('\n                          ', ' ').replace('\n                                                                          ', ' ').replace('/                                                 ', '/ ')
    return data


def get_equipment(soup: BeautifulSoup) -> dict:
    main_dir = soup.find('div', class_='configuration')
    data = {}
    if main_dir:
        names = main_dir.find_all('div', class_='name')
        values = main_dir.find_all('div', class_='value')
        for key, value in zip(names, values):
            list_of_values = [p.text.strip() for p in value.find_all('p')]
            data[key.text.strip()] = list_of_values
    return data


def get_all_info(soup: BeautifulSoup) -> dict:
    data = {}    
    try:
        data.update(get_main_info(soup))
        data.update(get_price(soup))
        data.update(get_user_info(soup))
        data.update(get_announcement_info(soup))
        data.update(get_equipment(soup))
        return data
    except Exception as error:
        return data