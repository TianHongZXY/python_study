# coding=gbk
#上行代码可解决无法编译含有中文的字符问题
cities = {
	'xi an':{'country':'china',
			'population':'8 million',
			'fact':'famous for its RouJiaMo肉',
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
