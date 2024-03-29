from app.database import (database)
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

junctions = {
    '2': {"id": 2, "name": "หัวลำโพง", "lat": 13.737908, "lng": 100.516311, "camera": [951]},
    '3': {"id": 3, "name": "มหานคร", "lat": 13.736726, "lng": 100.519133, "camera": []},
    '4': {"id": 4, "name": "สะพานเหลือง", "lat": 13.735735, "lng": 100.52161, "camera": [1121, 40, 1120]},
    '5': {"id": 5, "name": "สามย่าน", "lat": 13.732783, "lng": 100.528835, "camera": [533, 532, 531]},
    '6': {"id": 6, "name": "อังรีดูนังต์", "lat": 13.730785, "lng": 100.533573, "camera": []},
    '7': {"id": 7, "name": "ศาลาแดง", "lat": 13.729602, "lng": 100.53659, "camera": [953]},
    '8': {"id": 8, "name": "วิทยุ", "lat": 13.726334, "lng": 100.544419, "camera": [477]},
    '9': {"id": 9, "name": "ใต้ด่วนพระราม 4", "lat": 13.722911, "lng": 100.552615, "camera": []},
    '10': {"id": 10, "name": "คลองเตย", "lat": 13.721106, "lng": 100.557593, "camera": []},
    '11': {"id": 11, "name": "พระรามที่ 4", "lat": 13.720242, "lng": 100.559085, "camera": []},
    '12': {"id": 12, "name": "เกษมราษฎร์", "lat": 13.718941, "lng": 100.567157, "camera": []},
    '14': {"id": 14, "name": "กล้วยน้ำไท", "lat": 13.712945, "lng": 100.584065, "camera": []},
    '15': {"id": 15, "name": "พระโขนง", "lat": 13.714308, "lng": 100.592523, "camera": []},
    '16': {"id": 16, "name": "ณ ระนอง", "lat": 13.717685, "lng": 100.558180, "camera": []},
    '17': {"id": 17, "name": "กรมศุลกากร", "lat": 13.714643, "lng": 100.565236, "camera": []},
    '18': {"id": 18, "name": "อ่อนนุช", "lat": 13.708889, "lng": 100.599426, "camera": []},
}


def get_const_junction(id):
    if (id not in junctions):
        return "id doesn't exist on database"
    return junctions[id]

async def create_junction(junction):
    junction = jsonable_encoder(junction)
    new_junction = await database['junctions'].insert_one(junction)
    return new_junction
