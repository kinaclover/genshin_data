import genshinstats
import asyncio
import json


# get genshinstats data
async def get_spiral_data(uid):
    genshinstats.set_cookie_auto()
    data = genshinstats.get_characters(uid, lang='ko-kr')
    # print(data["stats"]["max_floor"])
    # print(data["stats"]["total_stars"])
    return data


sample = '테스트 | 59 | 801936571'
text = sample.split('|')[2].strip()
if len(text) < 9:
    print('error')
else:
    result = asyncio.run(get_spiral_data(text))
    # data = []
    # for temp in result:
    #     tempData = temp['name']
    # name
    # lv
    # friendship
    # constellations
    # weapon
    # artifacts
    print(type(result))
    file_path = 'test_file.json'
    with open(file_path, 'w', encoding='utf-8') as o:
        o.write(json.dumps(result, indent=2, ensure_ascii=False))

    # print(result)
    # print(json.dumps(result[1], indent=2))
    # print(json.dumps(result, indent=2))


