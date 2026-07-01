# Localized database of crop diseases and healthy states
# Languages: English (en), Hindi (hi), Marathi (mr)

DISEASE_DB = {
    # ------------------- TOMATO -------------------
    'tomato_early_blight': {
        'crop': 'Tomato',
        'severity': 'Medium',
        'en': {
            'name': 'Tomato Early Blight',
            'description': 'A common fungal disease caused by Alternaria solani. It causes circular dark spots with concentric rings resembling target boards on older leaves first.',
            'causes': 'Warm temperature (24-29°C), high humidity, wet foliage, and poor soil drainage.',
            'prevention': 'Rotate crops, keep foliage dry using drip irrigation, and remove infected crop residues.',
            'fertilizer': 'Apply balanced nitrogen-potassium fertilizers to improve crop vigor.',
            'pesticide': 'Spray copper-based fungicides (e.g., Copper Oxychloride) or Mancozeb.',
            'organic_solution': 'Spray neem oil or baking soda solution (3 tbsp per gallon of water).',
            'irrigation': 'Reduce overhead watering. Switch to drip irrigation and water early in the morning.'
        },
        'hi': {
            'name': 'टमाटर अगेती झुलसा (Early Blight)',
            'description': 'अल्टरनेरिया सोलानी नामक कवक के कारण होने वाला रोग। पत्तियों पर संकेंद्रित छल्लों (target boards) के साथ गोल काले धब्बे दिखाई देते हैं।',
            'causes': 'गर्म तापमान (24-29°C), अधिक आर्द्रता, पत्तियों का गीला रहना और खराब जल निकासी।',
            'prevention': 'फसल चक्र अपनाएं, ड्रिप सिंचाई का उपयोग करें, और संक्रमित पौधों को हटा दें।',
            'fertilizer': 'पौधों की मजबूती के लिए संतुलित नाइट्रोजन-पोटेशियम उर्वरक डालें।',
            'pesticide': 'तांबा आधारित फफूंदनाशी (जैसे कॉपर ऑक्सीक्लोराइड) या मैनकोज़ेब का छिड़काव करें।',
            'organic_solution': 'नीम के तेल या बेकिंग सोडा के घोल (3 चम्मच प्रति गैलन पानी) का छिड़काव करें।',
            'irrigation': 'पत्तियों के ऊपर से पानी देना बंद करें। ड्रिप प्रणाली का उपयोग करें और सुबह जल्दी पानी दें।'
        },
        'mr': {
            'name': 'टोमॅटो लवकर येणारा करपा (Early Blight)',
            'description': 'अल्टरनेरिया सोलानी या बुरशीमुळे होणारा रोग. पानावरील गोलाकार गडद ठिपके ज्यावर रिंगा दिसतात.',
            'causes': 'उष्ण तापमान (२४-२९ अंश सेल्सिअस), जास्त दमटपणा, पानांवर पाणी राहणे.',
            'prevention': 'पीक बदल (Crop Rotation) करा, ठिबक सिंचन वापरा, आणि खराब झाडे नष्ट करा.',
            'fertilizer': 'झाडांची ताकद वाढवण्यासाठी संतुलित नत्र-पलाश खते द्या.',
            'pesticide': 'तांबेयुक्त बुरशीनाशक (उदा. कॉपर ऑक्सीक्लोराईड) किंवा मँकोझेब फवारावे.',
            'organic_solution': 'कडुनिंब तेल किंवा बेकिंग सोडा द्रावणाचा फवारा मारा.',
            'irrigation': 'पानांवरून पाणी देणे थांबवा. ठिबक सिंचनाचा वापर करून सकाळी लवकर पाणी द्या.'
        },
        'schemes': ['PM Fasal Bima Yojana', 'Sub-Mission on Plant Protection']
    },
    'tomato_late_blight': {
        'crop': 'Tomato',
        'severity': 'High',
        'en': {
            'name': 'Tomato Late Blight',
            'description': 'A devastating disease caused by the oomycete Phytophthora infestans. It leads to rapid leaf blackening and fuzzy white fungal growth under humid conditions.',
            'causes': 'Cool temperatures (15-20°C) with persistent wet weather and high relative humidity.',
            'prevention': 'Use certified disease-free seeds, avoid overhead irrigation, and prune lower leaves.',
            'fertilizer': 'Avoid excessive nitrogen; apply phosphorus and potassium to strengthen cell walls.',
            'pesticide': 'Use systemic fungicides containing Metalaxyl or Chlorothalonil.',
            'organic_solution': 'Apply copper hydroxide spray or compost tea solutions.',
            'irrigation': 'Keep foliage completely dry. Monitor wet weather patterns closely.'
        },
        'hi': {
            'name': 'टमाटर पछेती झुलसा (Late Blight)',
            'description': 'फाइटोफ्थोरा इन्फेस्टन्स के कारण होने वाला विनाशकारी रोग। गीली परिस्थितियों में पत्तियों का तेजी से काला होना और उन पर सफेद कवक विकसित होना।',
            'causes': 'ठंडा तापमान (15-20°C) और लगातार बारिश या अत्यधिक नमी।',
            'prevention': 'प्रमाणित रोग-मुक्त बीजों का उपयोग करें, ऊपर से पानी देने से बचें और निचली पत्तियों को काटें।',
            'fertilizer': 'अत्यधिक नाइट्रोजन से बचें; कोशिकाओं को मजबूत करने के लिए फास्फोरस और पोटेशियम डालें।',
            'pesticide': 'मेटालैक्सिल या क्लोरोथैलोनिल युक्त प्रणालीगत फफूंदनाशी का उपयोग करें।',
            'organic_solution': 'कॉपर हाइड्रॉक्साइड का छिड़काव या कम्पोस्ट चाय के घोल का प्रयोग करें।',
            'irrigation': 'पत्तियों को पूरी तरह सूखा रखें। बरसात के मौसम में सिंचाई को नियंत्रित करें।'
        },
        'mr': {
            'name': 'टोमॅटो उशिरा येणारा करपा (Late Blight)',
            'description': 'फायटोफ्थोरा इन्फेस्टन्स या बुरशीमुळे होणारा अत्यंत नुकसानकारक रोग. पानांवर पांढऱ्या रंगाची बुरशी वाढते आणि पाने काळी पडतात.',
            'causes': 'थंड तापमान (१५-२० अंश सेल्सिअस) आणि सतत पडणारा पाऊस किंवा धुके.',
            'prevention': 'निरोगी रोपे वापरा, पानांवर पाणी उडवणे टाळा, खालची पाने छाटून टाका.',
            'fertilizer': 'नत्राचा अतिवापर टाळा; स्फुरद आणि पालाश खतांचा पुरवठा करा.',
            'pesticide': 'मेटालॅक्सिल किंवा क्लोरोथॅलोनिलयुक्त आंतरप्रवाही बुरशीनाशक फवारा.',
            'organic_solution': 'कॉपर हायड्रॉक्साइड किंवा कंपोस्ट टी द्रावण फवारा.',
            'irrigation': 'पाने सुकी राहतील याची काळजी घ्या. पावसाचा अंदाज घेऊन पाणी देणे थांबवा.'
        },
        'schemes': ['PM Fasal Bima Yojana', 'Sub-Mission on Plant Protection']
    },
    'tomato_leaf_mold': {
        'crop': 'Tomato',
        'severity': 'Low',
        'en': {
            'name': 'Tomato Leaf Mold',
            'description': 'Caused by the fungus Passalora fulva. Olive-green to brown velvety mold develops on the lower surface of older leaves.',
            'causes': 'High relative humidity (>85%) and moderate temperatures in greenhouses or crowded fields.',
            'prevention': 'Improve air circulation, space out plants, and select resistant cultivars.',
            'fertilizer': 'Ensure balanced micronutrients, particularly calcium and magnesium.',
            'pesticide': 'Apply Chlorothalonil or Dithane M-45 in severe cases.',
            'organic_solution': 'Spray baking soda solution or sulfur dust powder on dry leaves.',
            'irrigation': 'Water the soil directly. Avoid spraying foliage.'
        },
        'hi': {
            'name': 'टमाटर पत्ती मोल्ड (Leaf Mold)',
            'description': 'पासालोरा फुल्वा कवक के कारण होता है। पुरानी पत्तियों की निचली सतह पर जैतून-हरे से भूरे रंग के मखमली मोल्ड विकसित होते हैं।',
            'causes': 'अत्यधिक नमी (>85%) और मध्यम तापमान (ग्रीनहाउस या सघन बुवाई में)।',
            'prevention': 'हवा के संचार में सुधार करें, पौधों के बीच दूरी बढ़ाएं और प्रतिरोधी किस्में लगाएं।',
            'fertilizer': 'संतुलित सूक्ष्म पोषक तत्व, विशेष रूप से कैल्शियम और मैग्नीशियम सुनिश्चित करें।',
            'pesticide': 'गंभीर मामलों में क्लोरोथैलोनिल या डायथेन एम-45 लगाएं।',
            'organic_solution': 'सूखी पत्तियों पर बेकिंग सोडा घोल या सल्फर डस्ट पाउडर छिड़कें।',
            'irrigation': 'मिट्टी में सीधे पानी दें। पत्तियों पर पानी का छिड़काव करने से बचें।'
        },
        'mr': {
            'name': 'टोमॅटो पानावरील ओलिव्ह बुरशी (Leaf Mold)',
            'description': 'पासालोरा फुल्वा बुरशीमुळे होणारा रोग. पानाच्या पाठीमागच्या बाजूला मखमली तपकिरी-हिरवी बुरशी वाढते.',
            'causes': 'अति दमट हवामान (८५% पेक्षा जास्त) आणि हवा खेळती नसणे.',
            'prevention': 'हवा खेळती ठेवा, रोपांमध्ये अंतर ठेवा आणि रोगप्रतिकारक वाण लावा.',
            'fertilizer': 'कॅल्शियम आणि मॅग्नेशियमसारख्या सूक्ष्म अन्नद्रव्यांचा पुरवठा करा.',
            'pesticide': 'क्लोरोथॅलोनिल किंवा डायथेन एम-४५ बुरशीनाशक वापरावे.',
            'organic_solution': 'कोरड्या पानांवर बेकिंग सोडा किंवा गंधक (सल्फर) पावडर फवारा.',
            'irrigation': 'थेट मुळाशी पाणी द्या, पानांवर पाणी मारणे टाळा.'
        },
        'schemes': ['Rashtriya Krishi Vikas Yojana']
    },
    'tomato_septoria_leaf_spot': {
        'crop': 'Tomato',
        'severity': 'Medium',
        'en': {
            'name': 'Septoria Leaf Spot',
            'description': 'Caused by Septoria lycopersici. Small, circular gray spots with dark borders appear, leading to leaf drop and sunscald.',
            'causes': 'Warm weather with wet leaf surfaces caused by rainfall or overhead sprinklers.',
            'prevention': 'Remove weeds, clean tools, and mulch around plants to prevent soil splashing.',
            'fertilizer': 'Apply nitrogen to assist regrowth, but don\'t overdo it.',
            'pesticide': 'Copper fungicides or Mancozeb sprayed every 7-10 days.',
            'organic_solution': 'Spray copper soap or use biological fungicides like Bacillus subtilis.',
            'irrigation': 'Drip irrigation only. Water directly to the soil surface.'
        },
        'hi': {
            'name': 'सेप्टोरिया पत्ती धब्बा (Septoria Leaf Spot)',
            'description': 'सेप्टोरिया लाइकोपर्सिकी कवक से उत्पन्न। पत्तियों पर छोटे गोल भूरे रंग के धब्बे दिखते हैं जिससे पत्तियां गिर जाती हैं।',
            'causes': 'गर्म मौसम और बारिश या स्प्रिंकलर के कारण पत्तियों का लंबे समय तक गीला रहना।',
            'prevention': 'खरपतवार हटाएं, उपकरणों को साफ रखें और मिट्टी के छीटों को रोकने के लिए मल्चिंग करें।',
            'fertilizer': 'पत्तियों के पुनर्विकास में मदद के लिए संतुलित नाइट्रोजन का प्रयोग करें।',
            'pesticide': 'कॉपर फफूंदनाशी या मैनकोज़ेब का हर 7-10 दिनों में छिड़काव करें।',
            'organic_solution': 'कॉपर सोप का छिड़काव करें या बैसिलस सबटिलिस जैसे जैविक फंगिसाइड्स का उपयोग करें।',
            'irrigation': 'केवल ड्रिप सिंचाई करें। पानी सीधे मिट्टी में ही जाना चाहिए।'
        },
        'mr': {
            'name': 'सेप्टोरिया पानावरील ठिपके (Septoria Leaf Spot)',
            'description': 'सेप्टोरिया लायकोपर्सिकी बुरशीमुळे पानांवर करड्या रंगाचे लहान गोल ठिपके तयार होतात आणि पाने गळतात.',
            'causes': 'उष्ण हवामान आणि पावसाच्या किंवा फवाऱ्याच्या पाण्यामुळे पाने ओली राहणे.',
            'prevention': 'तण काढा, शेती अवजारे निर्जंतुक करा आणि झाडांच्या मुळाशी आच्छादन (Mulching) करा.',
            'fertilizer': 'नवीन पानांच्या वाढीसाठी योग्य प्रमाणात नत्र खते द्या.',
            'pesticide': 'कॉपर बुरशीनाशक किंवा मँकोझेब दर ७-१० दिवसांनी फवारावे.',
            'organic_solution': 'कॉपर सोप किंवा बॅसिलस सबटिलिस जैविक बुरशीनाशक वापरा.',
            'irrigation': 'फक्त ठिबक सिंचन वापरा. पाणी झाडाच्या बुंध्यापाशी द्या.'
        },
        'schemes': ['Sub-Mission on Plant Protection']
    },
    'tomato_yellow_leaf_curl_virus': {
        'crop': 'Tomato',
        'severity': 'High',
        'en': {
            'name': 'Tomato Yellow Leaf Curl Virus (TYLCV)',
            'description': 'A viral disease transmitted by silverleaf whiteflies. Infected plants exhibit severe stunting and upward leaf cupping.',
            'causes': 'Heavy whitefly populations in warm, dry weather conditions.',
            'prevention': 'Use insect netting, plant resistant tomato varieties, and weed host plants.',
            'fertilizer': 'Use fertilizers rich in potassium to support systemic stress resistance.',
            'pesticide': 'Control whiteflies using insecticides like Imidacloprid or Acetamiprid.',
            'organic_solution': 'Spray insecticidal soaps, neem formulations, or install yellow sticky traps.',
            'irrigation': 'Maintain regular irrigation. Do not let viral plants suffer dry stress.'
        },
        'hi': {
            'name': 'टमाटर पीला पत्ती कर्ल वायरस (TYLCV)',
            'description': 'सफेद मक्खियों (Whiteflies) द्वारा फैलाया जाने वाला वायरस। पौधे बौने हो जाते हैं और पत्तियां ऊपर की ओर मुड़ जाती हैं।',
            'causes': 'गर्म और सूखे मौसम के दौरान सफेद मक्खियों की संख्या में भारी वृद्धि।',
            'prevention': 'कीट नेटिंग का उपयोग करें, प्रतिरोधी टमाटर की किस्में उगाएं और खरपतवार नष्ट करें।',
            'fertilizer': 'तनाव प्रतिरोध को बढ़ावा देने के लिए पोटेशियम समृद्ध उर्वरकों का उपयोग करें।',
            'pesticide': 'इमिडाक्लोप्रिड या एसिटामिप्रिड जैसे कीटनाशकों से सफेद मक्खी को नियंत्रित करें।',
            'organic_solution': 'पीले चिपचिपे कार्ड (Yellow Sticky Traps) लगाएं और नीम के तेल का छिड़काव करें।',
            'irrigation': 'नियमित सिंचाई जारी रखें। वायरस-पीड़ित पौधों को सूखे तनाव से बचाएं।'
        },
        'mr': {
            'name': 'टोमॅटो पिवळा पानांचा चुरडा (TYLCV)',
            'description': 'पांढऱ्या माशीद्वारे (Whitefly) पसरणारा विषाणूजन्य रोग. झाडांची वाढ खुंटते आणि पाने पिवळी पडून वरच्या बाजूला वळतात.',
            'causes': 'उष्ण आणि कोरड्या हवामानात पांढऱ्या माशीचा वाढता प्रादुर्भाव.',
            'prevention': 'कीटक प्रतिबंधक नेट वापरा, पीक तणमुक्त ठेवा, पिवळे चिकट सापळे लावा.',
            'fertilizer': 'तनाव सहन करण्यासाठी पलाश (पोटॅशियम) समृद्ध खतांचा वापर करा.',
            'pesticide': 'पांढऱ्या माशीच्या नियंत्रणासाठी इमिडाक्लोप्रीड किंवा ॲसिटामीप्रीड फवारा.',
            'organic_solution': 'कडुनिंब तेल किंवा साबण पाण्याचे द्रावण फवारा, पिवळे सापळे लावा.',
            'irrigation': 'नियमित पाणी द्या. पाण्याची कमतरता भासू देऊ नका.'
        },
        'schemes': ['Sub-Mission on Agricultural Mechanization', 'PM Fasal Bima Yojana']
    },
    'tomato_healthy': {
        'crop': 'Tomato',
        'severity': 'Low',
        'en': {
            'name': 'Healthy Tomato Leaf',
            'description': 'The leaf shows normal structure and bright green color. No signs of infection, necrosis, or insect damage.',
            'causes': 'Excellent agricultural practices, healthy soil, and proper nutrition.',
            'prevention': 'Continue monitoring, keep field clean, and follow standard spray schedules.',
            'fertilizer': 'Apply balanced NPK at regular vegetative and flowering stages.',
            'pesticide': 'None required. Avoid unnecessary chemical applications.',
            'organic_solution': 'Apply preventive compost tea or diluted seaweed extract.',
            'irrigation': 'Continue scheduled watering based on moisture levels.'
        },
        'hi': {
            'name': 'स्वस्थ टमाटर की पत्ती',
            'description': 'पत्ती सामान्य संरचना और चमकीला हरा रंग प्रदर्शित करती है। किसी संक्रमण या कीट का कोई लक्षण नहीं है।',
            'causes': 'उत्कृष्ट कृषि पद्धतियां, उपजाऊ मिट्टी और उचित पोषण।',
            'prevention': 'नियमित निगरानी जारी रखें, खेत को साफ रखें और मानक देखभाल अपनाएं।',
            'fertilizer': 'नियमित वानस्पतिक और पुष्पन अवस्था में संतुलित एनपीके (NPK) डालें।',
            'pesticide': 'आवश्यकता नहीं है। रासायनिक दवाओं के अनावश्यक प्रयोग से बचें।',
            'organic_solution': 'बचाव के लिए कम्पोस्ट चाय या समुद्री शैवाल का सत्व छिड़कें।',
            'irrigation': 'नमी के स्तर के आधार पर नियमित सिंचाई चक्र जारी रखें।'
        },
        'mr': {
            'name': 'निरोगी टोमॅटोचे पान',
            'description': 'पानाचा आकार आणि हिरवा रंग अतिशय चांगला आहे. कोणत्याही रोगाची किंवा किडीची लक्षणे नाहीत.',
            'causes': 'उत्कृष्ट शेती पद्धती, सुपीक जमीन आणि योग्य पोषण.',
            'prevention': 'नियमित निरीक्षण ठेवा, शेत स्वच्छ ठेवा आणि योग्य नियोजन करा.',
            'fertilizer': 'नियमित वाढीच्या आणि फुलण्याच्या काळात संतुलित एनपीके (NPK) खते द्या.',
            'pesticide': 'गरज नाही. विनाकारण रासायनिक फवारणी टाळा.',
            'organic_solution': 'सुरक्षा म्हणून जीवामृत किंवा कंपोस्ट पाणी वापरा.',
            'irrigation': 'नमीनुसार नियमित पाणी देणे सुरू ठेवा.'
        },
        'schemes': ['Soil Health Card Scheme']
    },

    # ------------------- POTATO -------------------
    'potato_early_blight': {
        'crop': 'Potato',
        'severity': 'Medium',
        'en': {
            'name': 'Potato Early Blight',
            'description': 'A fungal infection caused by Alternaria solani. It targets older foliage, showing concentric brown rings and reducing tuber yield.',
            'causes': 'High humidity, alternate wet and dry periods, and low soil fertility.',
            'prevention': 'Ensure proper soil nutrition (especially nitrogen) and plant certified seed tubers.',
            'fertilizer': 'Apply potassium and adequate nitrogen to promote plant vigor.',
            'pesticide': 'Spray Mancozeb or Chlorothalonil when spots first appear.',
            'organic_solution': 'Use copper soap spray or compost tea foliar sprays.',
            'irrigation': 'Ensure steady watering to avoid drought-wet cycles.'
        },
        'hi': {
            'name': 'आलू अगेती झुलसा (Early Blight)',
            'description': 'अल्टरनेरिया सोलानी के कारण होने वाला कवक रोग। पुरानी पत्तियों पर संकेंद्रित भूरे रंग के छल्ले बनते हैं, जिससे आलू का उत्पादन प्रभावित होता है।',
            'causes': 'उच्च आर्द्रता, बारी-बारी से गीली-सूखी स्थितियां और कमजोर मिट्टी उर्वरता।',
            'prevention': 'मिट्टी को प्रचुर पोषण (विशेष रूप से नाइट्रोजन) दें और प्रमाणित बीज आलू ही बोएं।',
            'fertilizer': 'पौधों को स्वस्थ रखने के लिए पोटेशियम और आवश्यक नाइट्रोजन का छिड़काव करें।',
            'pesticide': 'धब्बे दिखाई देने पर मैन्कोजेब या क्लोरोथैलोनिल का छिड़काव करें।',
            'organic_solution': 'कॉपर सोप स्प्रे या कम्पोस्ट चाय के पर्णीय छिड़काव का प्रयोग करें।',
            'irrigation': 'सूखे-गीले चक्रों से बचने के लिए नियमित रूप से पानी दें।'
        },
        'mr': {
            'name': 'बटाटा लवकर येणारा करपा (Early Blight)',
            'description': 'अल्टरनेरिया सोलानी बुरशीमुळे पानांवर गोल कडेचे ठिपके उमटतात आणि बटाट्याची वाढ मंदावते.',
            'causes': 'जास्त आर्द्रता, सतत दमट हवामान आणि जमिनीत खतांची कमतरता.',
            'prevention': 'जमिनीचे योग्य पोषण ठेवा आणि प्रमाणित बटाटा बियाणे वापरा.',
            'fertilizer': 'झाडांची प्रतिकारशक्ती वाढवण्यासाठी पोटॅश आणि नत्र द्या.',
            'pesticide': 'लक्षणे दिसताच मँकोझेब किंवा क्लोरोथॅलोनिल फवारावे.',
            'organic_solution': 'कॉपर सोप किंवा कंपोस्ट चहाचा पानांवर फवारा घ्या.',
            'irrigation': 'तणाव टाळण्यासाठी ठराविक कालावधीने नियमित पाणी द्या.'
        },
        'schemes': ['PM Fasal Bima Yojana']
    },
    'potato_late_blight': {
        'crop': 'Potato',
        'severity': 'High',
        'en': {
            'name': 'Potato Late Blight',
            'description': 'Caused by Phytophthora infestans. Under cool and wet conditions, it can destroy an entire potato crop in days.',
            'causes': 'Cool temperatures (15-20°C) with persistent rain, dew, or fog.',
            'prevention': 'Destroy volunteer potato crops, avoid overhead watering, and use resistant varieties.',
            'fertilizer': 'Apply phosphorus and potassium at planting to bolster cell wall integrity.',
            'pesticide': 'Use Metalaxyl, Cymoxanil + Mancozeb mixture, or Chlorothalonil.',
            'organic_solution': 'Use copper fungicides or spray fermented nettle water.',
            'irrigation': 'Stop irrigation if continuous rainfall occurs. Ensure proper water drainage.'
        },
        'hi': {
            'name': 'आलू पछेती झुलसा (Late Blight)',
            'description': 'फाइटोफ्थोरा इन्फेस्टन्स के कारण होता है। ठंडी और नम परिस्थितियों में यह कुछ ही दिनों में पूरी आलू की फसल को नष्ट कर सकता है।',
            'causes': 'ठंडा तापमान (15-20°C) और लगातार बारिश, ओस या कोहरा।',
            'prevention': 'संक्रमित कचरे को नष्ट करें, ऊपर से सिंचाई न करें और प्रतिरोधी किस्मों का चुनाव करें।',
            'fertilizer': 'कोशिका भित्ति को मजबूत करने के लिए बुवाई के समय फास्फोरस और पोटाश डालें।',
            'pesticide': 'मेटालैक्सिल, साइमोक्सानिल + मैनकोजेब मिश्रण या क्लोरोथैलोनिल का उपयोग करें।',
            'organic_solution': 'तांबा आधारित कवकनाशी का प्रयोग करें या सड़े हुए बिछुआ (nettle) के पानी का छिड़काव करें।',
            'irrigation': 'लगातार बारिश के दौरान सिंचाई बंद रखें। जल निकासी अच्छी होनी चाहिए।'
        },
        'mr': {
            'name': 'बटाटा उशिरा येणारा करपा (Late Blight)',
            'description': 'फायटोफ्थोरा इन्फेस्टन्स मुळे बटाटा पिकाचे अत्यंत गंभीर नुकसान होते. काही दिवसातच पूर्ण शेत उद्ध्वस्त होऊ शकते.',
            'causes': 'थंड हवामान (१५-२० अंश सेल्सिअस) आणि सतत पडणारा पाऊस किंवा धूळ-धुके.',
            'prevention': 'खराब बटाटे गोळा करून जाळून टाका, पाने ओली ठेवू नका, निरोगी बियाणे वापरा.',
            'fertilizer': 'लागवडीच्या वेळी स्फुरद आणि पालाश खतांचा पुरेसा वापर करा.',
            'pesticide': 'मेटालॅक्सिल किंवा सायमोक्सानिल + मँकोझेब संयुक्त बुरशीनाशक फवारा.',
            'organic_solution': 'कॉपरयुक्त बुरशीनाशक वापरा किंवा पुदिना/कडुनिंब पानांचा अर्क फवारा.',
            'irrigation': 'सतत पाऊस असताना पाणी देणे बंद करा. शेतातून पाण्याचा जलद निचरा करा.'
        },
        'schemes': ['PM Fasal Bima Yojana', 'Sub-Mission on Plant Protection']
    },
    'potato_healthy': {
        'crop': 'Potato',
        'severity': 'Low',
        'en': {
            'name': 'Healthy Potato Leaf',
            'description': 'Foliage shows deep green color with firm leaves. Tubers are developing well beneath the soil.',
            'causes': 'Healthy soil structure, correct fertilization, and good crop management.',
            'prevention': 'Maintain weeding, keep hilling soil around tubers, and monitor for pests.',
            'fertilizer': 'Apply potassium-heavy fertilizers during tuber bulking phase.',
            'pesticide': 'None needed.',
            'organic_solution': 'Spray liquid seaweed extract as nutritional support.',
            'irrigation': 'Maintain consistent soil moisture, reducing slightly as harvest approaches.'
        },
        'hi': {
            'name': 'स्वस्थ आलू की पत्ती',
            'description': 'पत्तियां गहरे हरे रंग की और मजबूत हैं। मिट्टी के नीचे कंद (tubers) का विकास सही ढंग से हो रहा है।',
            'causes': 'स्वस्थ मिट्टी की संरचना, सही खाद का उपयोग और बढ़िया प्रबंधन।',
            'prevention': 'निराई-गुड़ाई जारी रखें, कंदों को ढकने के लिए मिट्टी चढ़ाएं और कीटों की निगरानी करें।',
            'fertilizer': 'आलू के आकार बढ़ने के चरण में पोटेशियम से भरपूर खाद डालें।',
            'pesticide': 'आवश्यकता नहीं है।',
            'organic_solution': 'पोषक सहायता के लिए तरल समुद्री शैवाल (seaweed) सत्व का छिड़काव करें।',
            'irrigation': 'मिट्टी में लगातार नमी बनाए रखें, खुदाई से कुछ दिन पहले सिंचाई कम कर दें।'
        },
        'mr': {
            'name': 'निरोगी बटाट्याचे पान',
            'description': 'पाने गडद हिरवी व निरोगी आहेत. जमिनीखालील बटाटे वेगाने फुगत आहेत.',
            'causes': 'चांगली जमीन, संतुलित खत व्यवस्थापन आणि योग्य देखरेख.',
            'prevention': 'तण काढा, बटाटे उघडे पडू नयेत म्हणून झाडाला मातीची भर द्या.',
            'fertilizer': 'बटाटे मोठे होण्याच्या काळात पालाश (पोटॅश) खत द्यावे.',
            'pesticide': 'गरज नाही.',
            'organic_solution': 'पिकाला पोषण देण्यासाठी समुद्री शेवाळ अर्काचा फवारा द्या.',
            'irrigation': 'जमिनीत ओलावा टिकवून ठेवा, काढणीच्या आधी काही दिवस पाणी कमी करा.'
        },
        'schemes': ['Soil Health Card Scheme']
    },

    # ------------------- RICE -------------------
    'rice_brown_spot': {
        'crop': 'Rice',
        'severity': 'Medium',
        'en': {
            'name': 'Rice Brown Spot',
            'description': 'A fungal disease caused by Bipolaris oryzae. It leads to numerous small, oval brown spots with yellow halos on rice leaves.',
            'causes': 'Nutrient-deficient soils (especially lacking potassium), drought conditions, or high humidity.',
            'prevention': 'Improve soil fertility by applying potassium, use certified seeds, and manage water levels.',
            'fertilizer': 'Apply muriate of potash (MOP) to correct potassium deficiency.',
            'pesticide': 'Spray Mancozeb, Hexaconazole, or Propiconazole.',
            'organic_solution': 'Treat seeds with Trichoderma viride or spray neem seed kernel extract.',
            'irrigation': 'Keep the field appropriately flooded; avoid moisture stress or drying cycles.'
        },
        'hi': {
            'name': 'धान का भूरा धब्बा (Brown Spot)',
            'description': 'बाइपोलारिस ओराइजे कवक के कारण होता है। धान की पत्तियों पर पीले रंग के प्रभामंडल के साथ छोटे, अंडाकार भूरे रंग के धब्बे बन जाते हैं।',
            'causes': 'पोषक तत्वों की कमी (विशेषकर पोटाश की कमी), सूखा या उच्च आर्द्रता।',
            'prevention': 'पोटेशियम का प्रयोग कर मिट्टी की उर्वरता में सुधार करें, प्रमाणित बीजों का उपयोग करें और पानी का उचित प्रबंधन करें।',
            'fertilizer': 'पोटेशियम की कमी को दूर करने के लिए म्यूटेट ऑफ पोटाश (MOP) का प्रयोग करें।',
            'pesticide': 'मैनकोजेब, हेक्साकोनाज़ोल या प्रोपिकोनाज़ोल का छिड़काव करें।',
            'organic_solution': 'बीजों को ट्राइकोडर्मा विरिडी से उपचारित करें या नीम के बीज के अर्क का छिड़काव करें।',
            'irrigation': 'खेत में उचित पानी बनाए रखें; धान को सूखने या पानी की कमी से बचाएं।'
        },
        'mr': {
            'name': 'भातावरील तांबेरा/तपकिरी ठिपके (Brown Spot)',
            'description': 'बायपोलारिस ओरायझे बुरशीमुळे पानांवर पिवळसर कडा असलेले लंबगोलाकार तपकिरी ठिपके पडतात.',
            'causes': 'जमिनीत अन्नद्रव्यांची कमतरता (विशेषतः पोटॅशची), दुष्काळी परिस्थिती किंवा जास्त दमटपणा.',
            'prevention': 'पोटॅशियम खतांचा वापर वाढवून जमिनीची सुपीकता सुधारा, निरोगी बियाणे निवडा.',
            'fertilizer': 'पोटॅशची कमतरता भरून काढण्यासाठी म्युरेट ऑफ पोटॅश (MOP) खत द्या.',
            'pesticide': 'मँकोझेब, हेक्साकोनाझोल किंवा प्रोपिकोनाझोल बुरशीनाशक फवारावे.',
            'organic_solution': 'ट्रायकोडर्मा विरिडीद्वारे बियाणे प्रक्रिया करा आणि निंबोळी अर्काची फवारणी करा.',
            'irrigation': 'शेतात योग्य प्रमाणात पाणी साठवून ठेवा, जमिनीला भेगा पडू देऊ नका.'
        },
        'schemes': ['Rashtriya Krishi Vikas Yojana', 'PM Fasal Bima Yojana']
    },
    'rice_leaf_blast': {
        'crop': 'Rice',
        'severity': 'High',
        'en': {
            'name': 'Rice Leaf Blast',
            'description': 'Caused by Magnaporthe oryzae. Lesions are spindle-shaped (diamond-shaped) with gray centers and brown borders, which can coalesce and kill leaves.',
            'causes': 'Cool temperatures (20-25°C), high relative humidity (>90%), long dew periods, and high nitrogen application.',
            'prevention': 'Avoid excessive nitrogen fertilizers, plant resistant crop varieties, and burn stubble after harvest.',
            'fertilizer': 'Reduce nitrogen doses and apply silicon-based fertilizers to strengthen plant tissue.',
            'pesticide': 'Spray Tricyclazole, Isoprothiolane, or Azoxystrobin.',
            'organic_solution': 'Use Pseudomonas fluorescens formulation for seed treatment and foliar spray.',
            'irrigation': 'Avoid water stress. Flooding reduces blast severity.'
        },
        'hi': {
            'name': 'धान का ब्लास्ट रोग (Leaf Blast)',
            'description': 'मैग्नापोर्टे ओराइजे कवक के कारण होता है। पत्तियों पर तकली के आकार (हीरे जैसी) के धब्बे बनते हैं जिनके केंद्र में धूसर (gray) रंग होता है।',
            'causes': 'कम तापमान (20-25°C), उच्च आर्द्रता (>90%), पत्तों पर ओस का देर तक टिकना और अधिक नाइट्रोजन खाद का प्रयोग।',
            'prevention': 'अत्यधिक नाइट्रोजन उर्वरकों से बचें, प्रतिरोधी किस्में लगाएं और फसल के अवशेषों को नष्ट करें।',
            'fertilizer': 'नाइट्रोजन की मात्रा कम करें और धान को मजबूत बनाने के लिए सिलिकॉन आधारित खादों का उपयोग करें।',
            'pesticide': 'ट्राइसाइक्लाजोल, आइसोप्रोथियोलेन या अजोक्सिस्ट्रोबिन का छिड़काव करें।',
            'organic_solution': 'स्यूडोमोनास फ्लोरेसेंस जैविक कवकनाशी का प्रयोग बीज उपचार और छिड़काव के लिए करें।',
            'irrigation': 'खेत में सूखा न पड़ने दें, पानी का सतत भराव ब्लास्ट के प्रभाव को कम करता है।'
        },
        'mr': {
            'name': 'भातावरील कडापा/करपा रोग (Leaf Blast)',
            'description': 'मॅग्नापोर्थे ओरायझे बुरशीमुळे पानांवर डोळ्याच्या आकाराचे (मध्यभागी राखाडी, कडेला तपकिरी) ठिपके पडतात व पाने जळतात.',
            'causes': 'कमी तापमान (२०-२५ अंश सेल्सिअस), हवेत जास्त ओलावा आणि नत्राचा जास्त वापर.',
            'prevention': 'नत्रयुक्त खतांचा वापर मर्यादित ठेवा, रोगप्रतिकारक जाती लावा, कापणीनंतर धानाचा पेंढा नष्ट करा.',
            'fertilizer': 'नत्राचा डोस कमी करा आणि सिलिकॉन खतांचा वापर करा जेणेकरून पाने टणक होतील.',
            'pesticide': 'ट्रायसायक्लाझोल, आयसोप्रोथिओलेन किंवा अझॉक्सीस्ट्रोबिन फवारावे.',
            'organic_solution': 'स्यूडोमोनास फ्लोरेसेन्स जिवाणू औषधाची बियाण्यांवर प्रक्रिया व फवारणी करा.',
            'irrigation': 'जमिनीला कोरडे पडू देऊ नका. शेतात पाणी साठवणे ब्लास्ट रोखण्यास मदत करते.'
        },
        'schemes': ['PM Fasal Bima Yojana', 'Sub-Mission on Plant Protection']
    },
    'rice_bacterial_leaf_blight': {
        'crop': 'Rice',
        'severity': 'High',
        'en': {
            'name': 'Bacterial Leaf Blight (BLB)',
            'description': 'A systemic bacterial infection caused by Xanthomonas oryzae. Yellowish-green wavy stripes run down leaf margins, causing wilting and kresek.',
            'causes': 'High temperature (25-34°C), strong winds, driving rains, and high nitrogen fertilizer.',
            'prevention': 'Keep fields clean, avoid flooding during early seedling stage, and plant resistant rice varieties.',
            'fertilizer': 'Avoid top-dressing nitrogen fertilizers when blight symptoms are visible.',
            'pesticide': 'Spray Streptocycline antibiotic (0.01%) along with copper hydroxide.',
            'organic_solution': 'Spray fresh cow dung extract (5%) or apply lime solution on leaves.',
            'irrigation': 'Drain fields for 2-3 days when disease is noticed to stop bacterial spread.'
        },
        'hi': {
            'name': 'जीवाणुज पत्ती झुलसा (Bacterial Leaf Blight)',
            'description': 'जैंथोमोनास ओराइजे जीवाणु के कारण होने वाला रोग। पत्ती के किनारों पर हल्के पीले-हरे रंग की लहरदार पट्टियां बनती हैं, जिससे पत्तियां सूख जाती हैं।',
            'causes': 'अधिक तापमान (25-34°C), तेज हवाएं, भारी बारिश और नाइट्रोजन का अधिक प्रयोग।',
            'prevention': 'खेतों को साफ रखें, नर्सरी में पानी का भराव न होने दें, प्रतिरोधी किस्में लगाएं।',
            'fertilizer': 'रोग के लक्षण दिखने पर तुरंत नाइट्रोजन खाद डालना बंद करें।',
            'pesticide': 'स्ट्रेप्टोसाइक्लिन एंटीबायोटिक (0.01%) को कॉपर हाइड्रॉक्साइड के साथ मिलाकर छिड़काव करें।',
            'organic_solution': 'ताजे गाय के गोबर के अर्क (5%) या चूने के पानी का छिड़काव पत्तों पर करें।',
            'irrigation': 'जीवाणुओं के प्रसार को रोकने के लिए रोग दिखने पर खेत से 2-3 दिनों के लिए पानी निकाल दें।'
        },
        'mr': {
            'name': 'भातावरील जिवाणूजन्य करपा (BLB)',
            'description': 'झँथोमोनास ओरायझे या जिवाणूमुळे पानांच्या कडा पिवळ्या पडतात आणि नंतर संपूर्ण पान जळून जाते.',
            'causes': 'जास्त तापमान (२५-३४ अंश सेल्सिअस), वादळी वारा, अतिवृष्टी आणि नत्राचा जास्त डोस.',
            'prevention': 'खेत तणमुक्त ठेवा, रोपे काढताना मुळांना इजा होऊ देऊ नका, प्रतिकारक वाण वापरा.',
            'fertilizer': 'रोग दिसल्यास युरिया किंवा इतर नत्रयुक्त खतांचा वापर तात्काळ थांबवा.',
            'pesticide': 'स्ट्रेप्टोसायक्लीन अँटीबायोटिक (०.०१%) आणि कॉपर हायड्रॉक्साइड एकत्रित फवारा.',
            'organic_solution': 'शेणाच्या अर्काची (५%) किंवा चुन्याच्या पाण्याची पानांवर फवारणी करा.',
            'irrigation': 'प्रादुर्भाव वाढल्यास २ ते ३ दिवस शेतातील पाणी पूर्णपणे बाहेर काढून टाका.'
        },
        'schemes': ['Sub-Mission on Plant Protection']
    },
    'rice_healthy': {
        'crop': 'Rice',
        'severity': 'Low',
        'en': {
            'name': 'Healthy Rice Leaf',
            'description': 'Deep green erect leaves indicating optimal chlorophyll levels and absence of pathogens.',
            'causes': 'Good water-level management, high organic carbon in soil, and balanced macro/micronutrients.',
            'prevention': 'Monitor nitrogen input, practice proper weed management, and maintain constant water level.',
            'fertilizer': 'Apply recommended NPK doses in 3 split applications (basal, tillering, panicle initiation).',
            'pesticide': 'None.',
            'organic_solution': 'Apply bio-fertilizers like Azospirillum or Blue-Green Algae.',
            'irrigation': 'Maintain standing water level of 2-5 cm during tillering to panicle stages.'
        },
        'hi': {
            'name': 'स्वस्थ धान की पत्ती',
            'description': 'गहरे हरे रंग की खड़ी पत्तियां जो अच्छे क्लोरोफिल स्तर और रोगजनकों की अनुपस्थिति को दर्शाती हैं।',
            'causes': 'अच्छा जल प्रबंधन, मिट्टी में जैविक कार्बन और संतुलित पोषक तत्व।',
            'prevention': 'नाइट्रोजन की निगरानी करें, खरपतवार नियंत्रण अपनाएं और पानी का स्तर बनाए रखें।',
            'fertilizer': 'एनपीके की अनुशंसित मात्रा को तीन किश्तों में डालें (बुवाई, कल्ले फूटने और बाली निकलने के समय)।',
            'pesticide': 'कोई नहीं।',
            'organic_solution': 'एजोस्पिरिलम या नीली-हरी काई (BGA) जैसे जैव उर्वरकों का प्रयोग करें।',
            'irrigation': 'कल्ले निकलने और बाली बनने के समय खेत में 2-5 सेमी पानी खड़ा रखें।'
        },
        'mr': {
            'name': 'निरोगी भाताचे पान',
            'description': 'पाने गर्द हिरव्या रंगाची असून रोगमुक्त आहेत. धान पीक जोमदार वाढत आहे.',
            'causes': 'योग्य पाणी पातळी, जमिनीतील सेंद्रिय कर्ब आणि संतुलित खत नियोजन.',
            'prevention': 'युरियाचा अतिवापर टाळा, वेळेवर तण नियंत्रण करा आणि योग्य प्रमाणात पाणी ठेवा.',
            'fertilizer': 'शिफारस केलेले एनपीके खत तीन हप्त्यांत द्या (लागवड, फुटवे फुटणे आणि लोंबी येताना).',
            'pesticide': 'गरज नाही.',
            'organic_solution': 'अझोस्पिरिलम किंवा निळे-हिरवे शेवाळ (BGA) सारख्या जिवाणू खतांचा वापर करा.',
            'irrigation': 'फुटवे येण्यापासून लोंबी येईपर्यंत शेतात २ ते ५ सेमी पाणी साठवून ठेवा.'
        },
        'schemes': ['Soil Health Card Scheme', 'Paramparagat Krishi Vikas Yojana']
    },

    # ------------------- MAIZE -------------------
    'maize_common_rust': {
        'crop': 'Maize',
        'severity': 'Medium',
        'en': {
            'name': 'Maize Common Rust',
            'description': 'Caused by Puccinia sorghi. It is characterized by small, powdery cinnamon-brown pustules on both upper and lower leaf surfaces.',
            'causes': 'Cool temperatures (16-23°C) and high relative humidity (>95%).',
            'prevention': 'Plant resistant hybrids, rotate crops with legumes, and plow under residues.',
            'fertilizer': 'Ensure balanced potassium levels to minimize rust susceptibility.',
            'pesticide': 'Spray Mancozeb or Tebuconazole if infection is early and severe.',
            'organic_solution': 'Dust sulfur powder or spray garlic extract solution.',
            'irrigation': 'Water early in the morning so the sun dries leaves quickly.'
        },
        'hi': {
            'name': 'मक्का का सामान्य रस्ट (Common Rust)',
            'description': 'पुक्सिनिया सोर्गी के कारण होता है। पत्तियों के ऊपर और नीचे दोनों सतहों पर दालचीनी जैसे भूरे रंग के पाउडर जैसे उभरे हुए धब्बे दिखाई देते हैं।',
            'causes': 'ठंडा तापमान (16-23°C) और अत्यधिक आर्द्रता (>95%)।',
            'prevention': 'प्रतिरोधी संकर किस्में उगाएं, दलहनी फसलों के साथ फसल चक्र अपनाएं और अवशेषों को दबा दें।',
            'fertilizer': 'रस्ट के प्रभाव को कम करने के लिए पोटेशियम का पर्याप्त उपयोग करें।',
            'pesticide': 'मैनकोजेब या टेबुकोनाज़ोल का छिड़काव करें यदि रोग प्रारंभिक अवस्था में तीव्र हो।',
            'organic_solution': 'गंधक (sulfur) पाउडर का भुरकाव करें या लहसुन के अर्क का छिड़काव करें।',
            'irrigation': 'सुबह जल्दी पानी दें ताकि धूप निकलने पर पत्तियां जल्दी सूख जाएं।'
        },
        'mr': {
            'name': 'मक्यावरील तांबेरा रोग (Common Rust)',
            'description': 'पक्सिनिया सोर्गी बुरशीमुळे पानांच्या दोन्ही बाजूंना विटकरी रंगाचे पावडरसारखे फोड येतात.',
            'causes': 'थंड हवामान (१६-२३ अंश सेल्सिअस) आणि हवेत जास्त दमटपणा.',
            'prevention': 'प्रतिकारक हायब्रीड बियाणे वापरा, कडधान्यांसोबत पीक फिरवा, जुने अवशेष जमिनीत गाडून टाका.',
            'fertilizer': 'तांबेरा प्रादुर्भाव कमी करण्यासाठी जमिनीत पोटॅशचे प्रमाण योग्य ठेवा.',
            'pesticide': 'तीव्रता जास्त असल्यास मँकोझेब किंवा टेब्युकोनाझोल बुरशीनाशक फवारावे.',
            'organic_solution': 'गंधक पावडर डस्ट करा किंवा लसणाचा अर्क फवारा.',
            'irrigation': 'सकाळी लवकर पाणी द्या जेणेकरून पानांवरील ओलावा सूर्यप्रकाशाने निघून जाईल.'
        },
        'schemes': ['PM Fasal Bima Yojana']
    },
    'maize_gray_leaf_spot': {
        'crop': 'Maize',
        'severity': 'High',
        'en': {
            'name': 'Maize Gray Leaf Spot',
            'description': 'Caused by Cercospora zeae-maydis. It creates long, rectangular, pale brown to gray spots restricted by leaf veins.',
            'causes': 'Warm, humid weather, and minimum-tillage fields with surface crop debris.',
            'prevention': 'Tillage to bury crop debris, rotate crops for at least 1-2 years, and plant tolerant varieties.',
            'fertilizer': 'Apply phosphorus and micronutrients like zinc to improve leaf health.',
            'pesticide': 'Foliar application of Pyraclostrobin or Propiconazole.',
            'organic_solution': 'Use copper-based organic sprays or baking soda solutions.',
            'irrigation': 'Ensure proper soil drainage. Over-saturation in high temperatures worsens the spots.'
        },
        'hi': {
            'name': 'मक्का का ग्रे लीफ स्पॉट (Gray Leaf Spot)',
            'description': 'सर्कॉस्पोरा ज़ी-मेयडिस कवक से जनित। पत्तियों पर लंबी, आयताकार, हल्के भूरे रंग की पट्टियां बनती हैं जो पत्तियों की नसों तक सीमित रहती हैं।',
            'causes': 'गर्म व आर्द्र मौसम और खेत में पिछली फसल का कचरा (न्यूनतम जुताई)।',
            'prevention': 'कचरे को मिट्टी में दबाने के लिए गहरी जुताई करें, कम से कम 1-2 वर्ष का फसल चक्र अपनाएं।',
            'fertilizer': 'पत्तियों को स्वस्थ रखने के लिए फास्फोरस और जिंक जैसे सूक्ष्म पोषक तत्व डालें।',
            'pesticide': 'पाइराक्लोस्ट्रोबिन या प्रोपिकोनाज़ोल का पर्णीय छिड़काव करें।',
            'organic_solution': 'कॉपर आधारित जैविक स्प्रे या बेकिंग सोडा घोल का प्रयोग करें।',
            'irrigation': 'मिट्टी की जल निकासी सही रखें। उच्च तापमान में अधिक पानी धब्बों को बढ़ाता है।'
        },
        'mr': {
            'name': 'मक्यावरील राखाडी करपा (Gray Leaf Spot)',
            'description': 'सर्कॉस्पोरा झी-मेयडीस मुळे पानांवर लांबट, चौकोनी राखाडी-तपकिरी रंगाचे पट्टे तयार होतात.',
            'causes': 'उबदार व दमट हवामान आणि शेतात पिकाचे जुने अवशेष सडत राहणे.',
            'prevention': 'खोल नांगरणी करून पिकाचे अवशेष गाडून टाका, १-२ वर्षे मका पीक घेणे टाळा.',
            'fertilizer': 'पानांची प्रतिकारशक्ती वाढवण्यासाठी फॉस्फरस आणि जस्त (झिंक) खते द्या.',
            'pesticide': 'पायराक्लोस्ट्रोबिन किंवा प्रोपिकोनाझोल बुरशीनाशक फवारावे.',
            'organic_solution': 'सेंद्रिय कॉपर स्प्रे किंवा बेकिंग सोडा द्रावण वापरावे.',
            'irrigation': 'शेतात पाणी साठणार नाही याची काळजी घ्या. पाणी योग्य निचरा होणाऱ्या जमिनीत द्या.'
        },
        'schemes': ['Sub-Mission on Plant Protection']
    },
    'maize_northern_leaf_blight': {
        'crop': 'Maize',
        'severity': 'High',
        'en': {
            'name': 'Northern Corn Leaf Blight (NCLB)',
            'description': 'Caused by Exserohilum turcicum. It causes large, cigar-shaped grayish-green lesions (up to 15 cm long) on leaves.',
            'causes': 'Moderate temperatures (18-27°C) along with heavy dew and rainy conditions.',
            'prevention': 'Sow resistant maize hybrids, rotate crops, and practice clean tillage.',
            'fertilizer': 'Avoid excessive nitrogen; ensure balanced soil fertility.',
            'pesticide': 'Spray Mancozeb or Azoxystrobin + Difenoconazole combination.',
            'organic_solution': 'Spray copper fungicides or use Trichoderma species on soil.',
            'irrigation': 'Avoid sprinkler irrigation. Switch to furrow or drip irrigation.'
        },
        'hi': {
            'name': 'उत्तरी मक्का पत्ती झुलसा (NCLB)',
            'description': 'एक्ससेरोहिलम टर्सिकम कवक के कारण होता है। पत्तियों पर बड़े, सिगार के आकार के धूसर-हरे रंग के घाव (15 सेमी लंबे तक) बनते हैं।',
            'causes': 'मध्यम तापमान (18-27°C) और लंबे समय तक भारी ओस या बारिश।',
            'prevention': 'प्रतिरोधी मक्का संकर बोएं, फसल चक्र अपनाएं और साफ-सुथरी जुताई करें।',
            'fertilizer': 'अत्यधिक नाइट्रोजन से बचें; संतुलित मिट्टी उर्वरता सुनिश्चित करें।',
            'pesticide': 'मैनकोजेब या एजोक्सिस्ट्रोबिन + डिफेनोकोनाज़ोल संयोजन का छिड़काव करें।',
            'organic_solution': 'कॉपर फंगिसाइड्स का छिड़काव करें या मिट्टी में ट्राइकोडर्मा का प्रयोग करें।',
            'irrigation': 'स्प्रिंकलर सिंचाई से बचें। नाली (furrow) या ड्रिप सिंचाई प्रणाली का उपयोग करें।'
        },
        'mr': {
            'name': 'मक्यावरील उत्तर करपा (NCLB)',
            'description': 'एक्सर्रोहिलम टर्सिकम मुळे पानांवर सिगारच्या आकाराचे (लांबट मोठे) राखाडी रंगाचे चट्टे पडतात.',
            'causes': 'मध्यम तापमान (१८-२७ अंश सेल्सिअस) आणि सतत पडणारे दव व पाऊस.',
            'prevention': 'प्रतिरोधक हायब्रीड वाण पेरा, योग्य पीक फेरपालट करा आणि स्वच्छ नांगरणी करा.',
            'fertilizer': 'नत्राचा अतिवापर टाळा; संतुलित खत व्यवस्थापन करा.',
            'pesticide': 'मँकोझेब किंवा अझॉक्सीस्ट्रोबिन + डिफेनोकोनाझोल फवारावे.',
            'organic_solution': 'सेंद्रिय कॉपर बुरशीनाशक फवारा किंवा ट्रायकोडर्माचा जमिनीवर वापर करा.',
            'irrigation': 'तुषार (Sprinkler) सिंचन टाळा. पाटाने किंवा ठिबक सिंचनाने पाणी द्या.'
        },
        'schemes': ['PM Fasal Bima Yojana', 'Sub-Mission on Plant Protection']
    },
    'maize_healthy': {
        'crop': 'Maize',
        'severity': 'Low',
        'en': {
            'name': 'Healthy Maize Leaf',
            'description': 'Strong upright stalk with broad, dark green leaves. Cob production is developing normally.',
            'causes': 'Optimal soil nitrogen-potassium balance, good drainage, and proper sunlight exposure.',
            'prevention': 'Monitor for stem borers, keep soil mulched, and fertilize at regular growth intervals.',
            'fertilizer': 'Apply nitrogen-phosphorus rich fertilizers (DAP/Urea) at knee-high and tasseling stages.',
            'pesticide': 'None.',
            'organic_solution': 'Apply bio-fertilizers or spray neem oil as a preventive pest defense.',
            'irrigation': 'Provide adequate water during critical stages like silking and tasseling.'
        },
        'hi': {
            'name': 'स्वस्थ मक्के की पत्ती',
            'description': 'चोड़ी, गहरे हरे रंग की पत्तियों के साथ मजबूत सीधा तना। मक्के की भुट्टियां सामान्य रूप से विकसित हो रही हैं।',
            'causes': 'अनुकूल नाइट्रोजन-पोटेशियम संतुलन, जल निकासी और सूर्य का प्रकाश।',
            'prevention': 'तना छेदक (stem borers) की निगरानी करें, समय-समय पर खाद डालें।',
            'fertilizer': 'घुटने की ऊँचाई और मन्जरी (tasseling) अवस्था में डीएपी/यूरिया डालें।',
            'pesticide': 'कोई नहीं।',
            'organic_solution': 'बचाव के तौर पर जैव उर्वरकों का प्रयोग करें या नीम के तेल का छिड़काव करें।',
            'irrigation': 'सिल्किंग और टेसलिंग जैसी नाजुक अवस्थाओं में मक्के को पर्याप्त पानी दें।'
        },
        'mr': {
            'name': 'निरोगी मक्याचे पान',
            'description': 'पाने रुंद, गडद हिरवी व झाड निरोगी आहे. कणसांचे पोषण उत्तम होत आहे.',
            'causes': 'जमिनीत पुरेसे नत्र आणि पाणी असून सूर्यप्रकाश योग्य मिळणे.',
            'prevention': 'खोडकिडीवर लक्ष ठेवा, झाडांची वाढ होताना वेळोवेळी खतांचे डोस द्या.',
            'fertilizer': 'गुडघाभर उंचीच्या काळात आणि तुरा बाहेर येताना युरिया/डीएपी खते द्या.',
            'pesticide': 'गरज नाही.',
            'organic_solution': 'जिवाणू खते वापरा किंवा प्रतिबंधात्मक उपाय म्हणून निंबोळी तेल फवारा.',
            'irrigation': 'तुरा आणि कणीस भरण्याच्या महत्त्वाच्या काळात पिकाला पाण्याचा ताण पडू देऊ नका.'
        },
        'schemes': ['Soil Health Card Scheme']
    },

    # ------------------- COTTON -------------------
    'cotton_fusarium_wilt': {
        'crop': 'Cotton',
        'severity': 'High',
        'en': {
            'name': 'Cotton Fusarium Wilt',
            'description': 'Caused by Fusarium oxysporum f. sp. vasinfectum. It causes yellowing and browning of leaf margins, followed by wilting and vascular browning of the stem.',
            'causes': 'Acidic soils, sandy soils, high soil temperature, and presence of root-knot nematodes.',
            'prevention': 'Plant certified wilt-resistant seed, raise soil pH by liming, and practice crop rotation with grains.',
            'fertilizer': 'Increase potassium fertilizer dose; reduce nitrogen input.',
            'pesticide': 'Soil drenching with Carbendazim (0.1%) around infected plants.',
            'organic_solution': 'Apply Trichoderma viride or Pseudomonas fluorescens to the soil during planting.',
            'irrigation': 'Avoid water-logging. Maintain clean, well-drained soil.'
        },
        'hi': {
            'name': 'कपास का फ्यूसेरियम विल्ट (Fusarium Wilt)',
            'description': 'फ्यूसेरियम ऑक्सीस्पोरम के कारण होता है। पत्ती के किनारे पीले व भूरे हो जाते हैं, इसके बाद पौधा मुरझा जाता है और तने के अंदर भूरे रंग की धारियां बन जाती हैं।',
            'causes': 'अम्लीय मिट्टी, रेतीली मिट्टी, उच्च तापमान और जड़-गांठ सूत्रकृमि (nematodes) की उपस्थिति।',
            'prevention': 'विल्ट-प्रतिरोधी बीज बोएं, चूने का प्रयोग कर मिट्टी के पीएच को बढ़ाएं और अनाज के साथ फसल चक्र अपनाएं।',
            'fertilizer': 'पोटेशियम उर्वरक की मात्रा बढ़ाएं; नाइट्रोजन का उपयोग कम करें।',
            'pesticide': 'संक्रमित पौधों के आसपास कार्बेंडाजिम (0.1%) का सॉयल ड्रेंचिंग (जड़ों में सिंचाई) करें।',
            'organic_solution': 'बुवाई के समय मिट्टी में ट्राइकोडर्मा विरिडी या स्यूडोमोनास फ्लोरेसेंस मिलाएं।',
            'irrigation': 'खेत में पानी जमा न होने दें। जल निकासी अच्छी रखें।'
        },
        'mr': {
            'name': 'कापसावरील मर रोग (Fusarium Wilt)',
            'description': 'फ्युसेरियम ऑक्सिस्पोरम मुळे पानांच्या कडा पिवळ्या-तपकिरी पडतात, झाड सुकते व खोड कापले असता आतील वाहिन्या काळ्या दिसतात.',
            'causes': 'आम्लधर्मी जमीन, वाळुयुक्त माती, जमिनीचे जास्त तापमान आणि सूत्रकृमींचा प्रादुर्भाव.',
            'prevention': 'मर रोगप्रतिकारक जाती लावा, जमिनीत चुना टाकून आम्लता कमी करा, तृणधान्यांसोबत पीक फिरवा.',
            'fertilizer': 'पोटॅश खतांचे प्रमाण वाढवा; नत्राचा अतिवापर टाळा.',
            'pesticide': 'झाडाच्या मुळाशी कार्बेन्डाझिम (०.१%) द्रावणाची आळवणी (Drenching) करा.',
            'organic_solution': 'लागवडीच्या वेळी शेणखतात ट्रायकोडर्मा विरिडी मिसळून जमिनीत द्या.',
            'irrigation': 'शेतात पाणी साठून राहू देऊ नका. जमिनीमध्ये हवा खेळती राहील अशी व्यवस्था करा.'
        },
        'schemes': ['Rashtriya Krishi Vikas Yojana', 'PM Fasal Bima Yojana']
    },
    'cotton_leaf_curl': {
        'crop': 'Cotton',
        'severity': 'High',
        'en': {
            'name': 'Cotton Leaf Curl Virus (CLCuV)',
            'description': 'A severe viral disease transmitted by whiteflies. Leaves cup upward/downward and develop thick veins and leaf-like growths (enations) underneath.',
            'causes': 'High whitefly populations and presence of susceptible cotton varieties.',
            'prevention': 'Eradicate weed hosts, plant CLCuV-resistant Bt cotton varieties, and maintain crop distance.',
            'fertilizer': 'Apply balanced secondary and micronutrients (Zinc, Magnesium) to reduce symptom severity.',
            'pesticide': 'Control whiteflies using Diafenthiuron, Spiromesifen, or Afidopyropen.',
            'organic_solution': 'Install yellow sticky traps and spray neem oil or fish oil rosin soap.',
            'irrigation': 'Provide stress-free, regular light irrigations.'
        },
        'hi': {
            'name': 'कपास का लीफ कर्ल वायरस (CLCuV)',
            'description': 'सफेद मक्खियों द्वारा फैलने वाला वायरस। पत्तियां ऊपर या नीचे मुड़ जाती हैं, नसें मोटी हो जाती हैं और पत्तियों के नीचे छोटी पत्ती जैसी संरचनाएं बन जाती हैं।',
            'causes': 'सफेद मक्खियों की अधिकता और संवेदनशील कपास किस्मों की बुवाई।',
            'prevention': 'नजदीकी खरपतवारों को नष्ट करें, प्रतिरोधी बीटी कपास की किस्में बोएं।',
            'fertilizer': 'लक्षणों को कम करने के लिए जस्ता (zinc) और मैग्नीशियम जैसे सूक्ष्म पोषक तत्वों का उपयोग करें।',
            'pesticide': 'डायफेंटीयूरॉन, स्पाइरोमेसिफेन या एफिडोपायरोपेन जैसे कीटनाशकों से सफेद मक्खी नियंत्रित करें।',
            'organic_solution': 'पीले चिपचिपे जाल लगाएं और नीम के तेल का छिड़काव करें।',
            'irrigation': 'बिना तनाव के समय पर हल्की सिंचाई करें।'
        },
        'mr': {
            'name': 'कापसावरील पान चुरडणारा विषाणू (CLCuV)',
            'description': 'पांढऱ्या माशीमुळे पसरणारा विषाणू. पाने वाटीसारखी वर किंवा खाली वळतात आणि पानांच्या शिरा जाड होतात.',
            'causes': 'पांढऱ्या माशीचा मोठा प्रादुर्भाव आणि रोगट वाणांची लागवड.',
            'prevention': 'पर्यायी तण नष्ट करा, पांढऱ्या माशीला प्रतिकारक बीटी कापसाचे वाण वापरा.',
            'fertilizer': 'लक्षणे कमी करण्यासाठी झिंक, मॅग्नेशियम आणि इतर सूक्ष्म अन्नद्रव्ये फवारा.',
            'pesticide': 'पांढऱ्या माशीच्या नियंत्रणासाठी डायफेंटियुरॉन किंवा स्पायरोमेसिफेन फवारा.',
            'organic_solution': 'पिवळे चिकट सापळे वापरा आणि कडुनिंब तेल किंवा साबण पाणी फवारा.',
            'irrigation': 'नियमित हलके पाणी द्या. पिकावर पाण्याचा ताण येऊ देऊ नका.'
        },
        'schemes': ['Sub-Mission on Plant Protection']
    },
    'cotton_bacterial_blight': {
        'crop': 'Cotton',
        'severity': 'Medium',
        'en': {
            'name': 'Cotton Bacterial Blight (Angular Leaf Spot)',
            'description': 'Caused by Xanthomonas citri pv. malvacearum. It causes angular, water-soaked leaf lesions, black spots on bolls, and black arm stem rot.',
            'causes': 'Warm, wet weather with high rainfall and heavy wind splashes.',
            'prevention': 'Use acid-delinted seed, practice clean tillage, and destroy old cotton stalks.',
            'fertilizer': 'Avoid nitrogen overuse. Ensure adequate potassium in the soil.',
            'pesticide': 'Spray Streptocycline (0.01%) combined with Copper Oxychloride (0.2%).',
            'organic_solution': 'Spray neem oil or treat seeds with bio-pesticides like Pseudomonas.',
            'irrigation': 'Ensure proper drainage; water logging favors bacterial multiplication.'
        },
        'hi': {
            'name': 'कपास का जीवाणुज झुलसा (Angular Leaf Spot)',
            'description': 'जैंथोमोनास के कारण होने वाला रोग। पत्तियों पर कोणीय, पानी से लथपथ धब्बे बनते हैं, टिंडों (bolls) पर काले धब्बे और तने पर सड़न (black arm) होती है।',
            'causes': 'गर्म व नम मौसम, तेज बारिश और हवा के थपेड़े।',
            'prevention': 'एसिड-डीलिंटेड बीजों का प्रयोग करें, जुताई अच्छी करें और पुराने डंठलों को जलाएं।',
            'fertilizer': 'नाइट्रोजन का अधिक उपयोग न करें। मिट्टी में पोटेशियम की मात्रा सही रखें।',
            'pesticide': 'स्ट्रेप्टोसाइक्लिन (0.01%) और कॉपर ऑक्सीक्लोराइड (0.2%) का छिड़काव करें।',
            'organic_solution': 'नीम के तेल का छिड़काव करें या स्यूडोमोनास जैसे जैव कीटनाशकों से बीज उपचार करें।',
            'irrigation': 'जल निकासी की उचित व्यवस्था करें; पानी का जमाव रोग को बढ़ावा देता है।'
        },
        'mr': {
            'name': 'कापसावरील जिवाणूजन्य करपा (दहीया/काळा डाग)',
            'description': 'झँथोमोनास जिवाणूमुळे पानांवर कोनीय पाणीदार ठिपके येतात, बोंडावर काळे डाग पडतात व फांद्या काळ्या होऊन सडतात.',
            'causes': 'उबदार व ओलसर हवामान, जोराचा पाऊस आणि वारा.',
            'prevention': 'आम्लप्रक्रिया केलेले बियाणे वापरा, शेत स्वच्छ ठेवा, कापणीनंतर कापसाची धसकटे जाळून टाका.',
            'fertilizer': 'नत्राचा वापर नियंत्रित करा. जमिनीत पालाशचे प्रमाण चांगले ठेवा.',
            'pesticide': 'स्ट्रेप्टोसायक्लिन (१० ग्रॅम) आणि कॉपर ऑक्सीक्लोराईड (२५० ग्रॅम) १०० लिटर पाण्यात मिसळून फवारा.',
            'organic_solution': 'निंबोळी तेल फवारा किंवा स्यूडोमोनास जिवाणूने बियाणे प्रक्रिया करा.',
            'irrigation': 'शेतात पाणी साठणार नाही याची काळजी घ्या; पाणी साठणे जिवाणूच्या वाढीस मदत करते.'
        },
        'schemes': ['Sub-Mission on Plant Protection']
    },
    'cotton_healthy': {
        'crop': 'Cotton',
        'severity': 'Low',
        'en': {
            'name': 'Healthy Cotton Leaf',
            'description': 'Lobate, wide green leaves showing no spots or structural deformation. Bolls are mature and white cotton is emerging.',
            'causes': 'Excellent soil prep, integrated pest management, and timely micronutrient applications.',
            'prevention': 'Monitor for sucking pests (thrips, jassids), maintain weeding, and hill up soil.',
            'fertilizer': 'Apply magnesium sulfate and boron to prevent red leaf (Lalya) and boll dropping.',
            'pesticide': 'None.',
            'organic_solution': 'Apply liquid vermicompost or cow-urine extract as a foliar tonic.',
            'irrigation': 'Irrigate during squaring and boll development; avoid moisture stress at these stages.'
        },
        'hi': {
            'name': 'स्वस्थ कपास की पत्ती',
            'description': 'चौड़ी हरी पत्तियां जिन पर कोई धब्बा या विकृति नहीं है। टिंडे (bolls) परिपक्व हैं और कपास बाहर आ रही है।',
            'causes': 'उत्कृष्ट मिट्टी की तैयारी, एकीकृत कीट प्रबंधन और समय पर सूक्ष्म पोषक तत्वों का छिड़काव।',
            'prevention': 'चूसने वाले कीटों (थ्रिप्स, जैसिड्स) की निगरानी करें और समय-समय पर निराई करें।',
            'fertilizer': 'पत्तियों को लाल होने से रोकने और टिंडे गिरने से बचाने के लिए मैग्नीशियम सल्फेट और बोरोन डालें।',
            'pesticide': 'कोई नहीं।',
            'organic_solution': 'वर्मीकम्पोस्ट या गोमूत्र के अर्क का पर्णीय छिड़काव टॉनिक के रूप में करें।',
            'irrigation': 'कली बनते समय और टिंडे विकसित होते समय आवश्यक रूप से पानी दें।'
        },
        'mr': {
            'name': 'निरोगी कापसाचे पान',
            'description': 'रुंद हिरवे पान ज्यावर कोणतेही डाग किंवा सुरकुत्या नाहीत. कापसाची बोंडे व्यवस्थित भरत आहेत.',
            'causes': 'योग्य नियोजन, एकात्मिक कीड नियंत्रण आणि वेळेवर सूक्ष्म अन्नद्रव्यांची फवारणी.',
            'prevention': 'रस शोषणाऱ्या किडींवर (मावा, तुडतुडे, थ्रिप्स) लक्ष ठेवा, तण नियंत्रण ठेवा.',
            'fertilizer': 'पान पिवळे/तांबडे पडणे (लालया रोग) रोखण्यासाठी मॅग्नेशियम सल्फेट आणि बोरॉन खत द्या.',
            'pesticide': 'गरज नाही.',
            'organic_solution': 'पिकाला सेंद्रिय ताकद देण्यासाठी गांडूळ खताचे पाणी किंवा गोमूत्र अर्क फवारा.',
            'irrigation': 'बोंडे धरण्याच्या आणि भरण्याच्या संवेदनशील काळात कापसाला पाण्याचा ताण पडू देऊ नका.'
        },
        'schemes': ['Soil Health Card Scheme', 'Paramparagat Krishi Vikas Yojana']
    },

    # ------------------- SUGARCANE -------------------
    'sugarcane_red_rot': {
        'crop': 'Sugarcane',
        'severity': 'High',
        'en': {
            'name': 'Sugarcane Red Rot',
            'description': 'Called the "cancer" of sugarcane, caused by Colletotrichum falcatum. It causes reddening of internal stalk tissues with white cross bands and sour smell.',
            'causes': 'Use of infected seed setts, water-logging, and planting in contaminated soil.',
            'prevention': 'Use certified healthy setts, practice crop rotation, and implement hot water treatment for setts.',
            'fertilizer': 'Apply balanced potassium and organic manure.',
            'pesticide': 'Drench soil or dip setts in Carbendazim solution before planting.',
            'organic_solution': 'Apply Trichoderma viride enriched farmyard manure in the furrow.',
            'irrigation': 'Avoid irrigation runoff from infected fields to healthy ones.'
        },
        'hi': {
            'name': 'गन्ने का लाल सड़न रोग (Red Rot)',
            'description': 'गन्ने का "कैंसर" कहा जाने वाला रोग, जो कोलेटोट्रिचम फाल्केटम कवक से होता है। गन्ने के आंतरिक भाग में सफ़ेद आड़ी धारियों के साथ लाल रंग और खट्टी गंध दिखाई देती है।',
            'causes': 'संक्रमित गन्ने के टुकड़ों (setts) का उपयोग, जलभराव और दूषित मिट्टी।',
            'prevention': 'स्वस्थ बीज टुकड़ों का उपयोग करें, फसल चक्र अपनाएं और गन्ने के टुकड़ों का गर्म पानी से उपचार करें।',
            'fertilizer': 'संतुलित पोटेशियम और जैविक खाद का प्रयोग करें।',
            'pesticide': 'रोपण से पहले गन्ने के टुकड़ों को कार्बेंडाजिम घोल में डुबोएं और मिट्टी में डालें।',
            'organic_solution': 'नालियों में ट्राइकोडर्मा विरिडी से समृद्ध गोबर की खाद डालें।',
            'irrigation': 'संक्रमित खेतों के बहते पानी को स्वस्थ खेतों में जाने से रोकें।'
        },
        'mr': {
            'name': 'उसावरील तांबेरी/लाल कुजव्या रोग (Red Rot)',
            'description': 'उसाचा "कॅन्सर" मानला जाणारा रोग. कोलेटोट्रिचम फालकॅटम बुरशीमुळे उसाचा आतील भाग लाल पडतो, आडवे पांढरे पट्टे दिसतात आणि आंबट वास येतो.',
            'causes': 'बाधित बेणे (Setts) वापरणे, जमिनीत पाणी साठणे आणि दूषित माती.',
            'prevention': 'निरोगी बेणे वापरा, पिकांची फेरपालट करा, लागवडीपूर्वी बेण्यांवर गरम पाण्याची प्रक्रिया (Hot Water Treatment) करा.',
            'fertilizer': 'संतुलित पोटॅश खत आणि सेंद्रिय खतांचा भरपूर वापर करा.',
            'pesticide': 'लागवडीपूर्वी बेणे कार्बेन्डाझिम द्रावणात बुडवून घ्या आणि जमिनीवर फवारा.',
            'organic_solution': 'शेणखतात ट्रायकोडर्मा बुरशी वाढवून ती लागवडीच्या वेळी सरीत टाका.',
            'irrigation': 'बाधित शेतातील पाणी निरोगी शेतात वाहून जाऊ देऊ नका.'
        },
        'schemes': ['PM Fasal Bima Yojana', 'Sub-Mission on Plant Protection']
    },
    'sugarcane_smut': {
        'crop': 'Sugarcane',
        'severity': 'High',
        'en': {
            'name': 'Sugarcane Smut',
            'description': 'Caused by Sporisorium scitamineum. It leads to the emergence of a long, black, whip-like structure from the growing tip of the sugarcane stalk.',
            'causes': 'Dry, warm weather and planting of infected seed setts.',
            'prevention': 'Rogue out infected plants carefully in a bag, grow resistant varieties, and avoid ratooning infected fields.',
            'fertilizer': 'Ensure adequate nitrogen and potassium balance.',
            'pesticide': 'Dip setts in Propiconazole (0.1%) solution before planting.',
            'organic_solution': 'Treat setts with hot water (52°C) for 30 minutes to kill smut spores.',
            'irrigation': 'Provide regular watering. Avoid severe moisture stress.'
        },
        'hi': {
            'name': 'गन्ने का कंडुआ रोग (Smut)',
            'description': 'स्पोरिसोरियम सिटामिनियम कवक के कारण होता है। गन्ने के बढ़ते सिरे से एक लंबी, काली, कोड़े जैसी संरचना निकलती है।',
            'causes': 'सूखा व गर्म मौसम और संक्रमित बीज सेटों का रोपण।',
            'prevention': 'संक्रमित पौधों को सावधानी से उखाड़कर नष्ट करें, प्रतिरोधी किस्में उगाएं और पेड़ी (ratooning) न लें।',
            'fertilizer': 'नाइट्रोजन और पोटेशियम का उचित संतुलन बनाए रखें।',
            'pesticide': 'रोपण से पहले सेटों को प्रोपिकोनाज़ोल (0.1%) घोल में डुबोएं।',
            'organic_solution': 'बीजाणुओं को मारने के लिए गन्ने के टुकड़ों को 30 मिनट के लिए गर्म पानी (52°C) से उपचारित करें।',
            'irrigation': 'नियमित अंतराल पर सिंचाई करें। गन्ने को गंभीर पानी की कमी से बचाएं।'
        },
        'mr': {
            'name': 'उसावरील काणी रोग (Smut)',
            'description': 'स्पोरिसोरियम सिटामिनियम बुरशीमुळे उसाच्या वाढणाऱ्या शेंड्यातून लांब, काळी, चाबकासारखी रचना बाहेर पडते.',
            'causes': 'कोरडे व उष्ण हवामान आणि बाधित बेण्याचा लागवडीसाठी वापर.',
            'prevention': 'बाधित झाडे पिशवीत झाकून बाहेर काढून नष्ट करा, प्रतिकारक जाती लावा, खोडवा पीक घेणे टाळा.',
            'fertilizer': 'नत्र आणि पालाश खतांचे योग्य संतुलन ठेवा.',
            'pesticide': 'लागवडीपूर्वी बेणे प्रोपिकोनाझोल (०.१%) द्रावणात बुडवून घ्या.',
            'organic_solution': 'बेणे काणीमुक्त करण्यासाठी गरम पाण्याच्या टाकीत (५२ अंश सेल्सिअस) ३० मिनिटे ठेवा.',
            'irrigation': 'नियमित पाणी द्या, पिकाला जास्त दिवस कोरडे ठेवू नका.'
        },
        'schemes': ['Sub-Mission on Plant Protection']
    },
    'sugarcane_yellow_leaf': {
        'crop': 'Sugarcane',
        'severity': 'Medium',
        'en': {
            'name': 'Sugarcane Yellow Leaf Disease',
            'description': 'A viral disease caused by Sugarcane Yellow Leaf Virus (SCYLV), transmitted by aphids. It causes bright yellowing of the leaf midrib on the lower surface, which spreads to the blade.',
            'causes': 'Aphid vector infestations and planting of infected vegetative setts.',
            'prevention': 'Use tissue-cultured planting material (meristem tip culture) and control aphid vectors.',
            'fertilizer': 'Apply micronutrient sprays (iron and zinc) to reduce leaf chlorosis.',
            'pesticide': 'Spray Dimethoate or Imidacloprid to control aphids.',
            'organic_solution': 'Spray neem-based formulations or release predators like ladybird beetles.',
            'irrigation': 'Provide adequate and consistent moisture to reduce plant stress.'
        },
        'hi': {
            'name': 'गन्ने का पीला पत्ता रोग (Yellow Leaf)',
            'description': 'गन्ने के पीले पत्तों का वायरस (SCYLV) के कारण होने वाला रोग, जो चेपा (aphids) द्वारा फैलता है। पत्ती के मध्य भाग (midrib) का चमकीला पीला होना, जो बाद में पूरी पत्ती में फैल जाता है।',
            'causes': 'माहू/चेपा (aphid) कीटों का हमला और संक्रमित बीज टुकड़ों का उपयोग।',
            'prevention': 'टिशू-कल्चर (ऊतक संवर्धन) से तैयार पौधों का उपयोग करें और चेपा कीटों को नियंत्रित करें।',
            'fertilizer': 'पत्तियों के पीलेपन को कम करने के लिए आयरन और जिंक का छिड़काव करें।',
            'pesticide': 'चेपा को नियंत्रित करने के लिए डाइमेथोएट या इमिडाक्लोप्रिड का छिड़काव करें।',
            'organic_solution': 'नीम आधारित दवाओं का छिड़काव करें या लेडीबर्ड बीटल जैसे मित्र कीटों को बढ़ावा दें।',
            'irrigation': 'पौधे के तनाव को कम करने के लिए नियमित रूप से सिंचाई करें।'
        },
        'mr': {
            'name': 'उसावरील पिवळे पान रोग (Yellow Leaf)',
            'description': 'मावा (Aphids) किडीद्वारे पसरणारा विषाणूजन्य रोग. पानाच्या मुख्य शिरेचा भाग खालच्या बाजूने पिवळा पडतो आणि नंतर संपूर्ण पान पिवळे होते.',
            'causes': 'मावा किडीचा वाढता प्रादुर्भाव आणि संक्रमित बेण्याचा वापर.',
            'prevention': 'उती संवर्धन (Tissue Culture) रोपे वापरा, मावा किडीचे वेळीच नियंत्रण करा.',
            'fertilizer': 'पानांमधील पिवळेपणा घालवण्यासाठी लोह (लोखंड) आणि जस्त फवारणी करा.',
            'pesticide': 'मावा नियंत्रणासाठी डायमेथोएट किंवा इमिडाक्लोप्रीड कीटकनाशक फवारा.',
            'organic_solution': 'निंबोळी अर्क फवारा किंवा लेडीबर्ड बीटल (मित्र कीटक) शेतात सोडा.',
            'irrigation': 'झाडाचा ताण कमी करण्यासाठी शेतात ओलावा टिकवून ठेवा.'
        },
        'schemes': ['Rashtriya Krishi Vikas Yojana', 'PM Fasal Bima Yojana']
    },
    'sugarcane_healthy': {
        'crop': 'Sugarcane',
        'severity': 'Low',
        'en': {
            'name': 'Healthy Sugarcane Stalk',
            'description': 'Thick solid stalks with lush green leaf canopy. Excellent sugar accumulation.',
            'causes': 'Proper spacing, deep tillage, organic manuring, and timely earthing up.',
            'prevention': 'Perform detrashed leaves removal to prevent scales/mealybugs, keep fields aerated.',
            'fertilizer': 'Apply nitrogen (Urea) and potassium at tillering and grand growth phases.',
            'pesticide': 'None.',
            'organic_solution': 'Apply bio-fertilizer Acetobacter or Azotobacter for nitrogen fixation.',
            'irrigation': 'Provide heavy irrigation during tillering and formative phases; reduce near harvest.'
        },
        'hi': {
            'name': 'स्वस्थ गन्ने का पौधा',
            'description': 'घने हरे पत्तों के शामियाने के साथ मोटा ठोस तना। शर्करा का संचय बहुत अच्छा है।',
            'causes': 'उचित दूरी, गहरी जुताई, जैविक खाद का प्रयोग और समय पर मिट्टी चढ़ाना।',
            'prevention': 'हवादार खेत रखने के लिए सूखी पत्तियों को हटाते रहें (detrashing)।',
            'fertilizer': 'कल्ले फूटते समय और विकास की मुख्य अवस्था में यूरिया और पोटाश डालें।',
            'pesticide': 'कोई नहीं।',
            'organic_solution': 'नाइट्रोजन स्थिरीकरण के लिए एसीटोबैक्टर या एजोटोबैक्टर जैव उर्वरक का प्रयोग करें।',
            'irrigation': 'कल्ले फूटने और शुरुआती विकास के समय भरपूर पानी दें; कटाई के पास पानी कम करें।'
        },
        'mr': {
            'name': 'निरोगी ऊस पीक',
            'description': 'ऊस जोमदार, जाड असून पाने हिरवीगार आहेत. उसात साखरेचे प्रमाण उत्तम तयार होत आहे.',
            'causes': 'दोन सऱ्यांमधील योग्य अंतर, खोल नांगरणी, भरपूर शेणखत आणि वेळेवर भर देणे.',
            'prevention': 'हवा खेळती राहण्यासाठी उसाची वाळलेली पाने काढत राहा (Detrashing).',
            'fertilizer': 'फुटवे येताना आणि ऊस वाढीच्या काळात वेळेवर नत्र आणि पालाश खते द्या.',
            'pesticide': 'गरज नाही.',
            'organic_solution': 'नत्र स्थिरीकरणासाठी ॲसिटोबॅक्टर किंवा अझोटोबॅक्टर या जिवाणू खतांचा वापर करा.',
            'irrigation': 'वाढीच्या सुरुवातीच्या काळात मुबलक पाणी द्या, तोडणीच्या आधी पाणी देणे थांबवा.'
        },
        'schemes': ['Soil Health Card Scheme', 'Rashtriya Krishi Vikas Yojana']
    },

    # ------------------- SOYBEAN -------------------
    'soybean_rust': {
        'crop': 'Soybean',
        'severity': 'High',
        'en': {
            'name': 'Soybean Rust',
            'description': 'A destructive fungal disease caused by Phakopsora pachyrhizi. Small, tan-to-reddish-brown lesions with volcano-like pustules form on leaf undersides.',
            'causes': 'Wet leaf conditions, high relative humidity, and temperatures between 15-28°C.',
            'prevention': 'Plant early-maturing varieties, avoid narrow row spacing, and monitor fields during flowering.',
            'fertilizer': 'Apply adequate potassium to increase foliar defense mechanisms.',
            'pesticide': 'Spray Propiconazole, Tebuconazole, or Azoxystrobin immediately upon detection.',
            'organic_solution': 'Use copper soap spray or apply plant oil-based biofungicides.',
            'irrigation': 'Irrigate in the morning. Avoid late afternoon sprinkler cycles.'
        },
        'hi': {
            'name': 'सोयाबीन का रस्ट (Rust)',
            'description': 'फैकोप्सोरा पैकीरहिजी कवक के कारण होने वाला विनाशकारी रोग। पत्तियों के निचले भाग पर छोटे, भूरे-लाल रंग के धब्बे और ज्वालामुखी जैसे उभार बनते हैं।',
            'causes': 'पत्तियों का गीला होना, उच्च सापेक्ष आर्द्रता और 15-28°C के बीच का तापमान।',
            'prevention': 'जल्दी पकने वाली किस्में बोएं, कतारों के बीच पर्याप्त दूरी रखें और पुष्पन के समय निगरानी करें।',
            'fertilizer': 'पत्तियों की रक्षा प्रणाली को मजबूत करने के लिए पोटेशियम का प्रयोग करें।',
            'pesticide': 'लक्षण दिखते ही प्रोपिकोनाज़ोल, टेबुकोनाज़ोल या अजोक्सिस्ट्रोबिन का छिड़काव करें।',
            'organic_solution': 'कॉपर सोप का छिड़काव करें या वनस्पति तेल आधारित जैविक कवकनाशियों का प्रयोग करें।',
            'irrigation': 'सुबह के समय सिंचाई करें। दोपहर के बाद स्प्रिंकलर चलाने से बचें।'
        },
        'mr': {
            'name': 'सोयाबीनवरील तांबेरा रोग (Rust)',
            'description': 'फॅकोप्सोरा पॅकिरिझाय बुरशीमुळे होणारा गंभीर रोग. पानाच्या मागच्या बाजूला ज्वालामुखीच्या मुखासारखे लहान फोड दिसतात.',
            'causes': 'पाने ओली राहणे, हवेतील प्रचंड दमटपणा आणि १५-२८ अंश सेल्सिअस तापमान.',
            'prevention': 'लवकर येणारे वाण पेरा, दोन ओळीत योग्य अंतर ठेवा आणि फुलोरा अवस्थेत पिकाची पाहणी करा.',
            'fertilizer': 'पानांची प्रतिकारशक्ती वाढवण्यासाठी पोटॅश खतांचा पुरेसा वापर करा.',
            'pesticide': 'रोग दिसताच प्रोपिकोनाझोल, टेब्युकोनाझोल किंवा अझॉक्सीस्ट्रोबिन फवारा.',
            'organic_solution': 'कॉपर सोप किंवा वनस्पती तेलावर आधारित सेंद्रिय बुरशीनाशक फवारावे.',
            'irrigation': 'सकाळी पाणी द्या. संध्याकाळी तुषार सिंचन चालवणे पूर्णपणे टाळा.'
        },
        'schemes': ['PM Fasal Bima Yojana', 'Sub-Mission on Plant Protection']
    },
    'soybean_downy_mildew': {
        'crop': 'Soybean',
        'severity': 'Low',
        'en': {
            'name': 'Soybean Downy Mildew',
            'description': 'Caused by Peronospora manshurica. Pale green-to-yellow spots appear on the upper leaf surface, with gray tufts of mold on the lower surface.',
            'causes': 'Cool temperatures (20-22°C) and high humidity or wet leaf surfaces.',
            'prevention': 'Use fungicide-treated seeds, rotate crops with corn or wheat, and plow under residues.',
            'fertilizer': 'Apply balanced NPK to promote general plant health.',
            'pesticide': 'Use Metalaxyl seed treatment or spray Mancozeb.',
            'organic_solution': 'Dust sulfur dust powder or spray dilute milk-water mixture (1:9).',
            'irrigation': 'Ensure proper soil drainage. Avoid overwatering.'
        },
        'hi': {
            'name': 'सोयाबीन का डाउनी मिल्ड्यू (Downy Mildew)',
            'description': 'पेरोनोस्पोरा मैन्शुरिका कवक के कारण होता है। पत्तियों की ऊपरी सतह पर हल्के हरे-पीले धब्बे और निचली सतह पर राखाडी रंग की फफूंद दिखाई देती है।',
            'causes': 'ठंडा तापमान (20-22°C) और अत्यधिक आर्द्रता या पत्तों का गीला रहना।',
            'prevention': 'कवकनाशी-उपचारित बीजों का उपयोग करें, मक्का या गेहूं के साथ फसल चक्र अपनाएं।',
            'fertilizer': 'सामान्य पौधे के स्वास्थ्य को बढ़ावा देने के लिए संतुलित एनपीके (NPK) डालें।',
            'pesticide': 'मेटालैक्सिल बीज उपचार का उपयोग करें या मैनकोजेब का छिड़काव करें।',
            'organic_solution': 'सल्फर डस्ट पाउडर छिड़कें या पानी मिश्रित दूध का घोल (1:9) छिड़कें।',
            'irrigation': 'मिट्टी की जल निकासी ठीक रखें। अधिक पानी देने से बचें।'
        },
        'mr': {
            'name': 'सोयाबीनवरील केवडा रोग (Downy Mildew)',
            'description': 'पेरोनोस्पोरा मानशुरिका बुरशीमुळे पानाच्या वरच्या बाजूला पिवळसर ठिपके आणि पाठीमागे राखाडी रंगाची बुरशी वाढते.',
            'causes': 'थंड हवामान (२०-२२ अंश सेल्सिअस) आणि पानांवर सतत साठणारा ओलावा.',
            'prevention': 'बुरशीनाशक प्रक्रिया केलेले बियाणे वापरा, मका किंवा गव्हा सोबत फेरपालट करा.',
            'fertilizer': 'पिकाच्या वाढीसाठी शिफारशीनुसार संतुलित खत व्यवस्थापन करा.',
            'pesticide': 'मेटालॅक्सिल औषधाने बीजप्रक्रिया करा किंवा मँकोझेब बुरशीनाशक फवारा.',
            'organic_solution': 'गंधक पावडर डस्ट करा किंवा दुधाचे पाण्याचे द्रावण फवारा.',
            'irrigation': 'शेतातील पाण्याचा योग्य निचरा करा. ओलावा जास्त काळ साठू देऊ नका.'
        },
        'schemes': ['Sub-Mission on Plant Protection']
    },
    'soybean_frogeye_leaf_spot': {
        'crop': 'Soybean',
        'severity': 'Medium',
        'en': {
            'name': 'Frogeye Leaf Spot',
            'description': 'Caused by Cercospora sojina. It causes circular gray spots with dark reddish-brown borders, resembling a frog\'s eye, on leaves.',
            'causes': 'Warm, humid weather (25-30°C) with frequent rainfall.',
            'prevention': 'Use resistant soybean varieties, practice crop rotation, and till the soil.',
            'fertilizer': 'Apply potassium and secondary nutrients like magnesium.',
            'pesticide': 'Spray Strobilurin or Triazole class fungicides.',
            'organic_solution': 'Spray copper soap formulations or use compost tea sprays.',
            'irrigation': 'Ensure rows are aligned with wind directions to assist drying.'
        },
        'hi': {
            'name': 'फ्रॉग आई लीफ स्पॉट (Frogeye Leaf Spot)',
            'description': 'सर्कॉस्पोरा सोजीना कवक से जनित। पत्तियों पर काले-लाल घेरे वाले गोल भूरे धब्बे बनते हैं, जो मेंढक की आंख जैसे लगते हैं।',
            'causes': 'गर्म व आर्द्र मौसम (25-30°C) और बार-बार बारिश होना।',
            'prevention': 'प्रतिरोधी किस्मों का उपयोग करें, फसल चक्र अपनाएं और मिट्टी पलटने वाली जुताई करें।',
            'fertilizer': 'पोटेशियम और मैग्नीशियम जैसे द्वितीयक पोषक तत्व मिट्टी में डालें।',
            'pesticide': 'स्ट्रोबिल्यूरिन या ट्राईजोल वर्ग के कवकनाशी का छिड़काव करें।',
            'organic_solution': 'कॉपर सोप का छिड़काव करें या कम्पोस्ट चाय का छिड़काव करें।',
            'irrigation': 'कतारों को हवा की दिशा में रखें ताकि पत्तियां जल्दी सूख सकें।'
        },
        'mr': {
            'name': 'सोयाबीनवरील बेडूक डोळा करपा (Frogeye)',
            'description': 'सर्कॉस्पोरा सोजीना बुरशीमुळे पानांवर मध्यभागी राखाडी आणि कडेला लाल-तपकिरी गोल ठिपके दिसतात, जे बेडकाच्या डोळ्यासारखे वाटतात.',
            'causes': 'उबदार, दमट हवामान (२५-३० अंश सेल्सिअस) आणि वारंवार होणारा पाऊस.',
            'prevention': 'प्रतिरोधक वाणांची निवड करा, पीक फेरपालट करा आणि उन्हाळ्यात खोल नांगरणी करा.',
            'fertilizer': 'पोटॅश आणि मॅग्नेशियमयुक्त खतांचा वापर करा.',
            'pesticide': 'स्ट्रोबिल्युरिन किंवा ट्रायझोल गटातील बुरशीनाशकांचा वापर करा.',
            'organic_solution': 'कॉपर सोप किंवा सेंद्रिय कंपोस्ट चहा द्रावण फवारावे.',
            'irrigation': 'वारा खेळता राहील अशा प्रकारे पेरणी करा जेणेकरून पाने कोरडी राहतील.'
        },
        'schemes': ['PM Fasal Bima Yojana']
    },
    'soybean_healthy': {
        'crop': 'Soybean',
        'severity': 'Low',
        'en': {
            'name': 'Healthy Soybean Leaf',
            'description': 'Vibrant trifoliate green leaves. Pods are filling uniformly with no insect bite markings.',
            'causes': 'Correct seed inoculation with Rhizobium, optimal soil moisture, and good sunlight.',
            'prevention': 'Monitor for defoliators (semiloopers, tobacco caterpillars), keep weeded.',
            'fertilizer': 'Apply sulfur-rich fertilizers (like Gypsum) to increase oil content.',
            'pesticide': 'None.',
            'organic_solution': 'Spray neem-based formulations as a preventative pest barrier.',
            'irrigation': 'Ensure adequate moisture during flowering and pod filling stages.'
        },
        'hi': {
            'name': 'स्वस्थ सोयाबीन की पत्ती',
            'description': 'जीवंत हरी तीन-पत्ती संरचना। फलियाँ (pods) बिना किसी कीट के नुकसान के समान रूप से भर रही हैं।',
            'causes': 'राइजोबियम जीवाणु का बीज उपचार, उचित नमी और भरपूर धूप।',
            'prevention': 'पत्ती खाने वाले कीड़ों (तम्बाकू इल्ली) की निगरानी करें और खरपतवार निकालें।',
            'fertilizer': 'तेल की मात्रा बढ़ाने के लिए सल्फर युक्त खाद (जैसे जिप्सम) का प्रयोग करें।',
            'pesticide': 'कोई नहीं।',
            'organic_solution': 'बचाव के लिए नीम के तेल का घोल छिड़कें।',
            'irrigation': 'फूल आने और फलियों के दाने भरते समय खेत में नमी की कमी न होने दें।'
        },
        'mr': {
            'name': 'निरोगी सोयाबीनचे पान',
            'description': 'हिरवीगार त्रीदळ पाने आणि झाडाची वाढ जोमदार. शेंगांमध्ये दाणे भरण्यास सुरुवात झाली आहे.',
            'causes': 'पेरणीच्या वेळी रायझोबियम जीवाणू संवर्धन प्रक्रिया, योग्य ओलावा आणि ऊन.',
            'prevention': 'पाने खाणाऱ्या अळ्या (लष्करी अळी, पाने खाणारी अळी) यांवर लक्ष ठेवा.',
            'fertilizer': 'सोयाबीनमध्ये तेलाचे प्रमाण वाढवण्यासाठी गंधकयुक्त खत (जिप्सम) द्यावे.',
            'pesticide': 'गरज नाही.',
            'organic_solution': 'रस शोषक किडी व अळ्या रोखण्यासाठी प्रतिबंधात्मक निंबोळी तेल फवारा.',
            'irrigation': 'फुलोरा आणि शेंगा भरण्याच्या अत्यंत संवेदनशील टप्प्यावर पिकाला पाण्याचा ताण पडू देऊ नका.'
        },
        'schemes': ['Soil Health Card Scheme', 'Paramparagat Krishi Vikas Yojana']
    }
}

