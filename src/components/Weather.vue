<template>
  <div class="weather">
    <div
      v-if="current !== undefined"
      class="today"
    >
      <div class="todayChild">
        Actuel <h1>{{ current.main.temp }}°C</h1>
        
        Resentie <h2>{{ current.main.feels_like }}°C</h2>
        Min / Max <h3>{{ current.main.temp_max + " / " + current.main.temp_min }}°C</h3>
        Humidité <h3>{{ current.main.humidity }}%</h3>
      </div>
      <div class="todayChild">
        <h1>{{ getDate(current.dt) }}</h1>
        <h1>{{ current.weather[0].description }}</h1>
      </div>
      <div class="todayChild">
        <img
          :src="'http://openweathermap.org/img/wn/' + current.weather[0].icon + '@2x.png'"
          class="todayIcon"
        >
      </div>
    </div>
    <div 
      v-if="forecast !== undefined"
      class="forecast"
    >
      <div 
        v-for="item in forecast.list.slice(0, 6)"
        :key="item.key"
        class="forecastChild"
      >
        <h3>{{ getDate(item.dt) }}</h3>
        <p>{{ item.weather[0].description }}</p>
        <p>{{ item.main.temp_max + " / " + item.main.temp_min + "°C " }}</p>
        <p>{{ item.main.humidity + "%" }}</p>
      </div>
    </div>
  </div>
</template>

<style>
    h1 {
      /* font: 1.3em sans-serif; */
      font: 4em sans-serif;
    }
    h2 {
      /* font: 1em sans-serif; */
      font: 3em sans-serif;
    }
    h3 {
      /* font: 0.8em sans-serif; */
      font: 2em sans-serif;
    }
    p {
      /* font: 0.7em sans-serif; */
      font: 1.7em sans-serif;
    }
    .weather {
        /* width: 50vw; */
        /* height: 50vh; */
        margin: 0;
        height: 100%;
        width: 100%
    }
    .today {
        height: 50%;
        display: flex;
        justify-content: space-around;
        align-items: center;
        flex-direction: row;
    }
    .todayChild {
        text-align: center;
    }
    .todayIcon {
        height: 300px;
    }
    .forecast {
        display: flex;
        justify-content: space-around;
        align-items: center;
        flex-direction: row;
    }
    .forecastChild {
      text-align: center;
    }
</style>

<script>
import axios from 'axios';
import moment from 'moment';

async function getCurentWeather() {
    const response = await axios.get("https://api.openweathermap.org/data/2.5/weather?zip=93460,fr&units=metric&appid=3acd0b10fd8f7ee76e05204efd0ce7af")
    return response.data

}
async function getForecastWeather() {
    const response = await axios.get("https://api.openweathermap.org/data/2.5/forecast?zip=93460,fr&units=metric&appid=3acd0b10fd8f7ee76e05204efd0ce7af")
    return response.data
}

export default {
    data() {
        return {
            forecast: undefined,
            current: undefined
        }
    },
    computed: {
    
    },
    mounted() {
        getForecastWeather().then((data) => {
            this.forecast = data
        })
        getCurentWeather().then((data) => {
            this.current = data

        })
    },
    methods: {
        getDate(date) {
            moment.locale('fr')
            var dt = moment.unix(date)
            return dt.format(moment.HTML5_FMT.TIME)
        }
    }


}
</script>
