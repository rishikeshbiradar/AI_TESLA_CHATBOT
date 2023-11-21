import re

knowledge_base = {
    "What is Tesla?": {
        "keywords": ["Tesla",'What'],
        "answer": "Tesla, Inc. is an American electric vehicle and clean energy company."
    },
    "Who is the CEO of Tesla?": {
        "keywords": ["CEO", "Tesla"],
        "answer": "Elon Musk is the CEO of Tesla."
    },
    "Where is Tesla headquartered?": {
        "keywords": ["headquarters", "Tesla"],
        "answer": "Tesla is headquartered in Palo Alto, California."
    },
    "What is the most popular Tesla car model?": {
        "keywords": ["popular", "Tesla", "car model"],
        "answer": "The Tesla Model 3 is currently the most popular Tesla car model."
    },
    "What is the range of the Tesla Model S?": {
        "keywords": ["range", "Tesla Model S"],
        "answer": "The range of the Tesla Model S varies depending on the version, but it can go up to 400 miles."
    },
    "Can you charge a Tesla at home?": {
        "keywords": ["charge", "Tesla", "home"],
        "answer": "Yes, you can charge a Tesla at home using a standard electrical outlet or a dedicated charging station."
    },
    "How long does it take to charge a Tesla?": {
        "keywords": ["charge", "Tesla"],
        "answer": "The charging time for a Tesla depends on the charging equipment and the car model. It can range from a few hours to several hours."
    },
    "What is Autopilot in Tesla?": {
        "keywords": ["Autopilot", "Tesla"],
        "answer": "Autopilot is an advanced driver-assistance system in Tesla vehicles that provides features like lane centering, adaptive cruise control, self-parking, and more."
    },
    "Are Teslas fully autonomous?": {
        "keywords": ["Teslas", "fully autonomous"],
        "answer": "No, Teslas are not fully autonomous. While they have advanced driver-assistance capabilities, they still require driver supervision."
    },
    "Does Tesla produce renewable energy?": {
        "keywords": ["Tesla", "renewable energy"],
        "answer": "Yes, Tesla is involved in renewable energy production through its subsidiary, SolarCity, which offers solar energy products and services."
    },
    "Is Tesla profitable?": {
        "keywords": ["Tesla", "profitable"],
        "answer": "Tesla has shown profitability in recent years, although it is important to note that financial performance can vary over time."
    },
    "What is the price of a Tesla Model X?": {
        "keywords": ["price", "Tesla Model X"],
        "answer": "The price of a Tesla Model X depends on various factors such as configuration and optional features. It typically starts around $90,000."
    },
    "Can you upgrade the software of a Tesla?": {
        "keywords": ["upgrade", "software", "Tesla"],
        "answer": "Yes, Tesla regularly releases software updates for its vehicles. These updates can add new features, improve performance, and enhance functionality."
    },
    "How many Supercharger stations are there?": {
        "keywords": ["Supercharger", "stations", "Tesla"],
        "answer": "As of my knowledge cutoff in September 2021, Tesla has a global network of over 25,000 Supercharger stations."
    },
    "What is the top speed of a Tesla Roadster?": {
        "keywords": ["top speed", "Tesla Roadster"],
        "answer": "The upcoming Tesla Roadster is expected to have a top speed of over 250 mph (400 km/h)."
    },
    "Does Tesla offer a warranty for its vehicles?": {
        "keywords": ["warranty", "Tesla", "vehicles"],
        "answer": "Yes, Tesla offers a limited warranty for its vehicles that covers specific components and systems for a certain period of time or mileage, whichever comes first."
    },
    "What is the Tesla Gigafactory?": {
        "keywords": ["Tesla", "Gigafactory"],
        "answer": "The Tesla Gigafactory is a large-scale manufacturing facility where Tesla produces batteries, battery packs, and other components for its vehicles and energy products."
    },
    "What is the energy capacity of the Tesla Powerwall?": {
        "keywords": ["energy capacity", "Tesla Powerwall"],
        "answer": "The Tesla Powerwall has a usable energy capacity of 13.5 kilowatt-hours (kWh)."
    },
    "Can you use a Tesla for long-distance road trips?": {
        "keywords": ["Tesla", "long-distance", "road trips"],
        "answer": "Yes, Tesla vehicles are well-suited for long-distance road trips due to their long-range capabilities and the extensive Supercharger network."
    },
    "Does Tesla offer any vehicle leasing options?": {
        "keywords": ["Tesla", "vehicle leasing"],
        "answer": "Yes, Tesla offers vehicle leasing options in select regions. You can check with your local Tesla dealership or visit their website for more details."
    },
    "What is the top speed of the Tesla Model S Plaid?": {
        "keywords": ["top speed", "Tesla Model S Plaid"],
        "answer": "The Tesla Model S Plaid has a top speed of 200 mph (322 km/h)."
    },
    "What is the acceleration of a Tesla Model 3 Performance?": {
        "keywords": ["acceleration", "Tesla Model 3 Performance"],
        "answer": "The Tesla Model 3 Performance can accelerate from 0 to 60 mph in just 3.1 seconds."
    },
    "Does Tesla offer any discounts or incentives?": {
        "keywords": ["Tesla", "discounts", "incentives"],
        "answer": "Tesla occasionally offers discounts, incentives, and promotions. It's best to check their official website or contact a Tesla representative for the most up-to-date information."
    },
    "Can you use third-party charging stations for a Tesla?": {
        "keywords": ["third-party", "charging stations", "Tesla"],
        "answer": "Yes, Tesla vehicles can be charged using third-party charging stations that are compatible with the Tesla charging standard (e.g., CHAdeMO or CCS). However, using Tesla Supercharger stations provides the fastest charging speeds."
    },
    "What is the warranty period for the Tesla battery pack?": {
        "keywords": ["warranty period", "Tesla", "battery pack"],
        "answer": "Tesla provides a warranty for the battery pack of its vehicles that typically covers 8 years or a certain mileage threshold, depending on the specific model and region."
    },
    "What is the towing capacity of a Tesla Model X?": {
        "keywords": ["towing capacity", "Tesla Model X"],
        "answer": "The Tesla Model X has a towing capacity of up to 5,000 pounds (2,268 kg) when properly equipped."
    },
    "Are Tesla vehicles eligible for government incentives or tax credits?": {
        "keywords": ["Tesla vehicles", "government incentives", "tax credits"],
        "answer": "Yes, in many regions, Tesla vehicles may be eligible for government incentives or tax credits for electric vehicles. The availability and amount of incentives can vary by location and change over time."
    },
    "What is the cargo capacity of a Tesla Model Y?": {
        "keywords": ["cargo capacity", "Tesla Model Y"],
        "answer": "The Tesla Model Y has a cargo capacity of up to 68 cubic feet (1,925 liters) with the rear seats folded down."
    },
    "Can you preheat or precool a Tesla remotely?": {
        "keywords": ["preheat", "precool", "Tesla", "remotely"],
        "answer": "Yes, Tesla vehicles have a feature called 'Preconditioning' that allows you to preheat or precool the car's interior remotely using the mobile app or web portal."
    },
    "Does Tesla offer any maintenance services?": {
        "keywords": ["maintenance services", "Tesla"],
        "answer": "Yes, Tesla offers maintenance services through their service centers. They provide routine maintenance, repairs, and software updates for Tesla vehicles."
    }
}

def process_question(question):
    for key in knowledge_base:
        if all(keyword in question for keyword in knowledge_base[key]['keywords']):
            return knowledge_base[key]['answer']
    return "I'm sorry, but I don't have the answer to that question."

while True:
    user_question = input("Ask me a question about Tesla: ")
    if user_question.lower() == "quit":
        break
    answer = process_question(user_question)
    print(answer)