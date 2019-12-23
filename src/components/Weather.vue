<template>
  <div>
    <div v-if="current !== undefined">
      <h1>{{ current.main.temp }}°C</h1>
      <h1>{{ current.weather[0].description }}</h1>
      <h2>{{ current.main.feels_like }}°C</h2>
      <h3>{{ current.main.temp_max + "/" + current.main.temp_min }}°C</h3>
      <p>{{ current.main.humidity }}%</p>
    </div>
    <div v-if="forecast !== undefined">
      <div 
        v-for="item in forecast.list"
        :key="item.key"
      >
        <h2>{{ getDate(item.dt) }}</h2>
        <h3>{{ item.weather[0].description }}</h3>
        <p>{{ item.main.temp_max + "/" + item.main.temp_min + "°C " + item.main.humidity + "%" }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import moment from 'moment';

async function getCurentWeather() {
    const response = await axios.get("https://api.openweathermap.org/data/2.5/weather?zip=93460,fr&units=metric&APPID=3acd0b10fd8f7ee76e05204efd0ce7af")
    return response.data

}
async function getForecastWeather() {
    const response = await axios.get("https://api.openweathermap.org/data/2.5/forecast?zip=93460,fr&units=metric&APPID=3acd0b10fd8f7ee76e05204efd0ce7af")
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
            return moment(date * 1000).calendar()
        }
    }


}
</script>

<style>

</style>