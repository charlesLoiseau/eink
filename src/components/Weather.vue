<template>
  <div class="weather">
    <div class="today">
      <div class="todayChild">
        <h1>{{ daily.Temperature.Maximum.Value }}°C / {{ daily.Temperature.Minimum.Value }}°C</h1>
      </div>
      <div class="todayChild">
        <img src="../assets/weather/001-cloud.png" class="todayIcon">
      </div>
    </div>
  </div>
</template>

<style>
    h1 {
        font-size: 1.7em;
    }
    .weather {
        width: 50vw;
        background-color: grey;
        height: 50vh;
        margin: 0;

    }
    .today {
        background-color: red;
        height: 50%;
        display: flex;
        justify-content: space-around;
        align-items: center;
        flex-direction: row;

    }
    .todayChild {
        background-color: blue
    }
    .todayIcon {
        height: 100px;

    }
</style>

<script>
import axios from 'axios';

async function getDailyWeather() {
    const response = await axios.get("http://dataservice.accuweather.com/forecasts/v1/daily/1day/133651?apikey=NZkRfJXuglJmtR6vYgdZFZ5bB6PfJAbV&metric=true")
    // eslint-disable-next-line no-unused-vars
    return response.data.DailyForecasts[0]

}
async function getHourlyWeather() {
    const response = await axios.get("http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/133651?apikey=NZkRfJXuglJmtR6vYgdZFZ5bB6PfJAbV&metric=true")
    return response.data
}
export default {
    data() {
        return {
            hourly: undefined,
            daily: undefined
        }
    },
    computed: {
    
    },
    mounted() {
        getHourlyWeather().then((data) => {
            this.hourly = data
        })
        getDailyWeather().then((data) => {
            this.daily = data

        })

    },


}
</script>
