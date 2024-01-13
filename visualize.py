import os
from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/')
def index():
    seoul_coordinates = (37.5665, 126.9780)
    seoul_map = folium.Map(location=seoul_coordinates, zoom_start=12)
    folium.Marker(location=seoul_coordinates, popup='서울').add_to(seoul_map)
    map_html = seoul_map.get_root().render()
    return render_template('index.html', map_html=map_html)


if __name__ == '__main__':
    # FLASK_RUN_EXTRA_FILES를 설정하여 watchdog를 비활성화
    os.environ['FLASK_RUN_EXTRA_FILES'] = 'true'

    app.run(host='127.0.0.1', debug=True, port=5000)   #use_reloader=False