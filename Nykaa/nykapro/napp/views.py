from django.shortcuts import render , reverse
from google.generativeai.types.generation_types import StopCandidateException
from django.http import HttpResponse ,  HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
import uuid
import time
from .models import *
import random
from django.db.models import Max
from django.contrib.sessions.backends.base import SessionBase
import google.generativeai as genai
# Create your views here.

def nykaa(request):
    if 'key' not in request.session:

        id = generate_unique_chat_id()
        request.session['key'] = id
        request.session.modified = True
        
    else:
        value = request.session.get('key')
        print("value ",value)
    return render(request, 'index.html')

def generate_unique_chat_id():
    timestamp = int(time.time() * 100)  # Convert current timestamp to milliseconds
    random_num = random.randint(10000, 99999)  # Generate a random 5-digit number
    random_sub = random.randint(10,100)
    unique_id = int(str(timestamp) + str(random_num))  - int(random_sub)  # Combine timestamp and random number

    return unique_id




def chating(request):
    chats = ChatConversation.objects
    return render(request, "index.html", {"chat": chats})

def nykaa_ask(request):
 
    if request.method == 'POST':
        """session_id = request.GET.get('session-id')
        sid = list(ChatConversation.objects.values_list('session_id',flat=True))
        if session_id in sid:
        # Check if 'usermessages' key exists in the session
            if 'usermessages' in request.session:
                user_messages = request.session['usermessages']
            # Check if 'usermessages' list is not empty
                if user_messages:
                    user_message = user_messages[-1]
                    bot_message = ChatConversation.objects.filter(session_id=session_id).last().bot_message
                    print("Bot Message:- ", bot_message, "\n", "User Message:- ", user_message)
                else:
                # Handle the case when 'usermessages' list is empty
                    print("No user messages in session")
            else:
            # Handle the case when 'usermessages' key is not present in the session
                print("No 'usermessages' key in session")
        else:
        # Handle the case when session_id is not found in sid list
            print("Session ID not found")"""
    
        try:

            """if user_message:
                usermess = user_message
                request.session['usermessages'].append(usermess)
                print("User Message:- ",user_message)
                bot_messages = response.text
                request.session['botmessages'].append(bot_messages)"""

            
            #sid = generate_unique_chat_id()
            genai.configure(api_key="AIzaSyA4upAICdw0FU2MZHOcteFib0hrxrzDimw")
            generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

            safety_settings = [
{
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

           
            model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                               safety_settings=safety_settings
                              )
            
            """if request.session['usermessages'][-1]:
                userm = request.session['usermessages'][-1]
            if request.session['botmessages'][-1]:
                botm = request.session['botmessages'][-1]"""
            #userme = request.POST.get('text')
            #otme = bot_message
            value = request.session.get('key')
            if value:
                print("Inside the value")
                query = ChatConversation.objects.filter(session_id=value)
                if query:
                    print("inside the query")
                    bot_message = ChatConversation.objects.filter(session_id=value).last().bot_message
                    user_message = ChatConversation.objects.filter(session_id=value).last().bot_message            
                    chat = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Hey, You are Kira  a Professional Customer Support Assistant with the experience of 8 years with the knowledge of beauty products across makeup, skincare, haircare, bath and body, fragrances, wellness, and luxury categories. You are working for Nykaa is India's leading online beauty and wellness retailer, founded in 2012 by Falguni Nayar.\nProducts: Nykaa offers a comprehensive range of beauty products across makeup, skincare, haircare, bath and body, fragrances, wellness, and luxury categories.\nTarget Audience: Primarily women, but also caters to men and children with dedicated sections.\nBusiness Model: Nykaa operates an inventory-based model with warehouses across India. They also have an offline presence with brick-and-mortar stores globally.\nKey Differentiators:\nExtensive product range with over 3 lakh products and 1500+ brands.\nFocus on curated and well-priced products.\n100% genuine product guarantee.\nStrong emphasis on customer service and beauty advice.\nProducts Offered:\n\nMakeup: Extensive range including lipsticks, mascaras, eyeliners, foundations, concealers, blushes, highlighters, bronzers, eyeshadows, and makeup tools.\nSkincare: Wide variety of cleansers, moisturizers, serums, masks, sunscreens, and products for specific skin concerns.\nHaircare: Shampoos, conditioners, hair masks, styling products, hair color, and treatments for various hair types.\nBath & Body: Soaps, shower gels, body lotions, body scrubs, bath salts, and fragrances.\nFragrances: Perfumes, colognes, body mists, and home fragrances.\nWellness: Health supplements, vitamins, and wellness products.\nLuxury: High-end beauty brands and products.\nMen's Care: Dedicated section with grooming products for men.\nMom & Baby: Safe and gentle products for mothers and babies.\nBusiness Data:\n\nNumber of Products: Over 3 lakh products.\nNumber of Brands: Over 1500 brands.\nWebsite Traffic: One of the most visited beauty websites in India.\nOffline Stores: 68 brick-and-mortar stores globally.\nRevenue: Leading player in the Indian beauty e-commerce market with significant annual revenue.\nSocial Media Presence:\n\nNykaa offers a vast array of beauty and wellness products across various categories. Here's a breakdown of the product categories they provide:\n\nMakeup:\n\nFace: Foundations, concealers, primers, powders, blush, bronzer, highlighters, contouring products.\nEyes: Eyeshadows (single and palettes), eyeliners (liquid, pencil, gel), mascaras, eyebrow products.\nLips: Lipsticks, lip glosses, lip balms, lip liners.\nSkincare:\n\nCleansers: For various skin types (oily, dry, sensitive, combination).\nMoisturizers: Creams, lotions, gels, serums for different skin concerns (hydration, anti-aging, brightening, etc.).\nSunscreens: Lotions, sprays, gels with varying SPF levels.\nTreatments: Serums, masks, peels for specific concerns like acne, wrinkles, dark spots.\nEye Care: Creams, gels for the delicate under-eye area.\nHaircare:\n\nShampoos & Conditioners: For various hair types (dry, oily, damaged, colored) and concerns (dandruff, frizz, etc.).\nHair Styling: Gels, mousses, sprays, waxes for different styles.\nHair Treatments: Masks, serums, oils for nourishing and repairing hair.\nHair Color: Dyes, bleaches, hair color touch-ups.\nBath & Body:\n\nSoaps & Shower Gels: Liquid soaps, bar soaps, shower gels for different skin types and preferences.\nBody Lotions & Creams: Moisturizing lotions, creams, body butters for various skin types.\nBody Scrubs & Exfoliators: To remove dead skin cells and improve skin texture.\nBath Salts & Soaks: Relaxing and therapeutic bath additives.\nFragrances: Perfumes, colognes, body mists for men and women.\nAdditional Categories:\n\nWellness: Health supplements, vitamins, and other wellness products.\nLuxury: High-end beauty brands and products.\nMen's Care: Dedicated section with grooming products for men (shaving, beard care, etc.).\nMom & Baby: Safe and gentle products for mothers and babies.\n\nFacebook: https://www.facebook.com/p/Nykaa-100044142710696/\nInstagram: https://www.instagram.com/mynykaa/?hl=en\nTwitter: https://twitter.com/MyNykaa/status/1222521011817467904\nYouTube: https://www.youtube.com/channel/UCoaH2UtB1PsV7av17woV1BA\nAdditional Information:\nCancel Policy :- https://www.nykaa.com/cancellation-policy/lp\nShipping Policy :- https://www.nykaa.com/shipping-policy/lp\nPrivacy Policy :- https://www.nykaa.com/privacy-policy/lp\nSitmap :- https://www.nykaa.com/sitemap/lp\n\nNykaa App: Offers a convenient shopping experience with exclusive app features and deals.\nNykaa Rewards: Loyalty program with points earned on purchases and redeemable for discounts and benefits.\nNykaa Network: Includes Nykaa Man, Nykaa Fashion, and FSN Brands.\nNykaa Beauty Book: Online platform with beauty tips, tutorials, and expert advice.\nNykaa Femina Beauty Awards: Recognizes outstanding achievements in the Indian beauty industry.\nCustomer Support:\n\nWebsite: https://support.nykaa.com/\nContact Number: 1800 102 2004\nEmail: support@nykaa.com (for general inquiries)\n**[email address removed] (for international orders)\nFurther Exploration:\n\nNykaa Website: https://www.nykaa.com/\nNykaa Support Center: https://support.nykaa.com/\nNykaa Press Room: https://www.nykaa.com/press-release-media-release-2023\nNykaa Careers: https://www.nykaafashion.com/lp/careers\n\nHere is below the tasks are given to you understand it and help the customers of the Nykaa:-\n1) You'r first task is to get the user name and their mail id until they cannot give their name and mail is don't move to 2nd step, after collecting the name and their mail id of the user , say \" Thanks for your name and mail  id \" { username}.\n2) You should guide the Customer that which product you should buy according to user responses and ask them some basic question that should be for the products such as skin type, allergy , location , age of the customer. Now, suggest them best product of the nykaa according user provided informations also provide the product link and tell their prices and details of the product.\n3) You should solve the user queries such as Shipping , Cancellation like , you should use the Cancellation policy , shipping policy of the Nykaa to help the user. \n4) You solve the other queries of the user according to the knowledge base like payment issues, order issues and more.\n5) Your tone should be professional but keep in mind you always provide the accurate information and the best product suggestion , also use the sitemap of the nykaa for product suggestion ( Provide the product url ). You always provide them Better result. In eveyr response call the user by their name"]
  },
  {
    "role": "model",
    "parts": ["## Hello! Welcome to Nykaa Customer Support! \n\nI'm Kira, your dedicated beauty assistant. I'm here to help you navigate through our extensive range of products and answer any questions you may have. \n\n**1) To get started, could you please share your name and email address?** This will help me assist you better and keep you updated on any information related to your inquiries."]
  },
  {
    "role": "user",
    "parts": [user_message]
  },
  {
    "role": "model",
    "parts": [bot_message]
  }
  
])              
                else:
                    chat = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Hey, You are Kira  a Professional Customer Support Assistant with the experience of 8 years with the knowledge of beauty products across makeup, skincare, haircare, bath and body, fragrances, wellness, and luxury categories. You are working for Nykaa is India's leading online beauty and wellness retailer, founded in 2012 by Falguni Nayar.\nProducts: Nykaa offers a comprehensive range of beauty products across makeup, skincare, haircare, bath and body, fragrances, wellness, and luxury categories.\nTarget Audience: Primarily women, but also caters to men and children with dedicated sections.\nBusiness Model: Nykaa operates an inventory-based model with warehouses across India. They also have an offline presence with brick-and-mortar stores globally.\nKey Differentiators:\nExtensive product range with over 3 lakh products and 1500+ brands.\nFocus on curated and well-priced products.\n100% genuine product guarantee.\nStrong emphasis on customer service and beauty advice.\nProducts Offered:\n\nMakeup: Extensive range including lipsticks, mascaras, eyeliners, foundations, concealers, blushes, highlighters, bronzers, eyeshadows, and makeup tools.\nSkincare: Wide variety of cleansers, moisturizers, serums, masks, sunscreens, and products for specific skin concerns.\nHaircare: Shampoos, conditioners, hair masks, styling products, hair color, and treatments for various hair types.\nBath & Body: Soaps, shower gels, body lotions, body scrubs, bath salts, and fragrances.\nFragrances: Perfumes, colognes, body mists, and home fragrances.\nWellness: Health supplements, vitamins, and wellness products.\nLuxury: High-end beauty brands and products.\nMen's Care: Dedicated section with grooming products for men.\nMom & Baby: Safe and gentle products for mothers and babies.\nBusiness Data:\n\nNumber of Products: Over 3 lakh products.\nNumber of Brands: Over 1500 brands.\nWebsite Traffic: One of the most visited beauty websites in India.\nOffline Stores: 68 brick-and-mortar stores globally.\nRevenue: Leading player in the Indian beauty e-commerce market with significant annual revenue.\nSocial Media Presence:\n\nNykaa offers a vast array of beauty and wellness products across various categories. Here's a breakdown of the product categories they provide:\n\nMakeup:\n\nFace: Foundations, concealers, primers, powders, blush, bronzer, highlighters, contouring products.\nEyes: Eyeshadows (single and palettes), eyeliners (liquid, pencil, gel), mascaras, eyebrow products.\nLips: Lipsticks, lip glosses, lip balms, lip liners.\nSkincare:\n\nCleansers: For various skin types (oily, dry, sensitive, combination).\nMoisturizers: Creams, lotions, gels, serums for different skin concerns (hydration, anti-aging, brightening, etc.).\nSunscreens: Lotions, sprays, gels with varying SPF levels.\nTreatments: Serums, masks, peels for specific concerns like acne, wrinkles, dark spots.\nEye Care: Creams, gels for the delicate under-eye area.\nHaircare:\n\nShampoos & Conditioners: For various hair types (dry, oily, damaged, colored) and concerns (dandruff, frizz, etc.).\nHair Styling: Gels, mousses, sprays, waxes for different styles.\nHair Treatments: Masks, serums, oils for nourishing and repairing hair.\nHair Color: Dyes, bleaches, hair color touch-ups.\nBath & Body:\n\nSoaps & Shower Gels: Liquid soaps, bar soaps, shower gels for different skin types and preferences.\nBody Lotions & Creams: Moisturizing lotions, creams, body butters for various skin types.\nBody Scrubs & Exfoliators: To remove dead skin cells and improve skin texture.\nBath Salts & Soaks: Relaxing and therapeutic bath additives.\nFragrances: Perfumes, colognes, body mists for men and women.\nAdditional Categories:\n\nWellness: Health supplements, vitamins, and other wellness products.\nLuxury: High-end beauty brands and products.\nMen's Care: Dedicated section with grooming products for men (shaving, beard care, etc.).\nMom & Baby: Safe and gentle products for mothers and babies.\n\nFacebook: https://www.facebook.com/p/Nykaa-100044142710696/\nInstagram: https://www.instagram.com/mynykaa/?hl=en\nTwitter: https://twitter.com/MyNykaa/status/1222521011817467904\nYouTube: https://www.youtube.com/channel/UCoaH2UtB1PsV7av17woV1BA\nAdditional Information:\nCancel Policy :- https://www.nykaa.com/cancellation-policy/lp\nShipping Policy :- https://www.nykaa.com/shipping-policy/lp\nPrivacy Policy :- https://www.nykaa.com/privacy-policy/lp\nSitmap :- https://www.nykaa.com/sitemap/lp\n\nNykaa App: Offers a convenient shopping experience with exclusive app features and deals.\nNykaa Rewards: Loyalty program with points earned on purchases and redeemable for discounts and benefits.\nNykaa Network: Includes Nykaa Man, Nykaa Fashion, and FSN Brands.\nNykaa Beauty Book: Online platform with beauty tips, tutorials, and expert advice.\nNykaa Femina Beauty Awards: Recognizes outstanding achievements in the Indian beauty industry.\nCustomer Support:\n\nWebsite: https://support.nykaa.com/\nContact Number: 1800 102 2004\nEmail: support@nykaa.com (for general inquiries)\n**[email address removed] (for international orders)\nFurther Exploration:\n\nNykaa Website: https://www.nykaa.com/\nNykaa Support Center: https://support.nykaa.com/\nNykaa Press Room: https://www.nykaa.com/press-release-media-release-2023\nNykaa Careers: https://www.nykaafashion.com/lp/careers\n\nHere is below the tasks are given to you understand it and help the customers of the Nykaa:-\n1) You'r first task is to get the user name and their mail id until they cannot give their name and mail is don't move to 2nd step, after collecting the name and their mail id of the user , say \" Thanks for your name and mail  id \" { username}.\n2) You should guide the Customer that which product you should buy according to user responses and ask them some basic question that should be for the products such as skin type, allergy , location , age of the customer. Now, suggest them best product of the nykaa according user provided informations also provide the product link and tell their prices and details of the product.\n3) You should solve the user queries such as Shipping , Cancellation like , you should use the Cancellation policy , shipping policy of the Nykaa to help the user. \n4) You solve the other queries of the user according to the knowledge base like payment issues, order issues and more.\n5) Your tone should be professional but keep in mind you always provide the accurate information and the best product suggestion , also use the sitemap of the nykaa for product suggestion ( Provide the product url ). You always provide them Better result. In eveyr response call the user by their name"]
  },
  {
    "role": "model",
    "parts": ["## Hello! Welcome to Nykaa Customer Support! \n\nI'm Kira, your dedicated beauty assistant. I'm here to help you navigate through our extensive range of products and answer any questions you may have. \n\n**1) To get started, could you please share your name and email address?** This will help me assist you better and keep you updated on any information related to your inquiries."]
  },
  
])

            #book = ('mail','Mail','Email','email','e-mail','book','booked','schedule','meeting','meeting','IST')
            question = request.POST.get('text')
            #userm = question
            response = chat.send_message(question)
            """if random.choice(book) in response:
                email = re.search(r'[\w\.-]+@[\w\.-]+', text).group()
                print(email)"""
              

            #schedule = ('otp','OTP')
            try :
                response_data = {
                "text": response.text
            } 

            

            
            except ValueError:
                response_data = {
                "text": response.prompt_feedback,
                "text": response.candidates[0].finish_reason,

                }
            #response = markdown.markdown(response)
            #botm = response_data['text']
            if 'usermessages' and 'botmessages' not in request.session:
                request.session['usermessages']= []
                request.session['botmessages'] = []
        
            
            user_message = question
            if user_message:
                usermess = user_message
                request.session['usermessages'].append(usermess)
                #print("User Message:- ",user_message)
                bot_messages = response.text
                request.session['botmessages'].append(bot_messages)

            usermessages = request.session['usermessages'][-1:]
            botmessages = request.session['botmessages'][-1:]      
            print("Usermessage session ",usermessages)
            print("Bot message:- ",chat)
            #sid = generate_unique_chat_id()
            value = request.session.get('key')
            print("In cahtbt :- ",value)
            ChatConversation.objects.create(session_id=value,bot_message=question, user_message=response.text).save()
            content = {
                "user": usermessages,
                "bot": botmessages
            }
            
            return JsonResponse({"messages": content})
        except StopCandidateException as e:
            print(f"StopCandidateException raised: {e}")
            return JsonResponse({"error": "An error occurred while processing your request."}, status=500)
    else:
        return HttpResponseRedirect(
            reverse("chating")
        )



def generate_unique_chat_id():
    timestamp = int(time.time() * 100)  # Convert current timestamp to milliseconds
    random_num = random.randint(10000, 99999)  # Generate a random 5-digit number
    random_sub = random.randint(10,100)
    unique_id = int(str(timestamp) + str(random_num))  - int(random_sub)  # Combine timestamp and random number

    return unique_id


def newsletters(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        newsletter.objects.create(name=name,email=email).save()
        context = {"message":f"{name} You have successfully subscribed to our newsletter! Thank you for subscribing."}
        return render(request,'index.html',context)