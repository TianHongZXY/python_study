# coding=gbk
#���д���ɽ���޷����뺬�����ĵ��ַ�����
cities = {
	'xi an':{'country':'china',
			'population':'8 million',
			'fact':'famous for its RouJiaMo��',
			},
	'new york':{'country':'america',
			   'population':'10 million',
			   'fact':'very big and wealthy',
			},
	'zhen jiang':{'country':'china',
				  'population':'2 million',
				  'fact':'a city with long history',
			},
	}
for cityname,city_info in cities.items():
	print("\nCityname is " + cityname)
	print("\tIt belongs to " + city_info['country'].title())
	print("\tIt's population is " + city_info['population'])
	print("\tA fact about it is that it's " + city_info['fact'])