# General UI localization dictionary
UI_LOCALIZATION = {
    'en': {
        'brand': 'AgroYaar',
        'home': 'Home',
        'crop_recommendation': 'Crop Recommendation',
        'disease_detection': 'Disease Detection',
        'marketplace': 'Marketplace',
        'library': 'Disease Library',
        'contact': 'Contact Us',
        'tagline': 'Your Smart Digital Farming Friend',
        'get_started': 'Get Started',
        'select_lang': 'Language',
        'select_theme': 'Theme',
        'footer_text': '© 2026 AgroYaar. Supporting sustainable agriculture and empowering farmers.',
        'details': 'Details',
        'causes': 'Causes',
        'prevention': 'Prevention & Remedies',
        'treatments': 'Treatments',
        'organic': 'Organic Solution',
        'chemical': 'Chemical Pesticide',
        'fertilizer': 'Recommended Fertilizer',
        'irrigation': 'Irrigation Advice',
        'severity': 'Severity Level',
        'confidence': 'Confidence',
        'weather_warning': 'Weather-Aware Outbreak Alert',
        'related_schemes': 'Government Schemes & Subsidies',
        'download_pdf': 'Download Report (PDF)',
        'speak': 'Listen to Report',
        'stop': 'Stop Listening',
        'npk_calc': 'N-P-K Fertilizer & Yield Calculator',
        'land_size': 'Enter Land Size (Acres)',
        'calculate': 'Calculate',
        'npk_result': 'Required Fertilizer Quantities for your farm:',
        'urea': 'Urea (Nitrogen)',
        'ssp': 'Single Superphosphate (Phosphorus)',
        'mop': 'Muriate of Potash (Potassium)',
        'est_yield': 'Estimated Yield Range',
        'search_placeholder': 'Search disease by name or symptom...',
        'all_crops': 'All Crops'
    },
    'hi': {
        'brand': 'एग्रोयार (AgroYaar)',
        'home': 'मुख्य पृष्ठ',
        'crop_recommendation': 'फसल की सिफारिश',
        'disease_detection': 'रोग की पहचान',
        'marketplace': 'बाज़ार मूल्य',
        'library': 'रोग पुस्तकालय',
        'contact': 'सम्पर्क करें',
        'tagline': 'आपका स्मार्ट डिजिटल खेती मित्र',
        'get_started': 'शुरू करें',
        'select_lang': 'भाषा',
        'select_theme': 'थीम',
        'footer_text': '© 2026 एग्रोयार। सतत कृषि का समर्थन और किसानों का सशक्तिकरण।',
        'details': 'विवरण',
        'causes': 'कारण',
        'prevention': 'रोकथाम और उपचार',
        'treatments': 'इलाज',
        'organic': 'जैविक समाधान',
        'chemical': 'रासायनिक कीटनाशक',
        'fertilizer': 'अनुशंसित उर्वरक',
        'irrigation': 'सिंचाई सलाह',
        'severity': 'गंभीरता का स्तर',
        'confidence': 'आत्मविश्वास',
        'weather_warning': 'मौसम-जागरूक प्रकोप चेतावनी',
        'related_schemes': 'सरकारी योजनाएं और सब्सिडी',
        'download_pdf': 'रिपोर्ट डाउनलोड करें (PDF)',
        'speak': 'रिपोर्ट सुनें',
        'stop': 'सुनना बंद करें',
        'npk_calc': 'एन-पी-के (N-P-K) खाद एवं उपज कैलकुलेटर',
        'land_size': 'भूमि का आकार दर्ज करें (एकड़)',
        'calculate': 'गणना करें',
        'npk_result': 'आपके खेत के लिए आवश्यक उर्वरक की मात्रा:',
        'urea': 'यूरिया (नाइट्रोजन)',
        'ssp': 'सिंगल सुपरफॉस्फेट (फास्फोरस)',
        'mop': 'मुरिएट ऑफ पोटाश (पोटेशियम)',
        'est_yield': 'अनुमानित उपज सीमा',
        'search_placeholder': 'नाम या लक्षण द्वारा रोग खोजें...',
        'all_crops': 'सभी फसलें'
    },
    'mr': {
        'brand': 'अ‍ॅग्रोयार (AgroYaar)',
        'home': 'मुख्य पान',
        'crop_recommendation': 'पीक शिफारस',
        'disease_detection': 'रोग ओळख/तपासणी',
        'marketplace': 'बाजार भाव',
        'library': 'रोग ग्रंथालय',
        'contact': 'संपर्क साधा',
        'tagline': 'तुमचा डिजिटल शेती मित्र',
        'get_started': 'सुरू करा',
        'select_lang': 'भाषा',
        'select_theme': 'थीम',
        'footer_text': '© २०२६ अ‍ॅग्रोयार. शाश्वत शेतीचा पाठिंबा आणि बळीराजाचे सबलीकरण.',
        'details': 'तपशील',
        'causes': 'कारणे',
        'prevention': 'प्रतिबंध व उपाय',
        'treatments': 'उपचार पद्धती',
        'organic': 'सेंद्रिय उपाय',
        'chemical': 'रासायनिक कीटकनाशक',
        'fertilizer': 'शिफारस केलेले खत',
        'irrigation': 'पाण्याचे नियोजन',
        'severity': 'तीव्रता पातळी',
        'confidence': 'निश्चितता',
        'weather_warning': 'हवामान-आधारित रोग चेतावणी',
        'related_schemes': 'शासकीय योजना आणि अनुदाने',
        'download_pdf': 'अहवाल डाउनलोड करा (PDF)',
        'speak': 'अहवाल ऐका',
        'stop': 'ऐकणे थांबवा',
        'npk_calc': 'एन-पी-के (N-P-K) खत आणि उत्पन्न मोजणी',
        'land_size': 'शेती क्षेत्र टाका (एकर)',
        'calculate': 'मोजणी करा',
        'npk_result': 'तुमच्या शेतासाठी आवश्यक खतांचे प्रमाण:',
        'urea': 'युरिया (नत्र)',
        'ssp': 'सिंगल सुपरफॉस्फेट (स्फुरद)',
        'mop': 'म्युरेट ऑफ पोटॅश (पालाश)',
        'est_yield': 'अंदाजे एकूण उत्पन्न',
        'search_placeholder': 'रोगाचे नाव किंवा लक्षणाने शोधा...',
        'all_crops': 'सर्व पिके'
    }
}
